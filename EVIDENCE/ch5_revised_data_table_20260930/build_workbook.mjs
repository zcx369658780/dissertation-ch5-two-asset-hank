import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root='D:/ProjectTemp/c5k1bturn56/EVIDENCE/ch5_revised_data_table_20260930';
const audit=JSON.parse(await fs.readFile(root+'/data_audit.json','utf8'));
const wb=Workbook.create();
const sh=wb.worksheets.add('修订对照');
const src=wb.worksheets.add('来源与候选');
for(const s of [sh,src]){s.showGridLines=false;s.getRange('A1:M135').format.font={name:'Arial',size:11,color:'#222222'};s.getRange('A1:M135').format.verticalAlignment='center';}
sh.getRange('A2').values=[['第五章省级数据修订对照｜2015—2018']];
sh.getRange('A2').format.font={size:16,bold:true};
sh.getRange('A3').values=[['31省 × 4年；GDP 124项版本差异，人口0项差异。采集日：2026-09-30。']];
sh.getRange('A4').values=[['独立数据候选；未接入模型、未重新校准。GDP价格与发布版本的精确绑定仍待核实。']];
sh.getRange('A5').values=[['人均代理 = 10000 × GDP（亿元）÷ 年末常住人口（万人）；不同于年平均人口口径的官方人均GDP。']];
sh.getRange('A4').format.font={color:'#9A5C00'};
sh.getRange('A7:M7').values=[['省份','年份','旧GDP\n亿元','新版GDP\n亿元','GDP差额\n亿元','GDP变幅','旧人口\n万人','新版人口\n万人','人口差额\n万人','旧人均代理\n元/人','新人均代理\n元/人','代理差额\n元/人','来源编号']];
const rows=audit.records.map(r=>[r.province,r.year,r.old_gdp,r.new_gdp,null,null,r.old_population,r.new_population,null,null,null,null,'S1–S4']);
sh.getRange('A8:M131').values=rows;
for(const [col,fn] of Object.entries({E:r=>`=D${r}-C${r}`,F:r=>`=E${r}/C${r}`,I:r=>`=H${r}-G${r}`,J:r=>`=10000*C${r}/G${r}`,K:r=>`=10000*D${r}/H${r}`,L:r=>`=K${r}-J${r}`})){
 sh.getRange(`${col}8:${col}131`).formulas=rows.map((_,i)=>[fn(i+8)]);
}
sh.getRange('A7:M7').format.fill='#30465D';sh.getRange('A7:M7').format.font={bold:true,color:'#FFFFFF'};sh.getRange('A7:M7').format.wrapText=true;sh.getRange('A7:M7').format.horizontalAlignment='center';sh.getRange('A7:M7').format.rowHeight=43;
sh.getRange('A8:M131').format.rowHeight=24;
sh.getRange('A1:A131').format.columnWidth=23;sh.getRange('B1:B131').format.columnWidth=9;sh.getRange('C1:M131').format.columnWidth=17;
sh.getRange('C8:E131').setNumberFormat('#,##0.0');sh.getRange('F8:F131').setNumberFormat('0.00%');sh.getRange('G8:I131').setNumberFormat('#,##0');sh.getRange('J8:L131').setNumberFormat('#,##0.00');sh.getRange('B8:B131').setNumberFormat('0');
for(let p=0;p<31;p++){if(p%2===0)sh.getRange(`A${8+p*4}:M${11+p*4}`).format.fill='#F1F4F7';}
sh.freezePanes.freezeRows(7);sh.freezePanes.freezeColumns(2);sh.tabColor='#30465D';
src.getRange('A2').values=[['来源、版本与其他数据评估']];src.getRange('A2').format.font={size:16,bold:true};
src.getRange('A4:E4').values=[['编号','指标 / 候选','证据与口径','使用结论','定位 / 哈希']];
const sourceRows=[
 ['S1','新版地区生产总值','国家统计局分省年度数据；31省2015—2018；亿元；页面注明第五次经济普查后系统修订1992—2023历史数据。','纳入独立新表；确切发布日期未显示。','https://data.stats.gov.cn/dg/website/page.html#/pc/national/fsYearData\n证据：nbs_gdp_display.json、nbs_gdp_dom.txt'],
 ['S2','新版年末常住人口','同一官方数据库；31省2015—2018；万人；常住人口口径；不除以三。','纳入新表；与旧表124项全部一致。','https://data.stats.gov.cn/dg/website/page.html#/pc/national/fsYearData\n证据：nbs_population_display.json、nbs_population_dom.txt'],
 ['S3','旧GDP表','Owner确认来自NBS直接下载；分省年度数据H等年度列；2015—2018源值与保留面板一致。','保留旧值；124项差异属于版本差异，未发现处理错配。',audit.source_paths.old_gdp+'\nSHA256 '+audit.source_hash_before.old_gdp],
 ['S4','旧人口表','年末常住人口；万人；2015—2018源值与保留面板一致。','保留旧值，不改原文件。',audit.source_paths.old_population+'\nSHA256 '+audit.source_hash_before.old_population],
 ['S5','GDP价格依据','中国统计年鉴2023表3-9注：本表绝对数按当年价格计算，指数按不变价格计算。','支持现价解释；新版数据库页面未独立标价，精确版本价格绑定待核实。','https://www.stats.gov.cn/sj/ndsj/2023/html/C03-09.jpg'],
 ['S6','保留的旧处理面板','248项原GDP/人口对照均一致；完整覆盖31省×4年。','只读对照，未更新原面板。',audit.source_paths.old_panel+'\nSHA256 '+audit.source_hash_before.old_panel],
 ['P1','已购人口与就业年鉴','2015/16归档为嵌套zip/rar；2017/18含表格，但条目中文编码不可靠。年鉴年份不等于数据年份。','未核验具体人口表题与年份；暂不补入数值。','D:\\BaiduNetdiskDownload\\NJ73-中国人口与就业统计年鉴1949-2023年'],
 ['P2','已购分省三次产业就业数据','表中字段为就业人员、三次产业就业人数及占比；单位万人/百分比；销售方注明中国统计年鉴及省年鉴。','可作就业辅助候选；缺逐项年鉴版本/表号/补数映射，不替代常住人口。','D:\\BaiduNetdiskDownload\\sj10-分省份按三次产业分从业人员数（就业人员数）1985-2024年数据\\分省份按三次产业分从业人员数（就业人员数）1985-2024年数据.xlsx'],
 ['U1','资本、TFP等其他指标','本轮未定位可独立核验的省级同口径修订来源；市级固定资产投资不等于省级固定资本形成，市级TFP不等于HANK生产率。','本轮不填入、更不推算校准。','仅记录口径缺口；未打开其他付费目录'],
 ['U2','模型与论文门','本工作簿只记录数据和算术代理；没有phi矩阵、模型执行、校准或Results。','C9暂停；旧调用账本未解决；Results eligibility FALSE。','下一步：价格/版本绑定与数据采纳审查；程序接入需另行任务。']
];
src.getRange('A5:E14').values=sourceRows;
src.getRange('A4:E4').format.fill='#30465D';src.getRange('A4:E4').format.font={bold:true,color:'#FFFFFF'};src.getRange('A4:E4').format.rowHeight=28;
src.getRange('A5:E14').format.wrapText=true;src.getRange('A5:E14').format.rowHeight=100;src.getRange('A5:E14').format.verticalAlignment='top';
src.getRange('A1:A14').format.columnWidth=8;src.getRange('B1:B14').format.columnWidth=24;src.getRange('C1:D14').format.columnWidth=55;src.getRange('E1:E14').format.columnWidth=95;
wb.recalculate();
for(const i of [0,61,123]){
 const r=audit.records[i], got=sh.getRange(`E${i+8}:L${i+8}`).values[0];
 if(Math.abs(got[0]-(r.new_gdp-r.old_gdp))>1e-8 || Math.abs(got[6]-10000*r.new_gdp/r.new_population)>1e-7)throw Error('formula mismatch');
}
const check=await wb.inspect({kind:'table',range:'修订对照!A7:M12',include:'values,formulas',tableMaxRows:6,tableMaxCols:13,maxChars:5500});
await fs.writeFile(root+'/workbook_inspection.ndjson',check.ndjson);
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50},summary:'formula error scan'});
await fs.writeFile(root+'/formula_error_scan.ndjson',errors.ndjson);
for(const [name,range,file] of [['修订对照','A1:M15','comparison_preview.png'],['来源与候选','A1:E14','sources_preview.png']]){
 const img=await wb.render({sheetName:name,range,scale:1.5,format:'png'});await fs.writeFile(root+'/'+file,new Uint8Array(await img.arrayBuffer()));
}
const out=await SpreadsheetFile.exportXlsx(wb);await out.save(root+'/第五章_省级修订数据候选_2015-2018.xlsx');
await fs.writeFile(root+'/build_check.json',JSON.stringify({exported:true,rows:124,representative_formula_rows:[8,69,131],science_calls:0},null,2));
console.log('Exported revised data candidate, 124 rows, two sheets.');
