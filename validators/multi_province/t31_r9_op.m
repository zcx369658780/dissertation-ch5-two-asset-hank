% R9: fixed synthetic source-anchored assembly only.
emit('ENTERED_MATLAB_USER_SCRIPT',struct());
expected=getenv('MATLAB_PREFDIR'); actual=prefdir;
same=strcmpi(regexprep(strrep(actual,char(92),'/'),'/+$',''),regexprep(strrep(expected,char(92),'/'),'/+$',''));
p=struct('actual_prefdir',actual,'expected_prefdir',expected,'equals_expected',logical(same));
if ~same; emit('PREFDIR_MISMATCH',p); error('TEMP31:PREFDIR_MISMATCH','PREFDIR_MISMATCH'); end
emit('PREFDIR_MATCH',p);
v=version; r=version('-release'); emit('MATLAB_VERSION',struct('version',v,'release',r));
assert(strcmp(r,'2022b'),'UNEXPECTED_MATLAB_RELEASE');
root=fileparts(expected); local=fileparts(fileparts(root));
for q=1:2
    input_path=fullfile(local,sprintf('fixture_%d.json',q));
    f=fopen(input_path,'rb'); assert(f~=-1,'INPUT_OPEN');
    fixture_input_bytes=fread(f,Inf,'*uint8')'; assert(fclose(f)==0,'INPUT_CLOSE');
    x=jsondecode(native2unicode(fixture_input_bytes,'UTF-8'));
    shp=double(x.shape(:)'); I=shp(1); J=shp(2); Nz=shp(3); M=I*J*Nz;
    if q==1; assert(isequal(shp,[2 2 2]) && M==8,'SHAPE1'); else; assert(isequal(shp,[3 2 2]) && M==12,'SHAPE2'); end
    assert(strcmp(x.fixture_id,sprintf('fixture_%d',q)),'FIXTURE_ID');
    b_backward=reshape(double(x.b_backward),shp); b_forward=reshape(double(x.b_forward),shp);
    a_backward=reshape(double(x.a_backward),shp); a_forward=reshape(double(x.a_forward),shp);
    switch_matrix=double(x.switch_matrix); vector=double(x.vector(:));
    assert(isequal(size(switch_matrix),[2 2]) && numel(vector)==M,'INPUT_DIM');
    assert(all(isfinite([b_backward(:);b_forward(:);a_backward(:);a_forward(:);switch_matrix(:);vector(:)])),'INPUT_FINITE');
    BB=axis_operator(b_backward,b_forward,1);
    AAH=axis_operator(a_backward,a_forward,2);
    Bswitch=kron(sparse(switch_matrix),speye(I*J));
    A=BB+AAH+Bswitch;
    BB_mv=BB*vector; AAH_mv=AAH*vector; Bswitch_mv=Bswitch*vector; A_mv=A*vector;
    input_b_backward_F=b_backward(:); input_b_forward_F=b_forward(:);
    input_a_backward_F=a_backward(:); input_a_forward_F=a_forward(:);
    [ci,cj,cz]=ind2sub(shp,(1:M)'); index_table=[ci cj cz (1:M)'];
    output_path=fullfile(local,sprintf('matlab_fixture_%d.mat',q));
    assert(~exist(output_path,'file'),'OUTPUT_EXISTS');
    save(output_path,'BB','AAH','Bswitch','A','BB_mv','AAH_mv','Bswitch_mv','A_mv','vector','shp','fixture_input_bytes','input_b_backward_F','input_b_forward_F','input_a_backward_F','input_a_forward_F','index_table','-v7');
    emit(sprintf('FIXTURE_%d_DONE',q),struct('fixture_id',sprintf('fixture_%d',q),'states',M,'operators',4));
end
emit('OPERATOR_ASSEMBLY_DONE',struct('fixtures',2,'operators',8));
disp('TEMP31_R9_MATLAB_ASSEMBLY_DONE_NOT_YET_PARITY');
function emit(stage,data)
    expected=getenv('MATLAB_PREFDIR'); assert(~isempty(expected),'PREFDIR_ENV');
    root=fileparts(expected); token=getenv('TEMP31_RUN_NONCE'); assert(~isempty(token),'RUN_NONCE');
    rec=struct('task_id','CH5_TEMP31_R6_R3_R2_R9_FIXED_SMALL_OPERATOR_PARITY_20261031','run_token',token,'stage',stage,'utc',char(datetime('now','TimeZone','UTC','Format',"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'")),'data',data);
    tmp=fullfile(root,[stage '.partial']); dst=fullfile(root,[stage '.json']);
    assert(~exist(tmp,'file') && ~exist(dst,'file'),'MARKER_EXISTS');
    f=fopen(tmp,'w','n','UTF-8'); assert(f~=-1,'MARKER_OPEN');
    fprintf(f,'%s',jsonencode(rec)); assert(fclose(f)==0,'MARKER_CLOSE');
    [ok,~]=movefile(tmp,dst); assert(ok,'MARKER_RENAME');
end

function G=axis_operator(backward,forward,axis_number)
shape=size(backward); I=shape(1); J=shape(2); Nz=shape(3); M=I*J*Nz;
rows=[]; cols=[]; vals=[];
for nz=1:Nz
 for j=1:J
  for i=1:I
   row=i+(j-1)*I+(nz-1)*I*J; rb=backward(i,j,nz); rf=forward(i,j,nz); total=rb+rf;
   if rb~=0
    if (axis_number==1 && i>1); col=row-1; elseif (axis_number==2 && j>1); col=row-I; else; col=0; end
    if col>0; rows(end+1)=row; cols(end+1)=col; vals(end+1)=rb; end
   end
   if rf~=0
    if (axis_number==1 && i<I); col=row+1; elseif (axis_number==2 && j<J); col=row+I; else; col=0; end
    if col>0; rows(end+1)=row; cols(end+1)=col; vals(end+1)=rf; end
   end
   rows(end+1)=row; cols(end+1)=row; vals(end+1)=-total;
  end
 end
end
G=sparse(rows,cols,vals,M,M);
end
