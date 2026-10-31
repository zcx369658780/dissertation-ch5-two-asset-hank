% One minimal startup probe; first user statement atomically emits the entry marker.
emit('ENTERED_MATLAB_USER_SCRIPT',struct());
expected=getenv('MATLAB_PREFDIR'); actual=prefdir;
same=strcmpi(regexprep(strrep(actual,char(92),'/'),'/+$',''),regexprep(strrep(expected,char(92),'/'),'/+$',''));
p=struct('actual_prefdir',actual,'expected_prefdir',expected,'equals_expected',logical(same));
if ~same
    emit('PREFDIR_MISMATCH',p); error('TEMP31:PREFDIR_MISMATCH','PREFDIR_MISMATCH');
end
emit('PREFDIR_MATCH',p);
v=version; r=version('-release');
emit('MATLAB_VERSION',struct('version',v,'release',r));
assert(strcmp(r,'2022b'),'UNEXPECTED_MATLAB_RELEASE');
s=sparse(1,1,1,1,1);
assert(isequal(size(s),[1 1]) && nnz(s)==1 && full(s(1,1))==1,'SPARSE_SANITY_FAILED');
emit('SPARSE_PROBE_PASS',struct('rows',1,'cols',1,'nnz',1,'value',1));
disp('TEMP31_R7_RELEASED_MEMORY_TWO_GIB_MINIMAL_NATIVE_PROBE_PASS');
function emit(stage,data)
    expected=getenv('MATLAB_PREFDIR'); assert(~isempty(expected),'EXPECTED_PREFDIR_ENV_MISSING');
    root=fileparts(expected); assert(~isempty(root),'EXPECTED_RUNTIME_ROOT_MISSING');
    token=getenv('TEMP31_RUN_NONCE'); assert(~isempty(token),'RUN_NONCE_ENV_MISSING');
    rec=struct('task_id','CH5_TEMP31_R6_R3_R2_R7_RELEASED_MEMORY_TWO_GIB_NATIVE_20261031','run_token',token,'stage',stage,'utc',char(datetime('now','TimeZone','UTC','Format',"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'")),'data',data);
    tmp=fullfile(root,[stage '.partial']); dst=fullfile(root,[stage '.json']);
    assert(~exist(tmp,'file') && ~exist(dst,'file'),'MARKER_ALREADY_EXISTS');
    f=fopen(tmp,'w','n','UTF-8'); assert(f~=-1,'MARKER_OPEN_FAILED');
    fprintf(f,'%s',jsonencode(rec)); status=fclose(f); assert(status==0,'MARKER_CLOSE_FAILED');
    [ok,~]=movefile(tmp,dst); assert(ok,'MARKER_ATOMIC_RENAME_FAILED');
end
