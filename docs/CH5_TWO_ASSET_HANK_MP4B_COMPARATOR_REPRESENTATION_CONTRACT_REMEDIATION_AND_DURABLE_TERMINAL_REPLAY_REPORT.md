# MP4B comparator representation-contract remediation and durable-terminal replay

## Terminal verdict

`MP4B_COMPARATOR_REPRESENTATION_CONTRACT_REMEDIATION_AND_DURABLE_TERMINAL_REPLAY_PASS`

Comparator-gate PASS only: it does **not** establish `MP4B_CORRECTED_CALENDAR2009_MATLAB_PYTHON_STATIONARY_PARITY_ACCEPTED`.

## Live continuity and immutable identities

- Live authority: `fb2c826b97f54dee589a89704a6d4e394ed5b14e`; required direct parent `00c60ebef99bc7143a7e8d41dc163df1e1f7b44c` confirmed after fresh fetch.
- Predecessor helper SHA/blob: `A6F7D2BBF7EE0936A6A0A45880B41D7AC77DB5AA7C3CA4B0F207F2D2A2DC08CF` / `03db092e2d5885364ab9698c2a07c6d5fa17a0cb`.
- Corrected entry-test blob: `89ff42fb99f24ed89ff162e69f2d6c3e01a052eb`.

| Immutable object | SHA-256 |
| --- | --- |
| economics.py | F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1 |
| matlab_faithful_policy.py | ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC |
| MATLAB-faithful export | B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3 |
| MP2 one-turn | D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D |
| MP3 steady-state | 7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C |
| stationary runtime | 226BE912AB776F57A8D8EFACE912AB2A3331E865638AC36976F6D578BDB086A0 |
| source semantics map | 6A4FD1576100D7CE36787EAA7E6B833ACED2D94B89B929EC6ADD45559995C028 |
| source-postloop adapter | 8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06 |
| validation driver | 9033218710204CA4EA2AF0351376E47BB5B4F203923E6155DC4776ADD336091E |
| canonical 2009 input | 507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48 |
| comparator contract | E74E5BF8506AF841BEDB07004C9DCD71E64E1F6143DC8B5C01F9FF734C6C3C3A |
| field map | A1D0F04D9FC77975D7E11EDBA44EF91FD860D5344D72688B68494FD9316024CB |
| MATLAB output | 6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B |
| MATLAB profile | 040C38E9E5FEE374202840C7741B7A15D6CFAE668FF8302619225FEEEC5DC90C |
| MATLAB terminal | 04D143B7553D1041B810B875575C06AE3E2F82132B2D55FEFDF5C3ED8AAB7270 |
| Python manifest | 030A4241D4FB7A8CFA5370811FC4502028A61E46521F9329D7768B45278F6774 |
| Python terminal | CE943372D0F313A33E1D326747683F47CC3065B502A8B2646B492FF3B64A8F01 |
| Python turn-184 household output | 70442A793408DCDE20C84F83CA4795FA3EB95865052714F9FE9A31ABFC350442 |
| accepted diagnostic JSON | D4AF68622ECF3526784BC4C86AE1D1A08604A4D7F06D145A4D36DE013F0B941B |


## Exact remediation contract and helper diff

For **raw MATLAB name only**, remove one final `省` or `市`; otherwise preserve the raw string. Python names are untouched. No whitespace stripping, Unicode normalization, fuzzy/pinyin/substring matching, translation, autonomous-region mapping, or reordering is implemented.

- New helper SHA-256: `0FD6889E10E502F32C10B3373702445333B452B25A11A63A3899184A67853EF3`; working-tree Git blob before commit: `cbe7ce4e4855c139cc7bb3b20b56d124c4add266`.
- Per aligned row, the evidence preserves `raw_matlab_province`, `raw_python_province`, and `comparison_key`.
- Fail closed before numerical comparison unless both lists have 31 names, raw MATLAB/projected MATLAB/Python names are unique, exactly 25 keys change, and projected MATLAB keys equal Python raw names position-by-position.
- Focused-test marker: `MP4B_COMPARATOR_PROVINCE_NAME_REPRESENTATION_CONTRACT_REMEDIATED`.

