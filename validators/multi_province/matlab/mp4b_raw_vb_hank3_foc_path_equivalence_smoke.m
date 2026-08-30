function manifest=mp4b_raw_vb_hank3_foc_path_equivalence_smoke(logical_root,physical_root,smoke_root)
% Infrastructure-only exact-pair guard smoke. HANK3_FOC is never invoked.
if isfolder(smoke_root) || isfile(smoke_root)
    error('MP4B:NoOverwrite','smoke_root must not exist');
end
expected = '772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D';
expected_logical = normalize_root("C:\MatlabProgram\2023年12月2日 多省份神经网络HANK");
expected_physical = normalize_root("D:\MatlabProgram\2023年12月2日 多省份神经网络HANK");
if normalize_root(logical_root) ~= expected_logical || normalize_root(physical_root) ~= expected_physical
    error('MP4B:PathEquivalence','model roots are not the exact protected pair');
end
verify_exact_junction();
if ~isfolder(logical_root) || ~isfolder(physical_root) ...
        || canonical_root(logical_root) ~= expected_physical ...
        || canonical_root(physical_root) ~= expected_physical
    error('MP4B:PathEquivalence','logical and physical model roots are not equivalent');
end
logical_source=fullfile(logical_root,'HANK3_FOC.m');
physical_source=fullfile(physical_root,'HANK3_FOC.m');
if ~isfile(logical_source) || ~isfile(physical_source) ...
        || ~strcmpi(file_sha256(logical_source),expected) ...
        || ~strcmpi(file_sha256(physical_source),expected)
    error('MP4B:SourceIdentity','protected HANK3_FOC identity mismatch');
end
old_path=path; cleanup_path=onCleanup(@() path(old_path));
addpath(logical_root);
resolved=which('HANK3_FOC');
allowed=[expected_logical,expected_physical];
resolved_parent=normalize_root(string(fileparts(resolved)));
if isempty(resolved) || ~root_allowed(resolved_parent,allowed) || ~strcmpi(file_sha256(resolved),expected)
    error('MP4B:SourceBinding','HANK3_FOC resolved outside protected root');
end
sibling_probe=normalize_root("D:\MatlabProgram\2023年12月2日 多省份神经网络HANK-sibling");
unrelated_rejected=~root_allowed(sibling_probe,allowed);
if ~unrelated_rejected
    error('MP4B:PathEquivalence','unrelated root representation was accepted');
end
smoke_dir=java.io.File(char(smoke_root));
if ~smoke_dir.mkdir()
    error('MP4B:NoOverwrite','cannot atomically create smoke root');
end
manifest_path=fullfile(smoke_root,'path_equivalence_smoke_manifest.json');
reserve_new_file(manifest_path);
manifest=struct('marker','MP4B_RAW_VB_HANK3_FOC_PATH_EQUIVALENCE_SMOKE_PASS', ...
    'logical_protected_root',logical_root,'physical_protected_root',physical_root, ...
    'resolved_helper_path',resolved,'protected_sha256',expected, ...
    'unrelated_root_rejected',unrelated_rejected, ...
    'call_ledger',struct('guard_smoke_batches',1,'HANK3_FOC_calls',0, ...
    'HJB',0,'KFE',0,'household',0,'multi_province',0));
fid=fopen(manifest_path,'w');
if fid<0; error('MP4B:Persistence','cannot open reserved manifest'); end
cleanup_file=onCleanup(@() fclose(fid));
fwrite(fid,jsonencode(manifest,'PrettyPrint',true),'char');
end

function value=normalize_root(value)
value=lower(replace(string(value),'/','\'));
value=strip(value,'right','\');
end
function value=canonical_root(value)
value=normalize_root(string(java.io.File(char(value)).getCanonicalPath()));
end
function tf=root_allowed(candidate,allowed)
tf=any(normalize_root(candidate) == allowed);
end
function verify_exact_junction()
command = ['powershell.exe -NoProfile -NonInteractive -Command ' ...
    '"$i=Get-Item -LiteralPath ''C:\MatlabProgram'' -Force;' ...
    '$t=@($i.Target);' ...
    'if($i.LinkType -eq ''Junction'' -and $t.Count -eq 1 -and ' ...
    '[IO.Path]::GetFullPath([string]$t[0]).TrimEnd(''\'') -ieq ''D:\MatlabProgram'')' ...
    '{[Console]::Out.Write(''PASS'');exit 0};exit 17"'];
[status,out]=system(command);
if status ~= 0 || ~strcmp(strtrim(out),'PASS')
    error('MP4B:PathEquivalence','exact C-to-D junction verification failed');
end
end
function reserve_new_file(p)
file=java.io.File(char(p));
if ~file.createNewFile()
    error('MP4B:NoOverwrite','cannot atomically reserve output');
end
end
function out=file_sha256(p)
md=java.security.MessageDigest.getInstance('SHA-256');
fid=fopen(p,'r'); if fid<0; error('MP4B:Read','cannot read source'); end
c=onCleanup(@() fclose(fid)); bytes=fread(fid,Inf,'*uint8'); md.update(bytes);
out=lower(reshape(dec2hex(typecast(md.digest(),'uint8'))',1,[]));
end
