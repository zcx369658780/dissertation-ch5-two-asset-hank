"""R2 source-only regression: parse bytes/AST; never import model modules."""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TASK = "CH5_TEMP31_HA_TAXFREE_HJB_POLICY_CALL_BINDING_REPAIR_R2_20261029"
REPORT = ROOT / "tasks" / TASK
HJB = "src/ch5_two_asset_hank/temp31_netwage_hjb.py"
POLICY = "src/ch5_two_asset_hank/temp31_netwage_policy.py"
ECONOMICS = "src/ch5_two_asset_hank/temp31_netwage_economics.py"
OLD = "select_matlab_faithful_local_policy"
NEW = "select_temp31_netwage_local_policy"
BEFORE_SHA256 = "f4e5b006afd333ce87667219b24001a18d3e3253245793d8462d96ce02a2bb50"


def parsed(raw: bytes) -> ast.Module:
    return ast.parse(raw.decode("utf-8"))


def policy_call(tree: ast.Module) -> ast.Call:
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)
             and isinstance(n.func, ast.Name) and n.func.id in (OLD, NEW)]
    assert len(calls) == 1, "expected exactly one real HJB policy call"
    return calls[0]


def assert_call_binding(hjb: bytes, policy: bytes) -> None:
    tree = parsed(hjb)
    call = policy_call(tree)
    imports = {a.asname or a.name: a.name
               for n in tree.body if isinstance(n, ast.ImportFrom)
               and n.level == 1 and n.module == "temp31_netwage_policy"
               for a in n.names}
    definitions = {n.name for n in parsed(policy).body if isinstance(n, ast.FunctionDef)}
    assert call.func.id in imports, (
        f"UNBOUND_HJB_POLICY_CALL line={call.lineno} symbol={call.func.id}; "
        f"imported={sorted(imports)}")
    assert call.func.id == NEW and imports[NEW] == NEW, "wrong policy binding"
    assert NEW in definitions, "imported policy has no real function definition"


class OldSourceCounterexample(unittest.TestCase):
    def test_actual_hjb_call_binding(self) -> None:
        assert_call_binding((ROOT / HJB).read_bytes(), (ROOT / POLICY).read_bytes())


class RepairedBinding(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.before = (REPORT / "evidence/hjb_before.py").read_bytes()
        cls.after = (ROOT / HJB).read_bytes()
        cls.policy = (ROOT / POLICY).read_bytes()

    def test_actual_import_call_definition_binding(self) -> None:
        assert_call_binding(self.after, self.policy)
        call = policy_call(parsed(self.after))
        self.assertEqual(call.lineno, 105)
        self.assertFalse(any(isinstance(n, ast.Name) and n.id == OLD
                             for n in ast.walk(parsed(self.after))))

    def test_old_call_mutant_is_rejected(self) -> None:
        call = policy_call(parsed(self.after))
        tree = parsed(self.after)
        policy_call(tree).func.id = OLD
        with self.assertRaisesRegex(AssertionError, "UNBOUND_HJB_POLICY_CALL.*" + OLD):
            assert_call_binding(ast.unparse(tree).encode(), self.policy)
        self.assertEqual(call.func.id, NEW)

    def test_exact_one_symbol_byte_change(self) -> None:
        self.assertEqual(hashlib.sha256(self.before).hexdigest(), BEFORE_SHA256)
        self.assertEqual(self.before.count(OLD.encode()), 1)
        self.assertEqual(self.after, self.before.replace(OLD.encode(), NEW.encode(), 1))

    def test_remaining_hjb_ast_and_call_arguments_unchanged(self) -> None:
        old_tree, new_tree = parsed(self.before), parsed(self.after)
        old_call, new_call = policy_call(old_tree), policy_call(new_tree)
        self.assertEqual(ast.dump(ast.Tuple(elts=old_call.args, ctx=ast.Load())),
                         ast.dump(ast.Tuple(elts=new_call.args, ctx=ast.Load())))
        self.assertEqual([ast.dump(k) for k in old_call.keywords],
                         [ast.dump(k) for k in new_call.keywords])
        restored = copy.deepcopy(new_tree)
        policy_call(restored).func.id = OLD
        self.assertEqual(ast.dump(old_tree), ast.dump(restored))

    def test_policy_keyword_signature_matches_real_call(self) -> None:
        definition = next(n for n in parsed(self.policy).body
                          if isinstance(n, ast.FunctionDef) and n.name == NEW)
        self.assertEqual(definition.args.args, [])
        self.assertIsNone(definition.args.vararg)
        self.assertIsNone(definition.args.kwarg)
        call = policy_call(parsed(self.after))
        self.assertEqual(call.args, [])
        self.assertEqual([k.arg for k in call.keywords],
                         [a.arg for a in definition.args.kwonlyargs])

    def test_policy_to_economics_real_call_bindings(self) -> None:
        tree = parsed(self.policy)
        imports = {a.asname or a.name: a.name for n in tree.body
                   if isinstance(n, ast.ImportFrom) and n.level == 1
                   and n.module == "temp31_netwage_economics" for a in n.names}
        expected = {"asset_drifts_matlab_faithful", "consumption_from_vb", "flow_utility",
                    "labor_from_vb", "matlab_faithful_illiquid_return",
                    "transfer_candidate_matlab_faithful_raw_vb"}
        self.assertEqual(set(imports), expected)
        definitions = {n.name for n in parsed((ROOT / ECONOMICS).read_bytes()).body
                       if isinstance(n, ast.FunctionDef)}
        calls = {n.func.id for n in ast.walk(tree)
                 if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
        for name in expected:
            self.assertEqual(imports[name], name)
            self.assertIn(name, definitions)
            self.assertIn(name, calls)

    def test_no_added_tax_or_migration_wedge(self) -> None:
        def names(raw: bytes) -> list[str]:
            return sorted(n.id if isinstance(n, ast.Name) else n.attr
                          for n in ast.walk(parsed(raw))
                          if isinstance(n, (ast.Name, ast.Attribute))
                          and any(s in (n.id if isinstance(n, ast.Name) else n.attr).lower()
                                  for s in ("tau", "sigma", "tax", "migration")))
        self.assertEqual(names(self.before), names(self.after))
        for raw in (self.after, self.policy, (ROOT / ECONOMICS).read_bytes()):
            attrs = {n.attr for n in ast.walk(parsed(raw)) if isinstance(n, ast.Attribute)}
            self.assertTrue(attrs.isdisjoint({"tau", "sigma", "tax_rates", "migration_costs"}))

    def test_previous_published_files_byte_preserved(self) -> None:
        identity = json.loads((REPORT / "source_identity.json").read_text(encoding="utf-8"))
        checked = set()
        for key, records in identity["previous_preservation"].items():
            if not key.endswith("published_files"):
                continue
            for record in records:
                path = record["path"]
                if path == HJB or path in checked:
                    continue
                checked.add(path)
                raw = (ROOT / path).read_bytes()
                self.assertEqual(len(raw), record["bytes"], path)
                self.assertEqual(hashlib.sha256(raw).hexdigest(), record["sha256"], path)
                blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
                self.assertEqual(blob, record["git_blob"], path)
        self.assertGreaterEqual(len(checked), 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("before", "after"), required=True)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        OldSourceCounterexample if args.phase == "before" else RepairedBinding)
    outcome = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if outcome.wasSuccessful() else 1)