Exact helper diff:
```diff
diff --git a/validators/multi_province/mp4b_compare_preserved_matlab_python_final_state.py b/validators/multi_province/mp4b_compare_preserved_matlab_python_final_state.py
index 03db092..cbe7ce4 100644
--- a/validators/multi_province/mp4b_compare_preserved_matlab_python_final_state.py
+++ b/validators/multi_province/mp4b_compare_preserved_matlab_python_final_state.py
@@ -13,6 +13,8 @@ FIELDS = (
     "Ct", "At", "Bt", "Lt", "Lt_supply", "Kt_supply", "rah", "Kt", "Yt",
     "mt", "KNratio", "w", "wjt", "rk", "ra", "GovInv", "rb", "it", "Zt", "Govinc",
 )
+EXPECTED_PROVINCE_COUNT = 31
+EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES = 25


 def _scalar(group, name: str) -> float:
@@ -24,6 +26,21 @@ def _text(dataset) -> str:
     return "".join(chr(int(value)) for value in values)


+def project_matlab_province_name(raw_name: str) -> str:
+    """Return the sole accepted MATLAB-to-canonical province-name projection."""
+    return raw_name[:-1] if raw_name.endswith(("省", "市")) else raw_name
+
+
+def _category_counts(states: list[dict[str, object]]) -> dict[str, int]:
+    return {
+        "final_household_converged_count": sum(bool(state["convergent"]) for state in states),
+        "ra_upper_count": sum(state["ra"] == state["ramax"] for state in states),
+        "ra_lower_count": sum(state["ra"] == state["ramin"] for state in states),
+        "wage_upper_count": sum(state["wjt"] == state["wjtmax"] for state in states),
+        "wage_lower_count": sum(state["wjt"] == state["wjtmin"] for state in states),
+    }
+
+
 def load_preserved_matlab_state(path: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
     states: list[dict[str, object]] = []
     with h5py.File(path, "r") as handle:
@@ -32,31 +49,55 @@ def load_preserved_matlab_state(path: Path) -> tuple[list[dict[str, object]], di
         for result_ref, grid_ref in zip(refs, grid_refs, strict=True):
             result = handle[result_ref]
             grid = handle[grid_ref]
-            state = {"name": _text(result["prvname"])}
+            raw_name = _text(result["prvname"])
+            state = {"name": raw_name, "raw_matlab_province": raw_name}
             state.update({field: _scalar(result, field) for field in FIELDS})
             state["convergent"] = bool(_scalar(result, "convergent"))
             state.update({name: _scalar(grid, name) for name in ("ramin", "ramax", "wjtmin", "wjtmax")})
             states.append(state)
-    categories = {
-        "final_household_converged_count": sum(bool(state["convergent"]) for state in states),
-        "ra_upper_count": sum(state["ra"] == state["ramax"] for state in states),
-        "ra_lower_count": sum(state["ra"] == state["ramin"] for state in states),
-        "wage_upper_count": sum(state["wjt"] == state["wjtmax"] for state in states),
-        "wage_lower_count": sum(state["wjt"] == state["wjtmin"] for state in states),
+    return states, _category_counts(states)
+
+
+def validate_province_identity(
+    matlab: list[dict[str, object]], python: list[dict[str, object]],
+) -> tuple[list[str], dict[str, object]]:
+    """Fail closed unless the bounded raw-MATLAB suffix projection aligns exactly."""
+    raw_matlab = [str(state["raw_matlab_province"]) for state in matlab]
+    raw_python = [str(state["name"]) for state in python]
+    if len(raw_matlab) != EXPECTED_PROVINCE_COUNT or len(raw_python) != EXPECTED_PROVINCE_COUNT:
+        raise ValueError("province identity requires exactly 31 MATLAB and Python states")
+    if len(set(raw_matlab)) != EXPECTED_PROVINCE_COUNT:
+        raise ValueError("raw MATLAB province names must be unique")
+    projected = [project_matlab_province_name(name) for name in raw_matlab]
+    if len(set(projected)) != EXPECTED_PROVINCE_COUNT:
+        raise ValueError("projected MATLAB province names must be unique; projection collision")
+    if len(set(raw_python)) != EXPECTED_PROVINCE_COUNT:
+        raise ValueError("Python province names must be unique")
+    changed_indices = [index + 1 for index, (raw, key) in enumerate(zip(raw_matlab, projected, strict=True)) if raw != key]
+    if len(changed_indices) != EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES:
+        raise ValueError("MATLAB suffix projection must change exactly the diagnosed 25 names")
+    if projected != raw_python:
+        raise ValueError("projected MATLAB province sequence must equal Python province sequence exactly")
+    evidence = {
+        "raw_matlab_province_names": raw_matlab,
+        "raw_python_province_names": raw_python,
+        "comparison_keys": projected,
+        "projection_changed_indices_1based": changed_indices,
+        "projection_changed_count": len(changed_indices),
     }
-    return states, categories
+    return projected, evidence


-def compare_terminal(matlab_path: Path, python_terminal_path: Path, output_path: Path) -> dict[str, object]:
-    if output_path.exists():
-        raise FileExistsError(f"refusing to overwrite {output_path}")
-    matlab, matlab_categories = load_preserved_matlab_state(matlab_path)
-    terminal = json.loads(python_terminal_path.read_text(encoding="utf-8"))
-    python = terminal["final_state"]
-    if [state["name"] for state in matlab] != [state["name"] for state in python]:
-        raise ValueError("province order mismatch")
+def build_comparison_payload(
+    matlab: list[dict[str, object]],
+    python: list[dict[str, object]],
+    matlab_outer_turn_count: int | None,
+    python_outer_turn_count: int | None,
+) -> dict[str, object]:
+    """Build aligned evidence only after the bounded representation contract passes."""
+    comparison_keys, identity = validate_province_identity(matlab, python)
     rows = []
-    for matlab_state, python_state in zip(matlab, python, strict=True):
+    for matlab_state, python_state, comparison_key in zip(matlab, python, comparison_keys, strict=True):
         differences = {}
         for field in FIELDS:
             m_value = float(matlab_state[field]); p_value = float(python_state[field])
@@ -67,8 +108,14 @@ def compare_terminal(matlab_path: Path, python_terminal_path: Path, output_path:
                 "relative": absolute / max(abs(m_value), abs(p_value)) if max(abs(m_value), abs(p_value)) else 0.0,
                 "normalized": absolute / scale,
             }
-        rows.append({"province": matlab_state["name"], "continuous": differences,
-                     "convergent_exact": bool(matlab_state["convergent"]) == bool(python_state["convergent"])})
+        rows.append({
+            "province": comparison_key,
+            "raw_matlab_province": matlab_state["raw_matlab_province"],
+            "raw_python_province": python_state["name"],
+            "comparison_key": comparison_key,
+            "continuous": differences,
+            "convergent_exact": bool(matlab_state["convergent"]) == bool(python_state["convergent"]),
+        })
     national = {}
     for field in ("Ct", "At", "Bt", "Yt"):
         m_value = sum(float(state[field]) for state in matlab)
@@ -77,12 +124,47 @@ def compare_terminal(matlab_path: Path, python_terminal_path: Path, output_path:
         national[field] = {"matlab": m_value, "python": p_value, "absolute": absolute,
                            "relative": absolute / max(abs(m_value), abs(p_value)),
                            "normalized": absolute / max(1.0, abs(m_value), abs(p_value))}
-    payload = {"schema": "MP4B_PRESERVED_MATLAB_PYTHON_FINAL_STATE_COMPARISON_V1",
-               "province_rows": rows, "national": national,
-               "matlab_categories": matlab_categories,
-               "python_outer_turn_count": terminal.get("iteration_count")}
+    matlab_categories = _category_counts(matlab)
+    python_categories = _category_counts(python)
+    categories = {"outer_turn_count": {"matlab": matlab_outer_turn_count, "python": python_outer_turn_count}}
+    categories.update({field: {"matlab": matlab_categories[field], "python": python_categories[field]}
+                       for field in matlab_categories})
+    for values in categories.values():
+        values["exact"] = values["matlab"] == values["python"]
+    return {
+        "schema": "MP4B_PRESERVED_MATLAB_PYTHON_FINAL_STATE_COMPARISON_V2",
+        "province_identity": identity,
+        "province_rows": rows,
+        "national": national,
+        "terminal_categories": categories,
+        "matlab_categories": matlab_categories,
+        "python_categories": python_categories,
+    }
+
+
+def compare_terminal(
+    matlab_path: Path,
+    python_terminal_path: Path,
+    output_path: Path,
+    matlab_terminal_status_path: Path | None = None,
+) -> dict[str, object]:
+    if output_path.exists():
+        raise FileExistsError(f"refusing to overwrite {output_path}")
+    matlab, matlab_categories = load_preserved_matlab_state(matlab_path)
+    terminal = json.loads(python_terminal_path.read_text(encoding="utf-8"))
+    matlab_outer_turn_count = None
+    if matlab_terminal_status_path is not None:
+        matlab_status = json.loads(matlab_terminal_status_path.read_text(encoding="utf-8"))
+        matlab_outer_turn_count = int(matlab_status["outer_turn_call_count"])
+    payload = build_comparison_payload(
+        matlab, terminal["final_state"], matlab_outer_turn_count, terminal.get("iteration_count"),
+    )
     output_path.write_text(json.dumps(payload, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
     return payload


-__all__ = ["FIELDS", "load_preserved_matlab_state", "compare_terminal"]
+__all__ = [
+    "EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES", "EXPECTED_PROVINCE_COUNT", "FIELDS",
+    "build_comparison_payload", "compare_terminal", "load_preserved_matlab_state",
+    "project_matlab_province_name", "validate_province_identity",
+]
```

