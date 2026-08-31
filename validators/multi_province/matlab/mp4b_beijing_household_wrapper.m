function manifest = mp4b_beijing_household_wrapper(mode, run_root, contract_path, logical_root, physical_root)
% Validation wrapper. Smoke mode returns before the protected household call.
expected_logical = normalize_root("C:\MatlabProgram\2023年12月2日 多省份神经网络HANK");
expected_physical = normalize_root("D:\MatlabProgram\2023年12月2日 多省份神经网络HANK");
expected_hjb_sha = '049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE';
expected_contract_sha = 'FE833FAEB48521CD0C7594627AF6FB5012F9497A455E9B2C5E7490E0C40E6F22';
mode = string(mode);
if mode ~= "smoke" && mode ~= "run"
    error('MP4B:Mode','mode must be smoke or run');
end
if normalize_root(logical_root) ~= expected_logical || normalize_root(physical_root) ~= expected_physical
    error('MP4B:SourceBinding','model roots are not the exact protected pair');
end
run_root = string(run_root);
[run_parent,run_name,run_ext] = fileparts(run_root);
if normalize_root(run_parent) ~= normalize_root("D:\ProjectTemp") || strlength(run_name + run_ext) == 0
    error('MP4B:RunRoot','run_root must be a fresh direct child of D:\ProjectTemp');
end
if isfolder(run_root) || isfile(run_root)
    error('MP4B:NoOverwrite','run_root already exists');
end
if ~isfile(contract_path) || ~strcmpi(file_sha256(contract_path),expected_contract_sha)
    error('MP4B:ContractIdentity','same-input candidate contract identity mismatch');
end
junction_evidence = verify_exact_junction();
logical_source = fullfile(logical_root,'HANK_2ASSETS_HJB.m');
physical_source = fullfile(physical_root,'HANK_2ASSETS_HJB.m');
if ~isfile(logical_source) || ~isfile(physical_source)
    error('MP4B:SourceIdentity','logical or physical protected HJB source is absent');
end
logical_sha = file_sha256(logical_source);
physical_sha = file_sha256(physical_source);
if ~strcmpi(logical_sha,expected_hjb_sha) || ~strcmpi(physical_sha,expected_hjb_sha)
    error('MP4B:SourceIdentity','logical or physical protected HJB SHA mismatch');
end
old_path = path;
cleanup_path = onCleanup(@() path(old_path));
addpath(logical_root,'-begin');
resolved = which('HANK_2ASSETS_HJB');
allowed = [expected_logical,expected_physical];
resolved_parent = normalize_root(string(fileparts(resolved)));
resolved_sha = file_sha256(resolved);
finite_root_membership = root_allowed(resolved_parent,allowed);
if isempty(resolved) || ~finite_root_membership || ~strcmpi(resolved_sha,expected_hjb_sha)
    error('MP4B:SourceBinding','HANK_2ASSETS_HJB resolved outside the exact protected pair');
end
sibling_rejected = ~root_allowed(normalize_root(physical_root + "-sibling"),allowed);
unrelated_rejected = ~root_allowed(normalize_root("D:\MatlabProgram\other-model"),allowed);
if ~sibling_rejected || ~unrelated_rejected
    error('MP4B:SourceBinding','negative root probe was accepted');
end
owned_root = java.io.File(char(run_root));
if ~owned_root.mkdir()
    error('MP4B:NoOverwrite','cannot atomically create fresh run_root');
end
wrapper_path = string([mfilename('fullpath'),'.m']);
manifest_path = fullfile(run_root,'matlab_wrapper_smoke_manifest.json');
ledger = complete_zero_ledger();
if mode == "smoke"
    manifest = struct( ...
        'marker','MP4B_BEIJING_MATLAB_HOUSEHOLD_WRAPPER_ZERO_CALL_SMOKE_PASS', ...
        'mode','smoke','wrapper_path',wrapper_path,'wrapper_sha256',file_sha256(wrapper_path), ...
        'logical_protected_root',logical_root,'physical_protected_root',physical_root, ...
        'junction_evidence',junction_evidence, ...
        'logical_hjb_path',logical_source,'logical_hjb_sha256',logical_sha, ...
        'physical_hjb_path',physical_source,'physical_hjb_sha256',physical_sha, ...
        'resolved_hjb_path',resolved,'resolved_hjb_sha256',resolved_sha, ...
        'finite_root_membership',finite_root_membership, ...
        'negative_probe_result',struct('sibling_rejected',sibling_rejected, ...
            'unrelated_d_root_rejected',unrelated_rejected,'all_pass',true), ...
        'same_input_contract_path',contract_path, ...
        'same_input_contract_sha256',file_sha256(contract_path), ...
        'matlab_version',version,'matlab_release',version('-release'), ...
        'call_ledger',ledger);
    persist_new_json(manifest_path,manifest);
    return
