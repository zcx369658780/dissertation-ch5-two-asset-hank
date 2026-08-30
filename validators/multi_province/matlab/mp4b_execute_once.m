function mp4b_execute_once(protected_root,physical_protected_root,run_root,canonical_sha256)
% One-shot validation runner. Error persistence adds observability only.
prepared=mp4b_build_source_prepared_state();
profile clear;
profile on;
try
    mp4b_calendar2009_stationary_wrapper(protected_root,physical_protected_root,run_root,canonical_sha256,prepared);
    profile off;
    info=profile('info');
    counts=extract_counts(info);
    terminal=struct('status','COMPLETED','household_call_count',counts.household, ...
        'outer_turn_call_count',counts.outer_turn);
    write_terminal(run_root,terminal,info);
catch ME
    profile off;
    info=profile('info');
    counts=extract_counts(info);
    if isfolder(run_root)
        failure=struct('identifier',ME.identifier,'message',ME.message, ...
            'report',getReport(ME,'extended','hyperlinks','off'), ...
            'household_call_count',counts.household, ...
            'outer_turn_call_count',counts.outer_turn);
        save(fullfile(run_root,'matlab_terminal_failure.mat'),'failure');
        fid=fopen(fullfile(run_root,'matlab_terminal_failure.json'),'w');
        if fid>=0
            fprintf(fid,'%s\n',jsonencode(failure)); fclose(fid);
        end
    end
    rethrow(ME);
end
end

function counts=extract_counts(info)
counts=struct('household',0,'outer_turn',0);
for i=1:numel(info.FunctionTable)
    name=info.FunctionTable(i).FunctionName;
    if endsWith(name,'HANK_2ASSETS_HJB'); counts.household=counts.household+info.FunctionTable(i).NumCalls; end
    if endsWith(name,'HANK_mp_1turn'); counts.outer_turn=counts.outer_turn+info.FunctionTable(i).NumCalls; end
end
end

function write_terminal(run_root,terminal,info)
save(fullfile(run_root,'matlab_profile_summary.mat'),'terminal','info');
fid=fopen(fullfile(run_root,'matlab_terminal_status.json'),'w');
if fid>=0; fprintf(fid,'%s\n',jsonencode(terminal)); fclose(fid); end
end