## Focused zero-science preflight and replay ledger

- `python -m pytest tests/test_mp4b_comparator_representation_contract.py tests/test_mp4b_preserved_matlab_python_final_state_field_map.py -q`: `7 passed in 0.59s`.
- `python -m py_compile validators/multi_province/mp4b_compare_preserved_matlab_python_final_state.py tests/test_mp4b_comparator_representation_contract.py tests/test_mp4b_preserved_matlab_python_final_state_field_map.py`: PASS.
- `git diff --check`: PASS before replay.
- Comparator replay ledger: `1/1`; reruns `0`.
- Artifact: `D:\ProjectTemp\ch5-mp4b-final-state-comparator-replay-after-representation-remediation-20260831-001.json`; 106389 bytes; SHA-256 `77916C2376B96D7C94CBF15A2E5DED1BCF366C4430FACCE84746794B468986AB`; schema `MP4B_PRESERVED_MATLAB_PYTHON_FINAL_STATE_COMPARISON_V2`.

## Raw-name and projected identity evidence

The raw MATLAB/Python sequences are both unique length 31. The projection changes exactly 25 raw MATLAB values; projected keys are unique and exactly equal to the Python sequence position-by-position. Six raw MATLAB names are unchanged: `内蒙古、黑龙江、广西、西藏、宁夏、新疆`.

| i | Raw MATLAB | Raw Python | Comparison key |
| --- | --- | --- | --- |
| 1 | 北京市 | 北京 | 北京 |
| 2 | 天津市 | 天津 | 天津 |
| 3 | 河北省 | 河北 | 河北 |
| 4 | 山西省 | 山西 | 山西 |
| 5 | 内蒙古 | 内蒙古 | 内蒙古 |
| 6 | 辽宁省 | 辽宁 | 辽宁 |
| 7 | 吉林省 | 吉林 | 吉林 |
| 8 | 黑龙江 | 黑龙江 | 黑龙江 |
| 9 | 上海市 | 上海 | 上海 |
| 10 | 江苏省 | 江苏 | 江苏 |
| 11 | 浙江省 | 浙江 | 浙江 |
| 12 | 安徽省 | 安徽 | 安徽 |
| 13 | 福建省 | 福建 | 福建 |
| 14 | 江西省 | 江西 | 江西 |
| 15 | 山东省 | 山东 | 山东 |
| 16 | 河南省 | 河南 | 河南 |
| 17 | 湖北省 | 湖北 | 湖北 |
| 18 | 湖南省 | 湖南 | 湖南 |
| 19 | 广东省 | 广东 | 广东 |
| 20 | 广西 | 广西 | 广西 |
| 21 | 海南省 | 海南 | 海南 |
| 22 | 重庆市 | 重庆 | 重庆 |
| 23 | 四川省 | 四川 | 四川 |
| 24 | 贵州省 | 贵州 | 贵州 |
| 25 | 云南省 | 云南 | 云南 |
| 26 | 西藏 | 西藏 | 西藏 |
| 27 | 陕西省 | 陕西 | 陕西 |
| 28 | 甘肃省 | 甘肃 | 甘肃 |
| 29 | 青海省 | 青海 | 青海 |
| 30 | 宁夏 | 宁夏 | 宁夏 |
| 31 | 新疆 | 新疆 | 新疆 |


## Aligned 31-province continuous comparisons

All values are durable-artifact values; no new acceptance tolerance was applied.

### Ct