end

% Future scientific mode. It is unreachable from smoke mode and is not run by this task.
contract = jsondecode(fileread(contract_path));
p = contract.param; g = contract.grid; n = contract.num; c = contract.CHI; r = contract.results;
param = struct('ga',p.ga,'alphap',p.alphap,'alphal',p.alphal,'rho',p.rho,'frisch_l',p.frisch_l);
grid = struct('I',g.I,'bmin',g.bmin,'bmax',g.bmax,'J',g.J,'amin',g.amin,'amax',g.amax, ...
    'Nz',g.Nz,'zmin',g.zmin,'zmax',g.zmax,'z',reshape(g.z,1,[]),'la_mat',g.la_mat);
num = struct('maxit',n.maxit,'crit',n.crit,'homecrit',n.homecrit,'Delta',n.Delta,'maxiter',n.maxiter);
CHI = struct('chi0',c.chi0,'chi1',c.chi1,'a_bar',c.a_bar,'fixcost',c.fixcost,'fixcost2',c.fixcost2);
results = struct('prvname',r.prvname,'rb',r.rb,'rah',r.rah,'w',r.w,'rb_gap',r.rb_gap, ...
    'tau',r.tau,'Tt',r.Tt,'Ct',r.Ct,'At',r.At,'Bt',r.Bt,'Lt',r.Lt, ...
    'Zt',r.Zt,'Kt',r.Kt,'Kt0',r.Kt0,'alpha',r.alpha,'wjt',r.wjt);
manifest = HANK_2ASSETS_HJB(param,grid,num,CHI,results,0);
end

function ledger = complete_zero_ledger()
ledger = struct('wrapper_smoke_batches',1,'HANK_2ASSETS_HJB_calls',0, ...
    'HJB_calls',0,'KFE_calls',0,'scientific_household_calls',0, ...
    'standalone_python_household_calls',0,'standalone_python_HJB_calls',0, ...
    'standalone_python_KFE_calls',0,'modular_python_HJB_calls',0, ...
    'modular_python_KFE_calls',0,'matlab_local_policy_reruns',0, ...
    'python_local_policy_reruns',0,'matlab_scalar_reruns',0, ...
    'exact_junction_smoke_reruns',0,'multi_province_calls',0, ...
    'stationary_calls',0,'second_province_household_calls',0, ...
    'MP2_calls',0,'MP3_calls',0,'annual_batch_calls',0,'shocks_calls',0, ...
    'transition_calls',0,'dynamics_calls',0,'IRF_calls',0,'R5_calls',0,'Results_calls',0);
end

function value = normalize_root(value)
value = lower(replace(string(value),'/','\'));
value = strip(value,'right','\');
end
function tf = root_allowed(candidate,allowed)
tf = any(normalize_root(candidate) == allowed);
end
function evidence = verify_exact_junction()
command = ['powershell.exe -NoProfile -NonInteractive -Command ' ...
    '"$i=Get-Item -LiteralPath ''C:\MatlabProgram'' -Force;' ...
    '$t=@($i.Target);' ...
    'if($i.LinkType -eq ''Junction'' -and $t.Count -eq 1 -and ' ...
    '[IO.Path]::GetFullPath([string]$t[0]).TrimEnd(''\'') -ieq ''D:\MatlabProgram'')' ...
    '{[Console]::Out.Write(''PASS'');exit 0};exit 17"'];
[status,out] = system(command);
if status ~= 0 || ~strcmp(strtrim(out),'PASS')
    error('MP4B:SourceBinding','exact C-to-D junction verification failed');
end
evidence = struct('logical_storage_root','C:\MatlabProgram','link_type','Junction', ...
    'target_count',1,'sole_target','D:\MatlabProgram');
end
function persist_new_json(path,payload)
reserved = java.io.File(char(path));
if ~reserved.createNewFile()
    error('MP4B:NoOverwrite','cannot atomically reserve manifest');
end
encoded = [jsonencode(payload,'PrettyPrint',true),newline];
fid = fopen(path,'w');
if fid < 0
    error('MP4B:Persistence','cannot open reserved empty manifest');
end
try
    count = fwrite(fid,encoded,'char');
    close_status = fclose(fid);
catch write_error
    fclose(fid);
    rethrow(write_error);
end
if count ~= numel(encoded) || close_status ~= 0
    error('MP4B:Persistence','manifest write or durable close was incomplete');
end
end
function out = file_sha256(path)
md = java.security.MessageDigest.getInstance('SHA-256');
fid = fopen(path,'r');
if fid < 0; error('MP4B:Read','cannot read source'); end
cleanup = onCleanup(@() fclose(fid));
md.update(fread(fid,Inf,'*uint8'));
out = lower(reshape(dec2hex(typecast(md.digest(),'uint8'))',1,[]));
end
