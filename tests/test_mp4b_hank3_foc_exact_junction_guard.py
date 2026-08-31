from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SMOKE = ROOT / "validators/multi_province/matlab/mp4b_raw_vb_hank3_foc_path_equivalence_smoke.m"
EDGE = ROOT / "validators/multi_province/matlab/mp4b_raw_vb_hank3_foc_edge_diagnostic.m"
LOGICAL = r"c:\matlabprogram\2023年12月2日 多省份神经网络hank"
PHYSICAL = r"d:\matlabprogram\2023年12月2日 多省份神经网络hank"
PROTECTED_SHA = "772b7b7bbf528fdd246bd152b3e3026035012fe50f30da808c1ee18c0f8463d"


def normalize(value: str) -> str:
    return value.replace("/", "\\").rstrip("\\").lower()


def junction_evidence_valid(link_type: str, targets: list[str]) -> bool:
    return link_type == "Junction" and len(targets) == 1 and normalize(targets[0]) == r"d:\matlabprogram"


def guard_contract(logical: str, physical: str, parent: str, sha: str, link_type="Junction", targets=None) -> bool:
    targets = [r"D:\MatlabProgram"] if targets is None else targets
    allowed = {LOGICAL, PHYSICAL}
    return (
        normalize(logical) == LOGICAL
        and normalize(physical) == PHYSICAL
        and normalize(parent) in allowed
        and sha.lower() == PROTECTED_SHA
        and junction_evidence_valid(link_type, targets)
    )


def test_exact_pair_accepts_and_wrong_argument_placement_rejects():
    assert guard_contract(LOGICAL, PHYSICAL, PHYSICAL, PROTECTED_SHA)
    assert not guard_contract(PHYSICAL, PHYSICAL, PHYSICAL, PROTECTED_SHA)
    assert not guard_contract(LOGICAL, LOGICAL, PHYSICAL, PROTECTED_SHA)


def test_sibling_other_d_root_and_wrong_sha_reject():
    assert not guard_contract(LOGICAL, PHYSICAL, PHYSICAL + "-sibling", PROTECTED_SHA)
    assert not guard_contract(LOGICAL, PHYSICAL, r"D:\MatlabProgram\other-model", PROTECTED_SHA)
    assert not guard_contract(LOGICAL, PHYSICAL, PHYSICAL, "0" * 64)


def test_invalid_junction_target_evidence_rejects():
    assert not guard_contract(LOGICAL, PHYSICAL, PHYSICAL, PROTECTED_SHA, targets=[r"D:\MatlabProgram", r"E:\MatlabProgram"])
    assert not guard_contract(LOGICAL, PHYSICAL, PHYSICAL, PROTECTED_SHA, targets=[r"E:\MatlabProgram"])
    assert not guard_contract(LOGICAL, PHYSICAL, PHYSICAL, PROTECTED_SHA, link_type="SymbolicLink")


def test_active_helpers_have_no_java_canonical_root_authority():
    for path in (SMOKE, EDGE):
        text = path.read_text(encoding="utf-8")
        assert "getCanonicalPath" not in text
        assert "canonical_root" not in text
        assert "startsWith" not in text
        assert "contains(" not in text
        assert "verify_exact_junction" in text
        assert "file_sha256" in text
        assert "other-model" in text


def test_edge_frozen_ten_case_call_expression_unchanged():
    text = EDGE.read_text(encoding="utf-8")
    for case_id in (
        "localized_BB", "localized_BF", "localized_FB", "localized_FF",
        "positive_pb", "negative_pb", "zero_pb_positive_pa",
        "zero_pb_negative_pa", "zero_pa_zero_pb", "zero_a_negative_pb",
    ):
        assert case_id in text
    assert "value = HANK3_FOC(dummy,chi,pa(k),pb(k),a(k),0);" in text