| Province | MATLAB | Python | Absolute | Relative | Normalized |
| --- | --- | --- | --- | --- | --- |
| 北京 | 9.52054960377584 | 9.285341116476275 | 0.23520848729956612 | 0.024705347599500205 | 0.024705347599500205 |
| 天津 | 9.4416978319382 | 9.20581761339903 | 0.23588021853916885 | 0.024982817999244015 | 0.024982817999244015 |
| 河北 | 9.69708582837359 | 9.45782986875182 | 0.2392559596217705 | 0.0246729753511833 | 0.0246729753511833 |
| 山西 | 9.545907432242398 | 9.310983908211565 | 0.23492352403083316 | 0.02460986822869788 | 0.02460986822869788 |
| 内蒙古 | 9.21801615985227 | 8.993788840358192 | 0.22422731949407826 | 0.024324899805520817 | 0.024324899805520817 |
| 辽宁 | 9.00654513187835 | 8.781769726252207 | 0.22477540562614173 | 0.024956895494872625 | 0.024956895494872625 |
| 吉林 | 8.564134112624199 | 8.349614604024712 | 0.2145195085994871 | 0.025048592861626102 | 0.025048592861626102 |
| 黑龙江 | 7.994625039270321 | 7.797471998731105 | 0.19715304053921656 | 0.024660698853389996 | 0.024660698853389996 |
| 上海 | 9.529671968432282 | 9.290049330269378 | 0.23962263816290452 | 0.025144898896485798 | 0.025144898896485798 |
| 江苏 | 9.812785009992638 | 9.564262095630204 | 0.24852291436243412 | 0.025326440364214255 | 0.025326440364214255 |
| 浙江 | 9.638230553624446 | 9.41995175087786 | 0.2182788027465854 | 0.02264718627886546 | 0.02264718627886546 |
| 安徽 | 9.707287305551827 | 9.465230838690996 | 0.2420564668608307 | 0.024935541644306017 | 0.024935541644306017 |
| 福建 | 9.308068529078355 | 9.076174733007623 | 0.23189379607073235 | 0.02491320249161224 | 0.02491320249161224 |
| 江西 | 9.410113457990121 | 9.178842997620695 | 0.23127046036942644 | 0.024576798292804306 | 0.024576798292804306 |
| 山东 | 9.851851486594065 | 9.604851332471561 | 0.2470001541225031 | 0.02507144514496684 | 0.02507144514496684 |
| 河南 | 9.731097448955921 | 9.493633110223374 | 0.23746433873254702 | 0.024402626731276366 | 0.024402626731276366 |
| 湖北 | 9.650338034990309 | 9.415097739490765 | 0.23524029549954406 | 0.024376378801095572 | 0.024376378801095572 |
| 湖南 | 9.558466376014362 | 9.323904560598034 | 0.2345618154163276 | 0.024539691430513134 | 0.024539691430513134 |
| 广东 | 9.311782276839907 | 9.083745498991613 | 0.22803677784829368 | 0.024489058170471034 | 0.024489058170471034 |
| 广西 | 8.94402449023395 | 8.729931055507116 | 0.21409343472683418 | 0.023937035834439457 | 0.023937035834439457 |
| 海南 | 8.436384473872726 | 8.234850847691106 | 0.20153362618161985 | 0.02388862513387868 | 0.02388862513387868 |
| 重庆 | 9.356556359811833 | 9.131649204806175 | 0.22490715500565805 | 0.024037385802716534 | 0.024037385802716534 |
| 四川 | 9.148467710595202 | 8.938943176931812 | 0.20952453366339086 | 0.02290269149889792 | 0.02290269149889792 |
| 贵州 | 9.092850494956902 | 8.874374129426037 | 0.21847636553086502 | 0.024027269078276046 | 0.024027269078276046 |
| 云南 | 8.638382281882196 | 8.440617549084099 | 0.19776473279809714 | 0.022893723193158647 | 0.022893723193158647 |
| 西藏 | 7.694449621102146 | 7.520506921474679 | 0.17394269962746733 | 0.02260625622272278 | 0.02260625622272278 |
| 陕西 | 9.541353992934837 | 9.311716565304344 | 0.2296374276304931 | 0.024067593320668594 | 0.024067593320668594 |
| 甘肃 | 9.095867862286692 | 8.880004467790986 | 0.21586339449570602 | 0.023732028407175892 | 0.023732028407175892 |
| 青海 | 8.410905300190594 | 8.216736679266035 | 0.19416862092455922 | 0.023085341469741585 | 0.023085341469741585 |
| 宁夏 | 9.147302471936191 | 8.929020389956086 | 0.2182820819801048 | 0.023863000338055013 | 0.023863000338055013 |
| 新疆 | 7.386144510429903 | 7.220494332337593 | 0.1656501780923092 | 0.022427150979566702 | 0.022427150979566702 |


### final firm Lt

| Province | MATLAB | Python | Absolute | Relative | Normalized |
| --- | --- | --- | --- | --- | --- |
| 北京 | 5245516.59882363 | 5202087.0336554395 | 43429.56516819075 | 0.008279368552170886 | 0.008279368552170886 |
| 天津 | 5069129.550773941 | 5120242.570252859 | 51113.01947891805 | 0.009982538674216342 | 0.009982538674216342 |
| 河北 | 5467091.789641744 | 5424870.091634472 | 42221.69800727256 | 0.007722880762175629 | 0.007722880762175629 |
| 山西 | 5055253.379355687 | 5106233.194670611 | 50979.815314924344 | 0.009983840018926694 | 0.009983840018926694 |
| 内蒙古 | 5001345.0813844185 | 5051803.958357905 | 50458.876973486505 | 0.009988288815128175 | 0.009988288815128175 |
| 辽宁 | 5246056.665187666 | 5202806.251427643 | 43250.41376002319 | 0.008244366487123334 | 0.008244366487123334 |
| 吉林 | 4952517.253809975 | 5002450.525800451 | 49933.271990475245 | 0.00998176228489243 | 0.00998176228489243 |
| 黑龙江 | 4831339.759161567 | 4880106.6403788 | 48766.881217232905 | 0.009992994991897873 | 0.009992994991897873 |
| 上海 | 5443986.335851818 | 5431176.277269392 | 12810.058582426049 | 0.002353065895493594 | 0.002353065895493594 |
| 江苏 | 5363531.183763999 | 5417362.608299099 | 53831.42453510035 | 0.009936832445484375 | 0.009936832445484375 |
| 浙江 | 5402660.121677092 | 5457065.7180648865 | 54405.59638779424 | 0.00996975283029702 | 0.00996975283029702 |
| 安徽 | 5218371.900999221 | 5175384.517649788 | 42987.38334943261 | 0.008237700218568424 | 0.008237700218568424 |
| 福建 | 5278567.754898328 | 5234873.556665608 | 43694.198232720606 | 0.008277661718403426 | 0.008277661718403426 |
| 江西 | 5058281.656981965 | 5109303.451441095 | 51021.794459130615 | 0.009986056796986633 | 0.009986056796986633 |
| 山东 | 5385279.578036318 | 5439374.622551247 | 54095.044514928944 | 0.009945085284373479 | 0.009945085284373479 |
| 河南 | 5461236.649930779 | 5516222.569318334 | 54985.91938755475 | 0.009968038580131046 | 0.009968038580131046 |
| 湖北 | 5374221.421341702 | 5329961.176685875 | 44260.24465582706 | 0.00823565707212288 | 0.00823565707212288 |
| 湖南 | 5351980.283594112 | 5307704.226154014 | 44276.057440098375 | 0.008272836425765918 | 0.008272836425765918 |
| 广东 | 5290184.954597753 | 5343186.240834868 | 53001.28623711504 | 0.009919415840693894 | 0.009919415840693894 |
| 广西 | 4971305.750554265 | 5021462.999815087 | 50157.24926082138 | 0.009988572904483892 | 0.009988572904483892 |
| 海南 | 5117342.919972535 | 5168483.510584712 | 51140.590612176806 | 0.009894699384731375 | 0.009894699384731375 |
| 重庆 | 5049637.967179942 | 5100532.724070686 | 50894.75689074397 | 0.009978321803634142 | 0.009978321803634142 |
| 四川 | 5376433.553319225 | 5331962.483437627 | 44471.069881598465 | 0.008271481352939545 | 0.008271481352939545 |
| 贵州 | 5101481.469265012 | 5152784.004780086 | 51302.53551507369 | 0.009956275183955282 | 0.009956275183955282 |
| 云南 | 4970405.937568278 | 5020510.400643594 | 50104.46307531558 | 0.009979954043894132 | 0.009979954043894132 |
| 西藏 | 5049770.552556309 | 5099879.310594013 | 50108.75803770404 | 0.009825479189990396 | 0.009825479189990396 |
| 陕西 | 5042300.679003462 | 5093173.489942642 | 50872.81093917973 | 0.009988430796562685 | 0.009988430796562685 |
| 甘肃 | 5103592.110179095 | 5154861.858312277 | 51269.748133182526 | 0.009945901469795827 | 0.009945901469795827 |
| 青海 | 5119138.880617672 | 5170112.2136926865 | 50973.333075014874 | 0.009859231476642907 | 0.009859231476642907 |
| 宁夏 | 5214364.356257692 | 5266373.80576396 | 52009.449506267905 | 0.009875761088083876 | 0.009875761088083876 |
| 新疆 | 4786747.83861888 | 4834900.476702667 | 48152.638083786704 | 0.00995938557904425 | 0.00995938557904425 |


