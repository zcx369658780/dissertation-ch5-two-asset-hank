function mp4b_raw_vb_hank3_foc_edge_diagnostic(output_json, protected_root)
% Validation-only freeze of protected HANK3_FOC raw-pb IEEE semantics.
if isfile(output_json) || isfolder(output_json)
    error('MP4B:NoOverwrite','output path already exists');
end
expected = '772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D';
source_path = fullfile(protected_root,'HANK3_FOC.m');
if ~isfile(source_path) || ~strcmpi(file_sha256(source_path),expected)
    error('MP4B:SourceIdentity','protected HANK3_FOC identity mismatch');
end
addpath(protected_root);
resolved = which('HANK3_FOC');
if ~strcmpi(normalize_path(resolved),normalize_path(source_path))
    error('MP4B:SourceBinding','HANK3_FOC resolved outside protected root');
end

% Pre-frozen before the sole invocation: exact BB/BF/FB/FF witness plus edges.
ids = {'localized_BB','localized_BF','localized_FB','localized_FF', ...
    'positive_pb','negative_pb','zero_pb_positive_pa','zero_pb_negative_pa', ...
    'zero_pa_zero_pb','zero_a_negative_pb'};
pa = [0.0183013418028827,0.029712870660726632,0.0183013418028827,0.029712870660726632, ...
    1.5,0.5,1,-1,0,1];
pb = [0.0036470322698923963,0.0036470322698923963,-0.014003744365506235,-0.014003744365506235, ...
    1,-1,0,0,0,-1];
a = [9.473684210526315,9.473684210526315,9.473684210526315,9.473684210526315, ...
    1,1,1,1,1,0];
chi = struct('chi0',0.1,'chi1',2,'fixcost',0,'fixcost2',0,'a_bar',0.5);
template = struct('case_id','','pa',0,'pb',0,'a',0,'chi0',0,'chi1',0, ...
    'ratio_class','','ratio_value','','output_class','','output_value','');
rows = repmat(template,numel(ids),1);
dummy = struct();
for k=1:numel(ids)
    ratio = pa(k)./pb(k);
    value = HANK3_FOC(dummy,chi,pa(k),pb(k),a(k),0);
    rows(k) = struct('case_id',ids{k},'pa',pa(k),'pb',pb(k),'a',a(k), ...
        'chi0',chi.chi0,'chi1',chi.chi1,'ratio_class',classify(ratio), ...
        'ratio_value',encode_value(ratio),'output_class',classify(value), ...
        'output_value',encode_value(value));
end
manifest = struct('schema','CH5_MP4B_RAW_VB_HANK3_FOC_EDGE_V1', ...
    'protected_source',source_path,'protected_sha256',expected, ...
    'case_count',numel(rows),'cases',rows, ...
    'call_ledger',struct('matlab_scalar_batch',1,'HANK3_FOC_calls',numel(rows), ...
    'HJB',0,'KFE',0,'household',0,'multi_province',0));
fid = fopen(output_json,'w');
if fid < 0; error('MP4B:Persistence','cannot create output'); end
cleanup = onCleanup(@() fclose(fid));
fwrite(fid,jsonencode(manifest,'PrettyPrint',true),'char');
end

function out=classify(x)
if isnan(x); out='NaN'; elseif isinf(x) && x>0; out='+Inf'; ...
elseif isinf(x); out='-Inf'; else; out='finite'; end
end
function out=encode_value(x)
if isnan(x); out='NaN'; elseif isinf(x) && x>0; out='+Inf'; ...
elseif isinf(x); out='-Inf'; else; out=sprintf('%.17g',x); end
end
function out=normalize_path(p)
out=lower(strrep(char(p),'/','\'));
end
function out=file_sha256(p)
md=java.security.MessageDigest.getInstance('SHA-256');
fid=fopen(p,'r'); if fid<0; error('MP4B:Read','cannot read source'); end
c=onCleanup(@() fclose(fid)); bytes=fread(fid,Inf,'*uint8'); md.update(bytes);
out=lower(reshape(dec2hex(typecast(md.digest(),'uint8'))',1,[]));
end
