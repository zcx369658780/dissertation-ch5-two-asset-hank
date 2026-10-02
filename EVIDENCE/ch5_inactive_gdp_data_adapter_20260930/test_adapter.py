"""Invented fixtures only; no scientific/helper import and no real matrix."""
import copy
from dataclasses import FrozenInstanceError
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from adapter import CANONICAL_AXIS, load_inactive_snapshot

class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path=Path(self.tmp.name)/'fixture.json'
        self.d={'schema':'CH5_REVISED_DATA_CANDIDATE_V1','science_calls':0,
          'model_imports':0,'wedge_matrices':0,'model_activation':False,
          'results_eligibility':False,'display_hashes':{k:'a'*64 for k in
           ('nbs_gdp_dom.txt','nbs_gdp_display.json','nbs_population_dom.txt','nbs_population_display.json')},
          'display_capture_times':{'gdp':'2026-09-30T01:00:00Z','population':'2026-09-30T01:00:01Z'},
          'records':[{'province':n,'year':y,'new_gdp':i*100.0+y,'new_population':i*10.0}
                     for i,n in CANONICAL_AXIS for y in range(2015,2019)]}
    def load(self, d=None, order=CANONICAL_AXIS, target=2018, sha=None):
        raw=json.dumps(self.d if d is None else d,ensure_ascii=False).encode()
        self.path.write_bytes(raw)
        return load_inactive_snapshot(self.path,sha or hashlib.sha256(raw).hexdigest(),
                                      target_year=target,province_order=order)
    def test_select_2017_and_preserve_units(self):
        s=self.load();self.assertEqual(s.observation_year,2017)
        self.assertEqual(len(s.records),31)
        self.assertEqual(s.records[0].gdp_raw_100m_yuan,2117.0)
        self.assertEqual(s.records[0].population_raw_10k_persons,10.0)
    def test_explicit_axis_reordering(self):
        s=self.load(order=tuple(reversed(CANONICAL_AXIS)))
        self.assertEqual(s.records[0].province_index,31)
        self.assertEqual(s.records[0].gdp_raw_100m_yuan,5117.0)
    def test_price_and_activation_remain_false(self):
        s=self.load();self.assertIs(s.price_verified,False)
        self.assertIs(s.model_activation,False);self.assertIsNone(s.release_date)
        self.assertEqual(s.information_set,'retrospective_revised')
        with self.assertRaises(FrozenInstanceError):s.target_year=2019
    def test_hash_mismatch(self):
        with self.assertRaises(ValueError):self.load(sha='f'*64)
    def test_duplicate_record(self):
        d=copy.deepcopy(self.d);d['records'][0]=d['records'][1]
        with self.assertRaises(ValueError):self.load(d)
    def test_missing_record(self):
        d=copy.deepcopy(self.d);d['records'].pop()
        with self.assertRaises(ValueError):self.load(d)
    def test_wrong_year_and_bool(self):
        for year in (2019,True):
            with self.subTest(year=year):
                with self.assertRaises(ValueError):self.load(target=year)
    def test_wrong_name_index_mapping(self):
        order=list(CANONICAL_AXIS);order[0]=(1,order[1][1])
        with self.assertRaises(ValueError):self.load(order=tuple(order))
    def test_invalid_numerics(self):
        for value in (True,0,-1,float('nan'),float('inf'),'2117'):
            d=copy.deepcopy(self.d);d['records'][0]['new_gdp']=value
            with self.subTest(value=value):
                with self.assertRaises(ValueError):self.load(d)
    def test_provenance_missing_or_activated(self):
        for field,value in (('display_hashes',{}),('model_activation',True),('science_calls',True)):
            d=copy.deepcopy(self.d);d[field]=value
            with self.subTest(field=field):
                with self.assertRaises(ValueError):self.load(d)
if __name__=='__main__':unittest.main(verbosity=2)