### Yt

| Province | MATLAB | Python | Absolute | Relative | Normalized |
| --- | --- | --- | --- | --- | --- |
| 北京 | 11920452.462887645 | 11918923.486233236 | 1528.9766544084996 | 0.0001282649848375064 | 0.0001282649848375064 |
| 天津 | 5711724.111329895 | 5711495.239191448 | 228.87213844712824 | 4.007058709175618e-05 | 4.007058709175618e-05 |
| 河北 | 15383457.75422399 | 15386343.787150003 | 2886.032926013693 | 0.0001875710673008607 | 0.0001875710673008607 |
| 山西 | 7146797.988876601 | 7147659.557199009 | 861.568322408013 | 0.00012053852250702891 | 0.00012053852250702891 |
| 内蒙古 | 7106231.338840198 | 7105963.810896938 | 267.5279432600364 | 3.7646951035469586e-05 | 3.7646951035469586e-05 |
| 辽宁 | 12880921.11107135 | 12882062.894322151 | 1141.7832508012652 | 8.863357213575733e-05 | 8.863357213575733e-05 |
| 吉林 | 5431349.196605436 | 5431372.351524669 | 23.154919233173132 | 4.263180230439033e-06 | 4.263180230439033e-06 |
| 黑龙江 | 7220792.946829608 | 7220514.578363423 | 278.3684661844745 | 3.8550955308405036e-05 | 3.8550955308405036e-05 |
| 上海 | 15770664.246868992 | 15811951.31081367 | 41287.06394467689 | 0.0026111302225197844 | 0.0026111302225197844 |
| 江苏 | 34034736.64277293 | 34030239.88315776 | 4496.759615167975 | 0.00013212265052513152 | 0.00013212265052513152 |
| 浙江 | 22834962.953403708 | 22827717.998625685 | 7244.954778023064 | 0.0003172746455865458 | 0.0003172746455865458 |
| 安徽 | 10918206.22310443 | 10919986.387860114 | 1780.1647556833923 | 0.00016301895372895556 | 0.00016301895372895556 |
| 福建 | 12471165.980792886 | 12469754.9723648 | 1411.0084280855954 | 0.00011314166055192595 | 0.00011314166055192595 |
| 江西 | 7589441.455665976 | 7590092.082785329 | 650.627119353041 | 8.572058313082824e-05 | 8.572058313082824e-05 |
| 山东 | 29542440.622275863 | 29541701.656378455 | 738.9658974073827 | 2.501370509145344e-05 | 2.501370509145344e-05 |
| 河南 | 19173739.107832376 | 19176305.346718814 | 2566.23888643831 | 0.00013382342636077235 | 0.00013382342636077235 |
| 湖北 | 13256701.039564902 | 13258891.364788065 | 2190.3252231627703 | 0.00016519670935532862 | 0.00016519670935532862 |
| 湖南 | 13113676.857655993 | 13112642.633379934 | 1034.2242760583758 | 7.88660790779344e-05 | 7.88660790779344e-05 |
| 广东 | 39889124.297758244 | 39884789.86100775 | 4334.436750493944 | 0.0001086621184796864 | 0.0001086621184796864 |
| 广西 | 7781191.352971271 | 7780052.664914763 | 1138.6880565080792 | 0.00014633852386540628 | 0.00014633852386540628 |
| 海南 | 1621735.2590400996 | 1621445.5768078559 | 289.6822322437074 | 0.00017862485916176571 | 0.00017862485916176571 |
| 重庆 | 6577619.166280433 | 6578166.550799795 | 547.3845193628222 | 8.32123229376534e-05 | 8.32123229376534e-05 |
| 四川 | 14265583.695621738 | 14264654.910922108 | 928.7846996299922 | 6.510667347702333e-05 | 6.510667347702333e-05 |
| 贵州 | 3855651.3801904293 | 3855092.0704196016 | 559.3097708276473 | 0.00014506232946818527 | 0.00014506232946818527 |
| 云南 | 6576482.925978097 | 6576224.136241265 | 258.78973683249205 | 3.935078061409293e-05 | 3.935078061409293e-05 |
| 西藏 | 441366.520675643 | 441366.30009408545 | 0.22058155754348263 | 4.997695729295843e-07 | 4.997695729295843e-07 |
| 陕西 | 8171710.929955554 | 8171410.6483693365 | 300.281586217694 | 3.6746476813923126e-05 | 3.6746476813923126e-05 |
| 甘肃 | 3384907.4725338304 | 3384731.236209968 | 176.23632386233658 | 5.206532978888544e-05 | 5.206532978888544e-05 |
| 青海 | 942227.5971618161 | 942081.255596048 | 146.34156576811802 | 0.00015531445503074736 | 0.00015531445503074736 |
| 宁夏 | 1266888.5109196573 | 1266902.2464750381 | 13.73555538081564 | 1.0841843101180635e-05 | 1.0841843101180635e-05 |
| 新疆 | 4274750.744913655 | 4275075.80395454 | 325.05904088448733 | 7.603585428445515e-05 | 7.603585428445515e-05 |


