function mp4b_initial_labor_scalar_diagnostic(output_json, protected_root)
% Validation-only: eight predeclared scalar lab_solve2/fzero calls, no model entry.
if exist(output_json,'file') || exist(fileparts(output_json),'dir') ~= 7
    error('MP4B:NoOverwrite','Output must be a new file in an existing fresh directory.');
end
lab_path = fullfile(protected_root,'lab_solve2.m');
expected = '74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20';
actual_bytes = System.Security.Cryptography.HashAlgorithm.Create('SHA256').ComputeHash(System.IO.File.ReadAllBytes(lab_path));
actual = reshape(dec2hex(uint8(actual_bytes),2).',1,[]);
if ~strcmpi(actual,expected), error('MP4B:SourceIdentity','lab_solve2 identity mismatch.'); end
addpath(protected_root);
b = [-2, 4/19]; a = [0,10]; z = [0.8,1.3];
template=struct('i',0,'j',0,'k',0,'b',0,'a',0,'z',0,'Rb',0,'raah',0, ...
    'tempMat',0,'B',0,'x0',0,'l0',0,'fval',0,'exitflag',0,'root_base',0);
rows=repmat(template,1,8); n=0; options=optimset('Display','off');
for iz=1:2
    for ia=1:2
        for ib=1:2
            n=n+1; bb=b(ib); aa=a(ia); zz=z(iz);
            rb=0.02+0.07*(bb<0);
            if aa==0, raah=0.09; else, raah=0.09*(1-0.1*(10/aa)^(-9)); end
            temp=raah^2+rb*bb+0.1; B=(1-0.05)*20*zz;
            params=[1,1,0.05,20,zz,0.2,temp,2];
            x0=B^(0.2*(1-2)/(1+2*0.2));
            [l0,fval,exitflag]=fzero(@(l) lab_solve2(l,params),x0,options);
            rows(n)=struct('i',ib,'j',ia,'k',iz,'b',bb,'a',aa,'z',zz,'Rb',rb, ...
                'raah',raah,'tempMat',temp,'B',B,'x0',x0,'l0',l0,'fval',fval, ...
                'exitflag',exitflag,'root_base',B*l0+temp);
        end
    end
end
payload=struct('schema','CH5_MP4B_INITIAL_LABOR_SCALAR_DIAGNOSTIC_V1', ...
    'protected_root',protected_root,'lab_solve2_sha256',expected, ...
    'cell_count',n,'stationary_model_calls',0,'cells',rows);
output_file=java.io.File(output_json);
if ~output_file.createNewFile()
    error('MP4B:NoOverwrite','Could not reserve a new output file exclusively.');
end
fid=fopen(output_json,'w');
if fid<0, error('MP4B:Persistence','Could not open the newly reserved output file.'); end
cleanup=onCleanup(@() fclose(fid)); fwrite(fid,jsonencode(payload),'char');
end
