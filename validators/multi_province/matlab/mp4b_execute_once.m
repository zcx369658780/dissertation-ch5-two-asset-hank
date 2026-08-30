function mp4b_execute_once(protected_root,run_root,canonical_sha256)
% One-shot validation runner. Error persistence adds observability only.
prepared=mp4b_build_source_prepared_state();
try
    mp4b_calendar2009_stationary_wrapper(protected_root,run_root,canonical_sha256,prepared);
catch ME
    if isfolder(run_root)
        failure=struct('identifier',ME.identifier,'message',ME.message, ...
            'report',getReport(ME,'extended','hyperlinks','off'));
        save(fullfile(run_root,'matlab_terminal_failure.mat'),'failure');
        fid=fopen(fullfile(run_root,'matlab_terminal_failure.json'),'w');
        if fid>=0
            fprintf(fid,'%s\n',jsonencode(failure)); fclose(fid);
        end
    end
    rethrow(ME);
end
end
