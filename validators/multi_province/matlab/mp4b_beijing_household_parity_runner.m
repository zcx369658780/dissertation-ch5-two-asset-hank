function summary = mp4b_beijing_household_parity_runner(run_root,contract_path,logical_root,physical_root)
% Exactly one accepted-wrapper call; the wrapper creates the fresh run root.
summary = mp4b_beijing_household_wrapper('run',run_root,contract_path,logical_root,physical_root);
full_path = fullfile(run_root,'matlab_household_full.mat');
if isfile(full_path) || ~java.io.File(char(full_path)).createNewFile()
    error('MP4B:NoOverwrite','cannot reserve MATLAB full result');
end
save(full_path,'summary','-v7.3');
compact = struct('schema','MP4B_BEIJING_MATLAB_HOUSEHOLD_RESULT_V1', ...
    'wrapper_calls',1,'HANK_2ASSETS_HJB_calls',1,'converged',logical(summary.convergent), ...
    'aggregates',struct('Ct',summary.Ct,'Lt',summary.Lt,'At',summary.At, ...
    'Bt',summary.Bt,'At_plus_Bt',summary.At+summary.Bt), ...
    'AtTax',summary.AtTax,'full_result_path',full_path);
persist_new_json(fullfile(run_root,'matlab_household_summary.json'),compact);
summary = compact;
end
function persist_new_json(path,payload)
if ~java.io.File(char(path)).createNewFile(); error('MP4B:NoOverwrite','cannot reserve JSON'); end
encoded=[jsonencode(payload,'PrettyPrint',true),newline]; fid=fopen(path,'w');
if fid<0; error('MP4B:Persistence','cannot open reserved JSON'); end
try
    count=fwrite(fid,encoded,'char');
    status=fclose(fid);
catch err
    fclose(fid);
    rethrow(err);
end
if count~=numel(encoded) || status~=0; error('MP4B:Persistence','incomplete JSON write'); end
end
