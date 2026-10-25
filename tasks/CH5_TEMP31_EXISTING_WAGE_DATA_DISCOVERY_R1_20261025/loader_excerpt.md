# Static loader excerpt; not executed

Source: validators/multi_province/mp4b_python_empirical.py
SHA-256: b9165a71e6a206dc78ad86c23c3502f27a4d81f1329d2efe83c304809556789b
Raw Git Blob: 102dbb88a629283a71a3f02541cd7f74f9944213

101: def load_entry_state(canonical_path: Path) -> tuple[dict, tuple[dict[str, object], ...]]:
102:     canonical = json.loads(Path(canonical_path).read_text(encoding="utf-8"))
103:     if canonical["binding"] != {"analysis_index":1,"calendar_year":2009,"data_mat_index":1,
104:             "output_filename_year":2009,"regression_vintage_key":10,"workbook_data_row_index":10}:
105:         raise ValueError("canonical annual binding mismatch")
106:     v=canonical["vectors"]; s=canonical["scalars"]
107:     states=[]
108:     for i,name in enumerate(canonical["province_order"]):
109:         state={"name":name,"N":v["pop"][i],"alpha":v["ind_alpha"][i],"Zt":v["initialized_zt"][i],
110:             "Kt0":v["cap"][i],"Kt":v["cap"][i],"Kt_prev":v["cap"][i],"Lt":v["pop"][i],
111:             "Lt_prev":v["pop"][i],"Yt0":v["gdp"][i],"Yt":v["gdp"][i],"Zt_1":v["initialized_zt"][i],
112:             "GovInv":v["gov_inv"][i],"inter_prv_ratio":v["inter_province_asset_ratio"][i],
113:             "rb_gap":s["rb_gap"],"rah":s["rah"],"ra":s["ra"],"it":s["nominal_rate"],
114:             "rb":s["rb"],"rk":s["rk"],"wjt":s["wjt"],"w":s["composite_wage"],
115:             "Tt":s["transfer_income"],"pit":s["inflation"],"pit_1":s["inflation"],
116:             "totalpit":s["inflation"],"epsilon_pi":0.0,"tau":s["wage_tax"],"At":s["initial_at"],
117:             "Bt":s["initial_bt"],"mt":s["initial_mt"],"Ct":s["initial_ct"],"AtTax":0.0,
118:             "GovSurplus":0.0,"corptau":s["corporate_tax"],"ramin":0.02,"ramax":0.09,
119:             "wjtmin":0.8,"wjtmax":1.3}
120:         states.append(state)
121:     return canonical, tuple(states)

Assigns common wage/tax scalars to named province states; no generator or economic wage unit proven.