### At

| Province | MATLAB | Python | Absolute | Relative | Normalized |
| --- | --- | --- | --- | --- | --- |
| 北京 | 0.12674265225445688 | 0.1246508509738043 | 0.0020918012806525887 | 0.016504319922648857 | 0.0020918012806525887 |
| 天津 | 0.2147874672267574 | 0.21105881000167867 | 0.0037286572250787298 | 0.01735975228546402 | 0.0037286572250787298 |
| 河北 | 0.6107342169549475 | 0.6149781099874962 | 0.004243893032548796 | 0.00690088470406708 | 0.004243893032548796 |
| 山西 | 1.2008178976114716 | 1.2145622887740566 | 0.013744391162584968 | 0.011316332879442644 | 0.011316332879442644 |
| 内蒙古 | 0.727873506378218 | 0.7234326377253429 | 0.004440868652875074 | 0.00610115440933154 | 0.004440868652875074 |
| 辽宁 | 0.5926035621941346 | 0.5871325162985219 | 0.005471045895612647 | 0.009232219049369052 | 0.005471045895612647 |
| 吉林 | 0.6156753278970996 | 0.6121660612611532 | 0.0035092666359463065 | 0.005699865622246967 | 0.0035092666359463065 |
| 黑龙江 | 2.4460272494480173 | 2.4245718962822966 | 0.02145535316572067 | 0.008771510280828797 | 0.008771510280828797 |
| 上海 | 0.14704564718281654 | 0.147223556890505 | 0.00017790970768846726 | 0.0012084323422561006 | 0.00017790970768846726 |
| 江苏 | 0.35863698806153027 | 0.35516733588279475 | 0.003469652178735516 | 0.00967455196824327 | 0.003469652178735516 |
| 浙江 | 0.6940758838729817 | 0.19402482111116182 | 0.5000510627618199 | 0.7204558959338961 | 0.5000510627618199 |
| 安徽 | 0.8420758349159279 | 0.8542261404456726 | 0.01215030552974472 | 0.014223757567762538 | 0.01215030552974472 |
| 福建 | 1.3108792729937702 | 1.3077648943072806 | 0.0031143786864895606 | 0.0023757936757799066 | 0.0023757936757799066 |
| 江西 | 3.6761945465142754 | 3.6072291634721574 | 0.06896538304211797 | 0.01875999275052245 | 0.01875999275052245 |
| 山东 | 0.5568620058452782 | 0.5539122665731809 | 0.002949739272097296 | 0.005297074034741865 | 0.002949739272097296 |
| 河南 | 3.3877607321548053 | 3.3297233011039147 | 0.05803743105089065 | 0.01713150238150839 | 0.01713150238150839 |
| 湖北 | 3.047586335868181 | 2.9875491266662544 | 0.06003720920192679 | 0.01969992071933335 | 0.01969992071933335 |
| 湖南 | 2.4255914420415197 | 2.414829026218624 | 0.010762415822895832 | 0.004437027454977147 | 0.004437027454977147 |
| 广东 | 1.7961154679226825 | 1.772501936717696 | 0.02361353120498655 | 0.013147000639272398 | 0.013147000639272398 |
| 广西 | 1.2543274676049656 | 1.2665218880986933 | 0.012194420493727653 | 0.009628274574894206 | 0.009628274574894206 |
| 海南 | 2.3334375386937958 | 2.3379599657254477 | 0.004522427031651954 | 0.001934347507207501 | 0.001934347507207501 |
| 重庆 | 1.1730317516517317 | 1.1733308669023463 | 0.0002991152506146566 | 0.00025492830628783865 | 0.00025492830628783865 |
| 四川 | 5.036636905458005 | 4.96196683934634 | 0.07467006611166482 | 0.014825381998600656 | 0.014825381998600656 |
| 贵州 | 1.693065089242799 | 1.7193720768944138 | 0.026306987651614877 | 0.015300345983942825 | 0.015300345983942825 |
| 云南 | 4.540755059590419 | 4.478903247819849 | 0.06185181177056975 | 0.013621481660838331 | 0.013621481660838331 |
| 西藏 | 1.4016656004015544 | 1.4074677986690296 | 0.005802198267475189 | 0.00412243766639779 | 0.00412243766639779 |
| 陕西 | 2.220184183973872 | 2.1833075669525637 | 0.03687661702130818 | 0.016609710711164204 | 0.016609710711164204 |
| 甘肃 | 1.5490211610877653 | 1.5695736816177028 | 0.0205525205299375 | 0.01309433304765582 | 0.01309433304765582 |
| 青海 | 0.6452834111187559 | 0.6500015153552154 | 0.004718104236459575 | 0.007258604980145633 | 0.004718104236459575 |
| 宁夏 | 0.6481548150519226 | 0.6494605958236941 | 0.0013057807717714587 | 0.0020105619650648255 | 0.0013057807717714587 |
| 新疆 | 0.6818834668571488 | 0.6795838941842924 | 0.002299572672856409 | 0.0033723836764298 | 0.002299572672856409 |


### Bt

