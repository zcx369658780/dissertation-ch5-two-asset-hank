function matlab_trajectory(manifest_path, initialization_path, output_dir, designated_root, max_updates)
% MATLAB_SOURCE_EXTRACTED_CONVERGED_HJB_PARITY
% Source extraction: HANK_2ASSETS_HJB.m lines 2-261; stops before KFE.
if max_updates~=1; error('update budget'); end
if exist(output_dir,'dir'); error('output directory exists'); end
mkdir(output_dir);
ledger=struct('invocations_entered',0,'iterations_entered',0,'solves_entered',0,'completed_updates',0,'converged',false,'status','INITIALIZING');
write_ledger(output_dir,ledger); started=tic;
addpath(designated_root);
m=jsondecode(fileread(manifest_path)); s=m.scalar_binding; p=s.parameters; n=s.numerics; switch_matrix=s.switch_matrix;
init=load(initialization_path);
required={'b','ah','z','v0','l0'};
for q=1:numel(required)
    if ~isfield(init,required{q}) || ~isa(init.(required{q}),'double') || ~isreal(init.(required{q})) || any(~isfinite(init.(required{q})(:)))
        error('exact-MAT common-input field invalid')
    end
end
b=init.b; ah=init.ah; z=init.z;
if ~isequal(size(b),[1,20]) || ~isequal(size(ah),[1,20]) || ~isequal(size(z),[1,2]) || ~isequal(size(init.v0),[20,20,2]) || ~isequal(size(init.l0),[20,20,2])
    error('exact-MAT common-input shape invalid')
