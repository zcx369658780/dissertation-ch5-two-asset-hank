function matlab_solve(payload,output_dir)
% One frozen sparse system, exact reference bits checked before one backslash.
if exist(output_dir,'dir'); error('output already exists'); end
mkdir(output_dir);
ledger=struct('invocations_entered',1,'solves_entered',0,'solves_completed',0,'durable_outputs',0,'status','LOADING');
persist(output_dir,ledger);
try
    m=load(payload); M=m.M; rhs=m.rhs;
    assert(issparse(M) && isa(M,'double') && isequal(size(M),[800,800]));
    assert(isa(rhs,'double') && isequal(size(rhs),[800,1]));
    [r,c,d]=find(M); [~,order]=sortrows([r,c],[1,2]);r=r(order);c=c(order);d=d(order);
    assert(isequal(int64(r),m.ref_row) && isequal(int64(c),m.ref_col));
    assert(isequal(typecast(d(:),'uint64'),m.ref_data_bits(:)));
    assert(isequal(typecast(rhs(:),'uint64'),m.ref_rhs_bits(:)));
    assert(all(isfinite(d)) && all(isfinite(rhs)));
    save(fullfile(output_dir,'loaded_input.mat'),'M','rhs','-v7');
    receipt=struct('exact_payload_bits_and_support',true,'format','MATLAB sparse','dtype','double','shape',[800,800], ...
        'rhs_shape',[800,1],'version',version,'computer',computer,'solver_entrypoint','M backslash rhs; no option overrides', ...
        'backend_observation','MATLAB version and BLAS/LAPACK strings observed; sparse factorization backend not instrumented');
    receipt.blas=version('-blas');receipt.lapack=version('-lapack');
    f=fopen(fullfile(output_dir,'loaded_receipt.json'),'w');fprintf(f,'%s',jsonencode(receipt));fclose(f);
    ledger.status='SOLVING';ledger.solves_entered=1;persist(output_dir,ledger);
    lastwarn('');started=tic;
    x=M\rhs;
    save(fullfile(output_dir,'solution.mat'),'x','-v7');
    ledger.solves_completed=1;ledger.durable_outputs=1;ledger.solve_seconds=toc(started);
    ledger.status='COMPLETE';ledger.finite=all(isfinite(x));persist(output_dir,ledger);
    [message,id]=lastwarn;
    f=fopen(fullfile(output_dir,'warnings.json'),'w');fprintf(f,'%s',jsonencode(struct('last_warning',message,'last_warning_id',id,'all_console_warnings','see process log')));fclose(f);
catch ME
    ledger.status='FAILED';ledger.error=ME.message;persist(output_dir,ledger);rethrow(ME);
end
end
function persist(output_dir,ledger)
f=fopen(fullfile(output_dir,'ledger.json'),'w');fprintf(f,'%s',jsonencode(ledger));fclose(f);
end
