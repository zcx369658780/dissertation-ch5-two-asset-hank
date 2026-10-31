% R12 fixed-input source assembly only. No HANK entry or linear solve.
fprintf('ENTERED_MATLAB_USER_SCRIPT\n');
root=fileparts(fileparts(fileparts(mfilename('fullpath'))));
task='CH5_TEMP31_R6_R3_R2_R12_R8_EXE_FIXED_INPUT_OPERATOR_PARITY_20261031';
local=fullfile(root,'tasks',task,'LOCAL_ONLY');
expected_prefdir=fullfile(local,'prefdir');
actual_prefdir=prefdir;
prefdir_match=strcmpi(strrep(actual_prefdir,'/','\'),strrep(expected_prefdir,'/','\'));
if ~prefdir_match; error('R12_PREFDIR_MISMATCH'); end
fprintf('PREFDIR_MATCH\n');
release=version('-release'); runtime_version=version;
if ~strcmp(release,'2022b'); error('R12_RELEASE_MISMATCH'); end
fprintf('RELEASE_R2022b_MATCH\n');
output=struct('release',release,'version',runtime_version,'prefdir_match',prefdir_match,'complete',false);
fixtures=cell(1,2); names={'BB','AAH','Bswitch','A'};
fields={'b_backward','b_forward','a_backward','a_forward'};
for q=1:2
 input_path=fullfile(local,sprintf('fixture_%d.json',q));
 f=fopen(input_path,'rb'); if f<0; error('R12_INPUT_OPEN'); end
 raw=fread(f,1025,'*uint8')'; fclose(f);
 expected_bytes=[415,516];
 if numel(raw)~=expected_bytes(q); error('R12_INPUT_BYTES'); end
 data=jsondecode(char(raw)); shp=double(data.shape(:)');
 if q==1; expected_shape=[2,2,2]; else; expected_shape=[3,2,2]; end
 if ~isequal(shp,expected_shape) || ~strcmp(data.flatten_order,'F') || ~strcmp(data.dtype,'float64'); error('R12_INPUT_SHAPE'); end
 I=shp(1); J=shp(2); Nz=shp(3); M=prod(shp); arrays=cell(1,4); inputs_F=struct();
 for fi=1:4
  x=double(data.(fields{fi})(:));
  if numel(x)~=M || any(~isfinite(x)); error('R12_NONFINITE_INPUT'); end
  arrays{fi}=reshape(x,shp); inputs_F.(fields{fi})=arrays{fi}(:)';
 end
 BB=axis_operator(arrays{1},arrays{2},1);
 AAH=axis_operator(arrays{3},arrays{4},2);
 Bswitch=kron(sparse(double(data.switch_matrix)),speye(I*J));
 A=BB+AAH+Bswitch;
 vector=double(data.vector(:));
 matrices={BB,AAH,Bswitch,A}; saved=struct();
 for ni=1:4
  G=matrices{ni}; [rr,cc,vv]=find(G);
  if any(~isfinite(nonzeros(G))); error('R12_MATRIX_NONFINITE'); end
  saved.(names{ni})=struct('shape',[M,M],'stored_nnz',nnz(G), ...
   'rows1',rr(:)','cols1',cc(:)','values',vv(:)', ...
   'dense_F',full(G(:))','matvec',full(G*vector)','row_sums',full(sum(G,2))');
 end
 mapping0=zeros(M,4);
 for k=0:M-1
  i=mod(k,I); j=mod(floor(k/I),J); z=floor(k/(I*J));
  mapping0(k+1,:)=[k,i,j,z];
 end
 fixtures{q}=struct('fixture_id',data.fixture_id,'shape',shp,'input_raw_bytes',double(raw), ...
  'inputs_F',inputs_F,'mapping0',mapping0,'matrices',saved);
 fprintf('FIXTURE_%d_ASSEMBLED\n',q);
end
output.fixtures=[fixtures{:}]; output.complete=true;
out=fullfile(local,'matlab_output.json');
if exist(out,'file'); error('R12_OUTPUT_EXISTS'); end
f=fopen(out,'w'); if f<0; error('R12_OUTPUT_OPEN'); end
fprintf(f,'%s',jsonencode(output)); fclose(f);
fprintf('R12_NATIVE_OPERATOR_ASSEMBLY_PASS\n');

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
