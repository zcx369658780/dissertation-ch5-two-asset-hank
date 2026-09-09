"""Package the saved static audit, tests, report, and manifest."""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def write_json(path, value):
    Path(path).write_text(
        json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main(evidence_root, repo_output, report_path):
    evidence = Path(evidence_root).resolve()
    output = Path(repo_output).resolve()
    report = Path(report_path).resolve()
    summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
    mappings = json.loads((output / "temporal_mapping.json").read_text(encoding="utf-8"))
    zt = json.loads((output / "zt_audit.json").read_text(encoding="utf-8"))
    patch_plan = json.loads((output / "patch_plan.json").read_text(encoding="utf-8"))
    unresolved = json.loads((output / "unresolved_decisions.json").read_text(encoding="utf-8"))
    inventory = json.loads((output / "source_inventory.json").read_text(encoding="utf-8"))

    command = [sys.executable, "-B", str(REPO / "tests/test_mp4c_temporal_contract_audit.py")]
    environment = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONDONTWRITEBYTECODE": "1"}
    result = subprocess.run(command, cwd=REPO, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    raw_log = result.stdout
    test_text = raw_log.decode("utf-8").replace("\r\n", "\n")
    (output / "tests.txt").write_text(test_text, encoding="utf-8", newline="\n")
    match = re.search(r"Ran (\d+) tests", test_text)
    receipt = {
        "command": command,
        "returncode": result.returncode,
        "ran": int(match.group(1)) if match else None,
        "individual_ok": len(re.findall(r" \.\.\. ok$", test_text, re.MULTILINE)),
        "sha256": hashlib.sha256(raw_log).hexdigest().upper(),
        "passed": result.returncode == 0 and "\nOK\n" in test_text,
    }
    write_json(output / "tests_receipt.json", receipt)
    assert receipt["passed"] and receipt["ran"] == receipt["individual_ok"] == 6

    rows = []
    for item in mappings:
        rolling = f"{item['workbook_implied_rolling_sample_start_year']}–{item['steady_year']}"
        rows.append(
            f"| {item['ii']} | {item['steady_year']} | {item['plm_vintage']} | {rolling} | "
            f"{item['current_level_row_1based']}/{item['current_level_year']} | "
            f"{item['candidate_level_row_1based']}/{item['candidate_level_year']} | "
            f"21/2020 | {item['candidate_zt_row_1based']}/{item['candidate_zt_year']} | "
            f"`{item['plm_window_status']}` |"
        )
    mapping_table = "\n".join(rows)
    patch_rows = "\n".join(
        f"| `{item['class']}` | `{item['file']}` | `{item['current']}` | `{item['proposed']}` | {item['meaning']} |"
        for item in patch_plan
    )
    source_hashes = "\n".join(f"- `{Path(item['path']).name}`: `{item['sha256']}`" for item in inventory)
    ii1 = mappings[0]
    ii10 = mappings[9]
    ii10_zt = zt[9]
    max_fixed_difference = max(item["cache_vs_fixed_formula_max_abs"] for item in zt)
    invalid_2022 = zt[13]["candidate_invalid_provinces"]
    invalid_2023 = zt[14]["candidate_invalid_provinces"]

    report_text = f"""# Chapter 5 MP4C 年度时间合同与 Zt legacy 审计报告

- Temporal-contract verdict: `{summary['temporal_contract_verdict']}`。
- PLM preservation verdict: `{summary['plm_preservation_verdict']}`。
- Zt legacy verdict: `{summary['zt_legacy_verdict']}`。
- Results eligibility: `FALSE`。
- MATLAB、HJB/KFE/household、firm/controller、GE/annual/stationary/IRF/Results及root/direct/iterative/eigen/model solve调用均为0。

## 结论

`steady_year = 2008 + ii` 同时得到年度文件名、源码2024-06-01注释和PLM sheet vintage支持。工作簿水平数据从2000开始，因此稳态同年水平量应使用矩阵一基行 `ii+9`。生产入口仍把 `data_year=ii` 传入初始化器；该初始化器据此读取GDP、CAP、POP及人均量。因此这是 `A_CONFIRMED_INDEX_DEFECT`。`data_MAT{{ii}}` 应继续保留，因为它选择以该稳态年为end-year的PLM/cache entry；最小修复是单独把水平量行改为 `ii+9`。

PLM estimator继续冻结保留。15个vintage（10–24）、4个行业的系数与截距sheet共120张全部存在，vintage end-year与2009–2023年度序列一致。可是全部60张系数sheet都只有 `time1` 至 `time9`，加上源码“前10年的数据估计本年alpha”注释，支持固定10期滚动窗。首个vintage10与Owner的2000–2009窗口一致；vintage19更像2009–2018，而不是2000–2018扩展窗。Owner已冻结2000起始扩展窗意图，因此现存PLM artifact不符合该合同。后续独立任务需找回/冻结R估计源，并在不切换PLM estimator的前提下重建版本化系数artifact。

`load_GDPdata.m` 将所有15个cache entry的Zt固定用矩阵row21/calendar2020构造。源码注释只说明“用2020年的pgdp和pcap”，没有给出base-year、normalization或经济锚定理由；搜索到的其他regression branches也没有为固定2020提供依据。因此分类为 `LIKELY_LEGACY_FIXED_YEAR_ANCHOR`，而非`PROVEN_BUG`。保存cache的465个industry4 Zt中384个与row21公式逐位相等，全部差异最大仅 `{max_fixed_difference}`，说明其余只是binary64运算次序舍入。

另有cache身份问题：industry4的ii1–ii14 alpha与当前PLM sheet逐位一致，但ii15 cache alpha=`0.967775174774325`，当前vintage24 sheet B11=`1.0219847778591`；PLM workbook修改时间晚于cache。旧cache文件名没有数据/时间合同版本，不能证明2023 entry与当前workbook来自同一PLM artifact。

## ii=1与ii=10

- ii=1：steady/filename year=`{ii1['steady_year']}`；PLM vintage10、sheet `总面板回归系数_10_行业4`；现有布局支持2000–2009十期窗；当前水平row1/year2000，候选row10/year2009；当前Zt row21/year2020，候选row10/year2009。
- ii=10：steady/filename year=`{ii10['steady_year']}`；PLM vintage19、sheet `总面板回归系数_19_行业4`；现有布局支持2009–2018十期窗，不能证明2000–2018扩展窗；当前水平row10/year2009，候选row19/year2018；当前Zt row21/year2020，候选row19/year2018。对31个有效省份，候选Zt相对保存Zt的绝对相对变化中位数 `{ii10_zt['candidate_vs_saved_median_abs_relative_change_valid']}`、最大 `{ii10_zt['candidate_vs_saved_max_abs_relative_change_valid']}`，仅作静态算术，不是模型结果。

## 全部支持年度映射

| ii | steady/filename year | PLM vintage | workbook支持的10期窗 | 当前level row/year | 候选level row/year | 当前Zt row/year | 候选Zt row/year | PLM窗口状态 |
|---:|---:|---:|---|---|---|---|---|---|
{mapping_table}

2020对应ii12，因此只有该年固定Zt row21恰好与候选同年。候选2022 Zt遇到非正资本省份 `{', '.join(invalid_2022)}`；候选2023遇到 `{', '.join(invalid_2023)}`。这些来自前序已接受的六个负资本单元，属于D类独立数据质量问题，必须先经官方/Owner数据处理，不能用时间索引修复掩盖。

## 最小source patch plan（未执行）

| 类别 | 文件/位置 | 当前表达式 | 候选表达式 | 保留的经济含义 |
|---|---|---|---|---|
{patch_rows}

稳定态输出文件名 `Multi_Province_12sts_{{steady_year}}.mat` 已按calendar year命名，可保留；但旧输出必须用contract metadata拒绝误读。cache名称必须增加明确版本或身份，否则生产代码会直接加载旧row21 Zt并绕过修正构造。metadata至少保存并断言 `steady_year`、level row/year、PLM vintage、sample start/end/window type、Zt row/year和temporal-contract version。

## 仍需Owner或官方数据决定

1. PLM窗口含义无需再次选择：Owner已定为2000起始扩展窗。当前缺口是R生成源和符合该合同的版本化PLM coefficient artifact；后续仍用PLM重建，不切换估计器。
2. Owner需接受或拒绝将Zt水平行从固定2020改为 `ii+9`。本报告推荐接受，但只给规格，不实施。
3. ii15/industry4需确定当前PLM workbook还是旧cache系数为权威；推荐新合同采用显式版本cache，禁止静默混用。
4. 安徽2018 GDP、常住人口、固定投资/资本链及alpha/Zt provenance仍按前序 `official_data_request.csv` 待核验。
5. 2022–2023六个负资本/复数log单元是独立问题；时间对齐会使其进入对应年度Zt候选，执行前必须关闭。

## 来源身份、检查和边界

{source_hashes}

6/6项synthetic tests通过，覆盖ii1/ii10映射、全部PLM sheet命名、固定10期layout分类、Zt静态算术和import-time零科学。完整静态证据根为 `{evidence}`；`-001`因过强cache-alpha断言停止，`-002`在最终authority措辞收紧前完成，两者均保留不覆盖且科学调用为0。manifest/readback、测试原始日志与机器可读mapping/patch plan位于 `reports/mp4c_temporal_contract_audit_20260909/`。
"""
    report.write_text(report_text, encoding="utf-8", newline="\n")

    output_files = [
        report,
        REPO / "tests/test_mp4c_temporal_contract_audit.py",
        *sorted((REPO / "validators/multi_province/temporal_contract_audit").glob("*.py")),
        *sorted(path for path in output.iterdir() if path.is_file() and path.name not in ("manifest.json", "manifest_readback.json")),
    ]
    outputs = []
    for path in output_files:
        raw = path.read_bytes()
        outputs.append({
            "path": str(path.resolve()),
            "sha256": hashlib.sha256(raw).hexdigest().upper(),
            "LF_sha256": hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest().upper(),
            "bytes": len(raw),
        })
    external = [
        {"path": str(path.resolve()), "sha256": sha256(path), "bytes": path.stat().st_size}
        for path in sorted(evidence.iterdir())
        if path.is_file()
    ]
    manifest = {
        "scope": "Read-only source/workbook/cache temporal audit and allowed text delivery; excludes original workbook/cache copies, itself, and readback.",
        "sources": inventory,
        "external_evidence": external,
        "outputs": outputs,
    }
    write_json(output / "manifest.json", manifest)
    verified = 0
    for section in ("sources", "external_evidence", "outputs"):
        for item in manifest[section]:
            assert sha256(item["path"]) == item["sha256"], item["path"]
            verified += 1
    readback = {
        "manifest_sha256": sha256(output / "manifest.json"),
        "independent_files_verified": verified,
        "all_matched": True,
        "test_receipt": receipt,
        "zero_scientific_calls": summary["zero_scientific_call_ledger"],
        "evidence_root": str(evidence),
    }
    write_json(output / "manifest_readback.json", readback)
    print(json.dumps(readback, ensure_ascii=False))


if __name__ == "__main__":
    main(*sys.argv[1:])
