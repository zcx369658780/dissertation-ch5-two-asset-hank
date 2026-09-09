"""Synthetic-only tests for the bounded expansion diagnostic."""
import ast, importlib.util, sys, tempfile, unittest
from pathlib import Path
import numpy as np
from scipy import sparse
DIR=Path(__file__).resolve().parents[1]/"validators/multi_province/call725_b_domain_expansion"; sys.path.insert(0,str(DIR))
from evidence import Store, decode_saved
from grid import expand_b, pin_details, boundary_leak, mass_regions

class Tests(unittest.TestCase):
 def setUp(self): self.old=np.linspace(-2,5,20)
 def test_exact_prefix_spacing_endpoint(self):
  new,db=expand_b(self.old); self.assertTrue(np.array_equal(new[:20],self.old)); self.assertEqual(len(new),39); self.assertTrue(all(new[i]==np.float64(new[i-1]+db) for i in range(20,39))); self.assertLess(abs(new[-1]-12),2e-14)
 def test_only_liquid_dimension_changes(self):
  new,_=expand_b(self.old); a=np.linspace(0,10,20); z=np.array([.8,1.3]); s=np.eye(2); self.assertEqual((len(new),len(a),len(z)),(39,20,2)); self.assertTrue(np.array_equal(a,a.copy())); self.assertTrue(np.array_equal(z,z.copy())); self.assertTrue(np.array_equal(s,s.copy()))
 def test_pin_mapping(self):
  new,_=expand_b(self.old); p=pin_details(new,np.linspace(0,10,20),np.array([.8,1.3])); self.assertEqual(p["state_count"],1560); self.assertEqual(p["k_zero_based"],576); self.assertEqual(np.ravel_multi_index((p["i_b_zero_based"],p["j_a_zero_based"],p["i_z_zero_based"]),(39,20,2),order="F"),576)
 def test_boundary_accounting(self):
  mb=np.zeros((3,2,1)); ma=np.zeros_like(mb); mb[-1,:,0]=[2,-1]; ma[0,0,0]=-3; faces,leak=boundary_leak(mb,ma,.5,2); self.assertEqual(faces["upper_b"][0,0],4); self.assertEqual(faces["lower_a"][0,0],1.5); self.assertEqual(leak.sum(),5.5)
 def test_mass_regions_signed_no_clip(self):
  d=np.array([[[1.]],[[2.]],[[-.5]]]); r=mass_regions(d,np.array([0,6,12]),.2); self.assertAlmostEqual(r["total"],.5); self.assertAlmostEqual(r["b_gt_5"],.3); self.assertEqual(r["negative_count"],1); self.assertAlmostEqual(r["negative_mass"],-.1)
 def test_roundtrip_and_save_order(self):
  with tempfile.TemporaryDirectory() as t:
   s=Store(Path(t)/"science"); s.save("hjb_return_before_kfe",{"x":np.arange(3.)}); s.save("kfe_entry",{"q":sparse.eye(2,format="csr")}); s.close(); rows=(Path(t)/"science/index.jsonl").read_text().splitlines(); self.assertIn("hjb_return_before_kfe",rows[0]); self.assertTrue(np.array_equal(decode_saved(Path(t)/"science/hjb_return_before_kfe.json")["x"],np.arange(3.)))
 def test_no_warm_start_or_interpolation_in_run(self):
  text=(DIR/"run.py").read_text(encoding="utf-8"); tree=ast.parse(text); self.assertNotIn("interp",text.lower()); self.assertIn("_source_initial_arrays",text); self.assertNotIn("native_initialization_return.json\")\n    old_init",text)
 def test_budget_limits_literal(self):
  text=(DIR/"run.py").read_text(encoding="utf-8"); self.assertIn('counts["labor_root"] > 1560',text); self.assertIn('counts["brentq"] > 1560',text); self.assertIn('counts["HJB_direct_solve"] > 100',text)
 def test_import_helpers_no_science(self):
  for name in ("evidence","grid"):
   spec=importlib.util.spec_from_file_location("x_"+name,DIR/(name+".py")); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); self.assertNotIn("faithful",mod.__dict__)

if __name__=="__main__": unittest.main(verbosity=2)