end
required_scalars={'r_a','r_b','borrowing_rate_gap','tau','wage','transfer_income','rho','gamma_c','phi','chi_0','chi_1','a_bar','labor_weight'};
for q=1:numel(required_scalars); if ~isfield(p,required_scalars{q}) || ~isscalar(p.(required_scalars{q})) || ~isfinite(p.(required_scalars{q})); error('scalar binding invalid'); end; end
required_numerics={'delta','convergence_tolerance','drift_tolerance'};
for q=1:numel(required_numerics); if ~isfield(n,required_numerics{q}) || ~isscalar(n.(required_numerics{q})) || ~isfinite(n.(required_numerics{q})); error('numeric binding invalid'); end; end
if ~isequal(size(switch_matrix),[2,2]); error('switch binding invalid'); end
initial_value=init.v0; l0=init.l0;
I=numel(b); J=numel(ah); Nz=numel(z);
db=b(2)-b(1); dah=ah(2)-ah(1);
[bbb,aaah,zzz]=ndgrid(b,ah,z);
Rb=p.r_b.*(bbb>=0)+(p.r_b+p.borrowing_rate_gap).*(bbb<0);
raah=p.r_a.*(1-0.1*(ah(end)./ah).^(-9)); raah(1)=p.r_a;
Rah=repmat(reshape(raah,1,J,1),I,1,Nz);
l0=init.l0; v=init.v0; initial_value=init.v0;
chi=struct('chi0',p.chi_0,'chi1',p.chi_1,'fixcost',0,'fixcost2',0,'a_bar',p.a_bar);
results=struct(); Bswitch=kron(sparse(switch_matrix),speye(I*J)); converged=false; dist=Inf;
ledger.invocations_entered=1; ledger.status='RUNNING'; write_ledger(output_dir,ledger);
try
for iter=1:max_updates
    if toc(started)>2650; error('trajectory wall budget'); end
    output_path=fullfile(output_dir,sprintf('step_%04d.mat',iter));
    ledger.iterations_entered=ledger.iterations_entered+1; write_ledger(output_dir,ledger);
    V=v; initial_value=V;
    VbF=zeros(I,J,Nz); VbB=zeros(I,J,Nz); VahF=zeros(I,J,Nz); VahB=zeros(I,J,Nz);
    VbF(1:I-1,:,:)=(V(2:I,:,:)-V(1:I-1,:,:))/db;
    VbF(I,:,:)=((1-p.tau)*p.wage.*zzz(I,:,:).*l0(I,:,:)+p.transfer_income+Rb(I,:,:).*bbb(I,:,:)).^(-p.gamma_c);
    VbB(2:I,:,:)=(V(2:I,:,:)-V(1:I-1,:,:))/db;
    VbB(1,:,:)=((1-p.tau)*p.wage.*zzz(1,:,:).*l0(1,:,:)+p.transfer_income+Rb(1,:,:).*bbb(1,:,:)).^(-p.gamma_c);
    VahF(:,1:J-1,:)=(V(:,2:J,:)-V(:,1:J-1,:))/dah;
    VahB(:,2:J,:)=(V(:,2:J,:)-V(:,1:J-1,:))/dah;
    raw_VbF=VbF; raw_VbB=VbB; raw_VahF=VahF; raw_VahB=VahB;
    C_B=max(VbB,1e-6).^(-1/p.gamma_c); C_F=max(VbF,1e-6).^(-1/p.gamma_c);
    C_0=(1-p.tau)*p.wage.*zzz.*l0+p.transfer_income+Rb.*bbb;
    l_B=(max(VbB,1e-6)*(1-p.tau)*p.wage.*zzz/p.labor_weight).^(1/p.phi);
    l_F=(max(VbF,1e-6)*(1-p.tau)*p.wage.*zzz/p.labor_weight).^(1/p.phi);
    sc_B=(1-p.tau)*p.wage.*zzz.*l_B+p.transfer_income+Rb.*bbb-C_B;
    sc_F=(1-p.tau)*p.wage.*zzz.*l_F+p.transfer_income+Rb.*bbb-C_F;
    Ic_B=sc_B < -n.drift_tolerance; Ic_F=(sc_F > n.drift_tolerance).*(1-Ic_B); Ic_0=1-Ic_F-Ic_B;
    C=C_F.*Ic_F+C_B.*Ic_B+C_0.*Ic_0; l=l_F.*Ic_F+l_B.*Ic_B+l0.*Ic_0;
    u=C.^(1-p.gamma_c)./(1-p.gamma_c)-p.labor_weight*l.^(1+p.phi)./(1+p.phi);
    dhBB=HANK3_FOC(results,chi,VahB,VbB,aaah,0); dhBF=HANK3_FOC(results,chi,VahF,VbB,aaah,0);
    dhFB=HANK3_FOC(results,chi,VahB,VbF,aaah,0); dhFF=HANK3_FOC(results,chi,VahF,VbF,aaah,0);
    dh_B=(dhBF>0).*dhBF+(dhBB<0).*dhBB; dh_B(:,1,:)=(dhBF(:,1,:)>n.drift_tolerance).*dhBF(:,1,:);
    dh_B(:,J,:)=(dhBB(:,J,:)<-n.drift_tolerance).*dhBB(:,J,:); dh_B(1,1,:)=max(dh_B(1,1,:),0);
    dh_F=(dhFF>0).*dhFF+(dhFB<0).*dhFB; dh_F(:,1,:)=(dhFF(:,1,:)>n.drift_tolerance).*dhFF(:,1,:);
    dh_F(:,J,:)=(dhFB(:,J,:)<-n.drift_tolerance).*dhFB(:,J,:);
    sdh_B=-dh_B-HANK3_cost(results,chi,dh_B,aaah,0); sdh_F=-dh_F-HANK3_cost(results,chi,dh_F,aaah,0);
    Idh_F=sdh_F>n.drift_tolerance; Idh_B=(sdh_B<-n.drift_tolerance).*(1-Idh_F);
    Idh_B(1,:,:)=0; Idh_F(I,:,:)=0; Idh_B(I,:,:)=1;
    bbB=-(Ic_B.*sc_B+Idh_B.*sdh_B)/db; bbF=(Ic_F.*sc_F+Idh_F.*sdh_F)/db;
    dhB=Idh_B.*dhBB+Idh_F.*dhFB; dhF=Idh_B.*dhBF+Idh_F.*dhFF;
    MhB=min(dhB,0); MhF=max(dhF,0)+Rah.*aaah; MhB(:,J,:)=dhB(:,J,:)+Rah(:,J,:)*ah(end); MhF(:,J,:)=0;
    aaB=-MhB/dah; aaF=MhF/dah;
    BB=axis_operator(bbB,bbF,1); AAH=axis_operator(aaB,aaF,2); A=BB+AAH+Bswitch;
    matrix=(1/n.delta+p.rho)*speye(I*J*Nz)-A;
    rhs=u(:)+V(:)/n.delta; ledger.solves_entered=ledger.solves_entered+1; write_ledger(output_dir,ledger); updated=reshape(matrix\rhs,[I,J,Nz]);
    dist=max(abs(updated-v),[],'all'); v=updated;
    dh=Idh_B.*dh_B+Idh_F.*dh_F;
    adjustment_cost=HANK3_cost(results,chi,dh,aaah,0);
    mu_b=(1-p.tau)*p.wage.*zzz.*l+Rb.*bbb+p.transfer_income-dh-adjustment_cost-C;
    mu_a=dh+Rah.*aaah;
    liquid_label=double(Ic_F)-double(Ic_B); transfer_label=double(Idh_F)-double(Idh_B);
    save(output_path,'initial_value','l0','b','ah','z','raw_VbF','raw_VbB','raw_VahF','raw_VahB', ...
        'VbF','VbB','VahF','VahB','Ic_B','Ic_F','Ic_0','Idh_B','Idh_F','C','l','dh','adjustment_cost','Rah','mu_a','mu_b','u', ...
        'bbB','bbF','aaB','aaF','BB','AAH','Bswitch','A','matrix','rhs','updated','dist','liquid_label','transfer_label','-v7');
    core=load(output_path,'matrix','rhs','updated');
    if ~isequal(size(core.matrix),[800 800]) || ~isequal(size(core.rhs),[800 1]) || ~isequal(size(core.updated),[20 20 2]) || ~isequal(core.matrix,matrix) || ~isequal(core.rhs,rhs) || ~isequal(core.updated,updated); error('core stage readback invalid'); end
    updated_vec=updated(:); residual_inf=norm(matrix*updated_vec-rhs,inf);
    save(output_path,'updated_vec','residual_inf','-append');
    ledger.completed_updates=ledger.completed_updates+1;
    finite=all(isfinite([V(:);updated(:);rhs(:);C(:);l(:);dh(:);adjustment_cost(:);Rah(:);mu_a(:);mu_b(:);u(:);bbB(:);bbF(:);aaB(:);aaF(:);nonzeros(A);nonzeros(matrix)]));
    ledger.statistic=dist; ledger.converged=finite && dist<n.convergence_tolerance;
    trace=struct('iteration',iter,'statistic',dist,'finite',finite,'converged',ledger.converged,'diagnostic_continuation',iter>100,'value_min',min(updated(:)),'value_max',max(updated(:)));
    f=fopen(fullfile(output_dir,'trace.jsonl'),'a'); fprintf(f,'%s\n',jsonencode(trace)); fclose(f);
    write_ledger(output_dir,ledger); fprintf('STEP %d statistic %.17g\n',iter,dist);
    if ~finite; ledger.status='NONFINITE'; break; end
    if ledger.converged; ledger.status='CONVERGED'; break; end
end
if strcmp(ledger.status,'RUNNING'); ledger.status='MAX_UPDATES'; end
catch ME
    ledger.status='FAILED'; ledger.error=ME.message; write_ledger(output_dir,ledger); rethrow(ME);
end
write_ledger(output_dir,ledger);
end

function write_ledger(output_dir,ledger)
f=fopen(fullfile(output_dir,'ledger.json'),'w'); fprintf(f,'%s',jsonencode(ledger)); fclose(f);
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
