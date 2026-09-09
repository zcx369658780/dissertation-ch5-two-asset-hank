"""Synthetic-only tests; no model or solver imports/calls."""
import importlib.util, sys, unittest
from pathlib import Path
DIR=Path(__file__).resolve().parents[1]/"validators/multi_province/data_audit"; sys.path.insert(0,str(DIR))
from contract import parse_year, annual_indices, classify_fill, missing_runs, model_consumed_value

class Tests(unittest.TestCase):
 def test_year_parser(self): self.assertEqual(parse_year("2018年"),2018); self.assertEqual(parse_year(2009),2009); self.assertIsNone(parse_year(None))
 def test_original_matlab_year_contract(self):
  x=annual_indices(10); self.assertEqual(x["output_filename_year"],2018); self.assertEqual(x["workbook_calendar_year_at_data_row"],2009); self.assertEqual(x["regression_vintage_key"],19)
 def test_fill_classification(self):
  self.assertEqual(classify_fill(None,3,True,True),"MISSING_FILLED_INTERIOR"); self.assertEqual(classify_fill(None,3,False,True),"ENDPOINT_OR_EXTRAPOLATION_SUSPECT"); self.assertEqual(classify_fill(2,2,True,True),"OBSERVED_UNCHANGED"); self.assertEqual(classify_fill(2,3,True,True),"CHANGED_MECHANISM_UNRESOLVED")
 def test_missing_runs(self): self.assertEqual(missing_runs([1,None,None,2,None]),[(1,2,2),(4,4,1)])
 def test_unit_and_lineage_bookkeeping(self):
  self.assertEqual(model_consumed_value("GDP",10864.68),10864680.0); self.assertEqual(model_consumed_value("POP",6131),613100.0)
 def test_import_time_zero_science(self):
  spec=importlib.util.spec_from_file_location("data_contract",DIR/"contract.py"); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); self.assertNotIn("solve",module.__dict__); self.assertNotIn("matlab",module.__dict__)
if __name__=="__main__": unittest.main(verbosity=2)
