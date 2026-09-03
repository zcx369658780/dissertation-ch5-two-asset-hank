import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = process.env.MP4C_PACKAGE_ROOT || "D:/ProjectTemp/ch5-mp4c-manual-steady-state-comparison-package-20260903-001";
const matlabPath = "D:/MatlabProgram/2023年12月2日 多省份神经网络HANK_DIAGNOSTIC_PATCH_2026_06_23/12年稳态值.xlsx";
const label = "LEGACY_CALENDAR_BINDING_DIAGNOSTIC_ONLY__NOT_SAME_INPUT_PARITY_EVIDENCE";
const ctx = JSON.parse(await fs.readFile(`${root}/workbook_context.json`, "utf8"));
const colName = n => { let s=""; while(n){const r=(n-1)%26;s=String.fromCharCode(65+r)+s;n=Math.floor((n-1)/26)} return s; };
const style = (sheet, cols, rows) => { sheet.showGridLines=false; sheet.getRange(`A1:${colName(cols)}1`).format={fill:"#164E63",font:{bold:true,color:"#FFFFFF"}}; sheet.getRange(`A1:${colName(cols)}${rows}`).format.autofitColumns(); sheet.getRange(`A1:${colName(cols)}${rows}`).format.autofitRows(); sheet.freezePanes.freezeRows(1); };
const writeNew = async (path, content) => { await fs.writeFile(path, content, {encoding:"utf8",flag:"wx"}); };
const exportBook = async (book, path) => { try { await fs.access(path); throw new Error(`Refusing overwrite: ${path}`); } catch (error) { if (error.code !== "ENOENT") throw error; } const out=await SpreadsheetFile.exportXlsx(book); await out.save(path); };

async function pythonWorkbook() {
  const book=Workbook.create();
  const readme=book.worksheets.add("README");
  readme.getRange("A1:B6").values=[["Package","Owner-A 13-pass steady states"],["Years",ctx.years.join(", ")],["2018","Absent: both authorized attempts failed; no zero fill."],["2023","Out of scope."],["MATLAB boundary",label],["Note","Values are copied from immutable Python final_steady_state JSON records."]];
  readme.getRange("A1:A6").format={fill:"#164E63",font:{bold:true,color:"#FFFFFF"}}; readme.getRange("A1:B6").format.autofitColumns();
  for (const field of ctx.fields) {
    const sh=book.worksheets.add(field); const rows=[["province",...ctx.years]];
    for (const province of ctx.province_order) rows.push([province,...ctx.years.map(y=>ctx.wide[field][province][y] ?? null)]);
    sh.getRangeByIndexes(0,0,rows.length,rows[0].length).values=rows; style(sh,rows[0].length,rows.length); sh.getRange(`B2:${colName(rows[0].length)}${rows.length}`).format.numberFormat="0.0000000000";
  }
  await exportBook(book,`${root}/PYTHON_OWNER_A_STEADY_STATE_2009_2022_13PASS.xlsx`);
}

function normalized(v){ return typeof v === "string" ? v.trim().replace(/[市省]$/u,"") : v; }
async function matlabWorkbook() {
  const source=await SpreadsheetFile.importXlsx(await FileBlob.load(matlabPath));
  const sheets=await source.inspect({kind:"sheet",include:"id,name",maxChars:10000});
  const output=Workbook.create(); const meta=[]; const extracted={rows:[]};
  for (const name of ["稳态值_Yt0","稳态值_Yt","稳态值_Kt0","稳态值_Kt","稳态值_Lt0","稳态值_Lt"]) {
    const src=source.worksheets.getItemOrNullObject(name); if (!src || src.isNullObject) throw new Error(`Missing MATLAB sheet ${name}`);
    const used=src.getUsedRange(); const values=used.values; let candidate=-1;
    for(let start=values.length-31;start>=0;start--){ const names=values.slice(start,start+31).map(r=>normalized(r[0])); if(names.every(x=>typeof x==="string" && x.length>0) && new Set(names).size===31){candidate=start;break;} }
    if(candidate<0) throw new Error(`Cannot identify final 31-province block in ${name}`);
    const block=values.slice(candidate,candidate+31).map(r=>r.slice(0,15)); const out=output.worksheets.add(name); out.getRange("A1").values=[[label]]; out.getRange("A2:O2").values=[["province",...Array.from({length:14},(_,i)=>2009+i)]]; out.getRangeByIndexes(2,0,31,15).values=block; out.getRange("A1:O1").format={fill:"#7F1D1D",font:{bold:true,color:"#FFFFFF"}}; out.getRange("A2:O2").format={fill:"#164E63",font:{bold:true,color:"#FFFFFF"}}; out.freezePanes.freezeRows(2); out.getRange("A1:O33").format.autofitColumns();
    meta.push({sheet:name,final_complete_block_excel_rows:`${candidate+1}-${candidate+31}`,province_order:block.map(r=>normalized(r[0])),year_columns:[...Array.from({length:14},(_,i)=>2009+i)],semantic_label:label});
    const field=name.replace("稳态值_","");
    for(let i=0;i<31;i++){ for(let yi=0;yi<14;yi++){ const year=2009+yi; const province=normalized(block[i][0]); const v=block[i][yi+1]; let row=extracted.rows.find(x=>x.year===year&&x.province===province); if(!row){row={year,province};extracted.rows.push(row)} row[field]=Number(v); } }
  }
  await exportBook(output,`${root}/MATLAB_LEGACY_STEADY_STATE_RECORD_EXTRACT.xlsx`);
  extracted.rows=extracted.rows.filter(r=>["Yt","Kt","Lt","Yt0","Kt0","Lt0"].every(k=>Number.isFinite(r[k]))); if(extracted.rows.length!==434) throw new Error(`Expected 434 MATLAB extracted rows, got ${extracted.rows.length}`);
  await writeNew(`${root}/matlab_extract.json`,JSON.stringify({workbook:matlabPath,label,source_sheet_metadata:meta,rows:extracted.rows},null,2)+"\n");
  for(const field of ["Yt","Kt","Lt","Yt0","Kt0","Lt0"]){ const lines=[`semantic_label,year,province,${field}`]; for(const r of extracted.rows)lines.push([label,r.year,JSON.stringify(r.province),r[field]].join(",")); await writeNew(`${root}/matlab_legacy_${field}_2009_2022.csv`,lines.join("\n")+"\n"); }
}
await pythonWorkbook(); await matlabWorkbook();