| Province | MATLAB | Python | Absolute | Relative | Normalized |
| --- | --- | --- | --- | --- | --- |
| 北京 | 2.08732379818565 | 2.085604269856615 | 0.0017195283290352137 | 0.0008237956806365487 | 0.0008237956806365487 |
| 天津 | 2.1282491873986866 | 2.1269172229241944 | 0.001331964474492242 | 0.0006258498686990097 | 0.0006258498686990097 |
| 河北 | 2.1727310579237624 | 2.172254474168171 | 0.00047658375559134214 | 0.0002193477898947881 | 0.0002193477898947881 |
| 山西 | 2.1608502163536 | 2.1581281721356076 | 0.00272204421799227 | 0.0012597098111620509 | 0.0012597098111620509 |
| 内蒙古 | 2.171923812965865 | 2.171009947059365 | 0.0009138659064999999 | 0.000420763334811488 | 0.000420763334811488 |
| 辽宁 | 2.1704627447896074 | 2.169422734813699 | 0.0010400099759082515 | 0.0004791650897509712 | 0.0004791650897509712 |
| 吉林 | 2.168733000631694 | 2.1673554953755243 | 0.0013775052561695311 | 0.0006351659036720061 | 0.0006351659036720061 |
| 黑龙江 | 2.0581672491426213 | 2.056904723569498 | 0.001262525573123341 | 0.000613422244304624 | 0.000613422244304624 |
| 上海 | 2.0999327350782186 | 2.099836479500418 | 9.625557780079674e-05 | 4.5837457644666603e-05 | 4.5837457644666603e-05 |
| 江苏 | 2.156876970451195 | 2.156354962200631 | 0.0005220082505639212 | 0.0002420204108603945 | 0.0002420204108603945 |
| 浙江 | 2.1734148787023453 | 2.121239273246378 | 0.05217560545596722 | 0.024006279687897914 | 0.024006279687897914 |
| 安徽 | 2.1725515057026232 | 2.171251100526803 | 0.0013004051758200852 | 0.0005985612642124782 | 0.0005985612642124782 |
| 福建 | 2.1536909312374046 | 2.151515551522666 | 0.002175379714738579 | 0.0010100705180983015 | 0.0010100705180983015 |
| 江西 | 1.9591218106468116 | 1.9641098689288086 | 0.004988058281996999 | 0.002539602473825662 | 0.002539602473825662 |
| 山东 | 2.1715591648726353 | 2.1710787105440272 | 0.0004804543286081042 | 0.0002212485555908321 | 0.0002212485555908321 |
| 河南 | 1.9900888977561109 | 1.993856910046604 | 0.0037680122904930613 | 0.0018898107840672421 | 0.0018898107840672421 |
| 湖北 | 2.022354187227827 | 2.026252114700889 | 0.0038979274730621682 | 0.0019237129697641656 | 0.0019237129697641656 |
| 湖南 | 2.0782030664794515 | 2.0769981053444857 | 0.0012049611349658207 | 0.0005798091410802636 | 0.0005798091410802636 |
| 广东 | 2.1258216705852666 | 2.1246012342780185 | 0.0012204363072481073 | 0.0005741009813453003 | 0.0005741009813453003 |
| 广西 | 2.1529572009166467 | 2.1503824179444715 | 0.0025747829721751714 | 0.0011959285447378737 | 0.0011959285447378737 |
| 海南 | 2.073450564086048 | 2.070595015877244 | 0.0028555482088039597 | 0.0013771961860410457 | 0.0013771961860410457 |
| 重庆 | 2.16030596194175 | 2.1584141846200575 | 0.0018917773216924338 | 0.0008756987922173976 | 0.0008756987922173976 |
| 四川 | 1.8154710755698784 | 1.8227660623787374 | 0.007294986808858983 | 0.004002151981773741 | 0.004002151981773741 |
| 贵州 | 2.130005146572282 | 2.1256188502532836 | 0.0043862963189984505 | 0.0020592890707598114 | 0.0020592890707598114 |
| 云南 | 1.8659579592432765 | 1.870805659109139 | 0.0048476998658626425 | 0.0025912364773212596 | 0.0025912364773212596 |
| 西藏 | 2.1313716215022698 | 2.128657061700609 | 0.0027145598016606876 | 0.0012736210683650584 | 0.0012736210683650584 |
| 陕西 | 2.0954990039913985 | 2.096102063319628 | 0.0006030593282293495 | 0.00028770513553823593 | 0.00028770513553823593 |
| 甘肃 | 2.1387811425530616 | 2.1348246824912116 | 0.00395646006185002 | 0.0018498667222805211 | 0.0018498667222805211 |
| 青海 | 2.1680127367072632 | 2.1666441696200955 | 0.0013685670871677047 | 0.0006312541730018886 | 0.0006312541730018886 |
| 宁夏 | 2.171673986719063 | 2.1708202304991726 | 0.000853756219890478 | 0.0003931327745838692 | 0.0003931327745838692 |
| 新疆 | 2.157623938370497 | 2.155062394153609 | 0.0025615442168880342 | 0.0011872060609517477 | 0.0011872060609517477 |


## Frozen-field summaries

