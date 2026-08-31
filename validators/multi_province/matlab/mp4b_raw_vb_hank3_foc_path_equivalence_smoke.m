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
junction_evidence=verify_exact_junction();
if ~isfolder(logical_root) || ~isfolder(physical_root)
    error('MP4B:PathEquivalence','exact logical and physical model roots must exist');
end
logical_source=fullfile(logical_root,'HANK3_FOC.m');
physical_source=fullfile(physical_root,'HANK3_FOC.m');
logical_sha=file_sha256(logical_source);
physical_sha=file_sha256(physical_source);
if ~isfile(logical_source) || ~isfile(physical_source) ...
        || ~strcmpi(logical_sha,expected) || ~strcmpi(physical_sha,expected)
    error('MP4B:SourceIdentity','protected HANK3_FOC identity mismatch');
end
old_path=path; cleanup_path=onCleanup(@() path(old_path));
addpath(logical_root);
resolved=which('HANK3_FOC');
allowed=[expected_logical,expected_physical];
resolved_parent=normalize_root(string(fileparts(resolved)));
resolved_sha=file_sha256(resolved);
finite_root_membership=root_allowed(resolved_parent,allowed);
if isempty(resolved) || ~finite_root_membership || ~strcmpi(resolved_sha,expected)
    error('MP4B:SourceBinding','HANK3_FOC resolved outside protected root');
end
sibling_probe=normalize_root("D:\MatlabProgram\2023年12月2日 多省份神经网络HANK-sibling");
other_d_probe=normalize_root("D:\MatlabProgram\other-model");
sibling_rejected=~root_allowed(sibling_probe,allowed);
unrelated_rejected=~root_allowed(other_d_probe,allowed);
if ~sibling_rejected || ~unrelated_rejected
    error('MP4B:PathEquivalence','unrelated root representation was accepted');
end
smoke_dir=java.io.File(char(smoke_root));
if ~smoke_dir.mkdir()
    error('MP4B:NoOverwrite','cannot atomically create smoke root');
end
manifest_path=fullfile(smoke_root,'path_equivalence_smoke_manifest.json');
reserve_new_file(manifest_path);
manifest=struct('marker','MP4B_RAW_VB_HANK3_FOC_EXACT_JUNCTION_GUARD_SMOKE_PASS', ...
    'logical_protected_root',logical_root,'physical_protected_root',physical_root, ...
    'junction_evidence',junction_evidence, ...
    'logical_helper_path',logical_source,'logical_helper_sha256',logical_sha, ...
    'physical_helper_path',physical_source,'physical_helper_sha256',physical_sha, ...
    'resolved_helper_path',resolved,'resolved_helper_sha256',resolved_sha, ...
    'protected_sha256',expected,'finite_root_membership',finite_root_membership, ...
    'negative_probe_result',struct('sibling_rejected',sibling_rejected, ...
    'unrelated_d_root_rejected',unrelated_rejected,'all_pass',true), ...
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
function tf=root_allowed(candidate,allowed)
tf=any(normalize_root(candidate) == allowed);
end
function evidence=verify_exact_junction()
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
evidence=struct('logical_storage_root','C:\MatlabProgram', ...
    'link_type','Junction','target_count',1,'sole_target','D:\MatlabProgram');
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