| Field | Max abs | Province | Max rel | Province | Max norm | Province | Median norm | Exact count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ct | 0.24852291436243412 | 江苏 | 0.025326440364214255 | 江苏 | 0.025326440364214255 | 江苏 | 0.024402626731276366 | 0 |
| At | 0.5000510627618199 | 浙江 | 0.7204558959338961 | 浙江 | 0.5000510627618199 | 浙江 | 0.004718104236459575 | 0 |
| Bt | 0.05217560545596722 | 浙江 | 0.024006279687897914 | 浙江 | 0.024006279687897914 | 浙江 | 0.0008237956806365487 | 0 |
| Lt | 54985.91938755475 | 河南 | 0.009992994991897873 | 黑龙江 | 0.009992994991897873 | 黑龙江 | 0.009945085284373479 | 0 |
| Lt_supply | 54985.91938755475 | 河南 | 0.009992994991897873 | 黑龙江 | 0.009992994991897873 | 黑龙江 | 0.009945085284373479 | 0 |
| Kt_supply | 2289.791506876747 | 安徽 | 0.0486221644809797 | 四川 | 0.0486221644809797 | 四川 | 0.04506913457533 | 0 |
| rah | 0.006218239813147744 | 浙江 | 0.14708135558884142 | 浙江 | 0.006218239813147744 | 浙江 | 3.620846050116089e-05 | 0 |
| Kt | 17993733.576112688 | 浙江 | 0.09996998709057899 | 浙江 | 0.09996998709057899 | 浙江 | 4.075543970665044e-05 | 0 |
| Yt | 41287.06394467689 | 上海 | 0.0026111302225197844 | 上海 | 0.0026111302225197844 | 上海 | 8.863357213575733e-05 | 0 |
| mt | 0.09494484317040897 | 浙江 | 0.09424453704982749 | 浙江 | 0.09424453704982749 | 浙江 | 0.09284204876008088 | 0 |
| KNratio | 2.9983866977268647 | 浙江 | 0.09090655009538795 | 浙江 | 0.09090655009538795 | 浙江 | 0.010025985933747983 | 0 |
| w | 0.4277915497414142 | 江苏 | 0.02990369463805356 | 浙江 | 0.02990369463805356 | 浙江 | 0.029024881824895175 | 0 |
| wjt | 0.1077389255455592 | 河北 | 0.08538747550044494 | 北京 | 0.08538747550044494 | 北京 | 0.0 | 22 |
| rk | 0.014175948309403281 | 浙江 | 0.1850515435322308 | 浙江 | 0.014175948309403281 | 浙江 | 0.006709312709141338 | 0 |
| ra | 0.007754002275032416 | 浙江 | 0.15025562495982533 | 浙江 | 0.007754002275032416 | 浙江 | 3.711192050429024e-05 | 0 |
| GovInv | 17994268.70931992 | 浙江 | 0.09999999999999996 | 浙江 | 0.09999999999999996 | 浙江 | 0.0 | 30 |
| rb | 0.0 | 北京 | 0.0 | 北京 | 0.0 | 北京 | 0.0 | 31 |
| it | 0.0 | 北京 | 0.0 | 北京 | 0.0 | 北京 | 0.0 | 31 |
| Zt | 0.04041836820332256 | 浙江 | 0.05988289974196975 | 浙江 | 0.04041836820332256 | 浙江 | 0.0018771855603149645 | 0 |
| Govinc | 1155905.452839028 | 广东 | 0.570687084741256 | 新疆 | 0.570687084741256 | 新疆 | 0.0488677211251967 | 0 |


## Top-five normalized differences

| Field | Rank | Province | Normalized difference |
| --- | --- | --- | --- |
| Ct | 1 | 江苏 | 0.025326440364214255 |
| Ct | 2 | 上海 | 0.025144898896485798 |
| Ct | 3 | 山东 | 0.02507144514496684 |
| Ct | 4 | 吉林 | 0.025048592861626102 |
| Ct | 5 | 天津 | 0.024982817999244015 |
| Lt | 1 | 黑龙江 | 0.009992994991897873 |
| Lt | 2 | 广西 | 0.009988572904483892 |
| Lt | 3 | 陕西 | 0.009988430796562685 |
| Lt | 4 | 内蒙古 | 0.009988288815128175 |
| Lt | 5 | 江西 | 0.009986056796986633 |
| Yt | 1 | 上海 | 0.0026111302225197844 |
| Yt | 2 | 浙江 | 0.0003172746455865458 |
| Yt | 3 | 河北 | 0.0001875710673008607 |
| Yt | 4 | 海南 | 0.00017862485916176571 |
| Yt | 5 | 湖北 | 0.00016519670935532862 |
| At | 1 | 浙江 | 0.5000510627618199 |
| At | 2 | 湖北 | 0.01969992071933335 |
| At | 3 | 江西 | 0.01875999275052245 |
| At | 4 | 河南 | 0.01713150238150839 |
| At | 5 | 陕西 | 0.016609710711164204 |
| Bt | 1 | 浙江 | 0.024006279687897914 |
| Bt | 2 | 四川 | 0.004002151981773741 |
| Bt | 3 | 云南 | 0.0025912364773212596 |
| Bt | 4 | 江西 | 0.002539602473825662 |
| Bt | 5 | 贵州 | 0.0020592890707598114 |


## National values and exact terminal categories

| National | MATLAB | Python | Absolute | Relative | Normalized |
| --- | --- | --- | --- | --- | --- |
| Ct | 283.3909431582526 | 276.52720698365306 | 6.863736174599524 | 0.02422002657567868 | 0.02422002657567868 |
| At | 47.95553248807161 | 47.11415467808319 | 0.8413778099884226 | 0.017544958137993893 | 0.017544958137993893 |
| Bt | 65.2831672243048 | 65.21538414270965 | 0.06778308159515234 | 0.0010382933990052618 | 0.0010382933990052618 |
| Yt | 350556701.89460325 | 350585612.6035657 | 28910.70896244049 | 8.246404850370191e-05 | 8.246404850370191e-05 |


| Category | MATLAB | Python | Exact |
| --- | --- | --- | --- |
| outer_turn_count | 184 | 184 | True |
| final_household_converged_count | 31 | 31 | True |
| ra_upper_count | 0 | 0 | True |
| ra_lower_count | 0 | 0 | True |
| wage_upper_count | 7 | 5 | False |
| wage_lower_count | 17 | 17 | True |


`MP4B_FINAL_WAGE_BOUNDARY_CATEGORY_MISMATCH_CONFIRMED_ORDER_INVARIANT` is preserved: wage upper `7` MATLAB versus `5` Python; wage lower is `17/17`.

## Scientific disposition, audit, and closeout

- Repaired defect: the read-only comparator representation gate only; raw persistent MATLAB administrative suffixes remain visible.
- Exact categorical mismatch: wage upper `7` versus `5` is retained.
- Continuous differences are reported above for every frozen field and national sum, without a post-hoc tolerance.
- First visible material divergence is wage-upper category count. This gate does not attribute a cause to MATLAB or Python and does not locate an update layer.
- Zero-science ledger: Python stationary/adapter/HJB/KFE/aggregation/MP2/MP3, MATLAB stationary/household/HJB/KFE/presolver, Shanxi, other years/batches, shocks/AR1/transition/dynamics/IRF, R5, and Results are all `0`; only the permitted comparator replay is `1`.
- Changed paths: helper, focused comparator-representation test, and this report. No scientific source, driver, adapter, contract, field map, canonical data, protected MATLAB, or project rule changed.
- Forbidden-operation audit: PASS. No artifact was overwritten. Commit/push/GitHub read-back and final branch status are captured in execution closeout.

Recommended next gate: one read-only final-state first-divergence localization gate using this aligned evidence, without any stationary rerun.
