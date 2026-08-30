function prepared = mp4b_build_source_prepared_state()
% Validation-only literal extraction from multi_prov_HANK_12sts.m.
% This function constructs inputs only and never invokes a model.

num.maxit=100; num.crit=1e-7; num.reg_threshold=1e-9;
num.homecrit=1e-2; num.Delta=1000; num.maxiter=100;
num.max2iter=200; num.max3iter=500;

CHI.chi0=0.1; CHI.chi1=2; CHI.a_bar=1e-6;
CHI.fixcost=0; CHI.fixcost2=0;

grid.I=20; grid.bmin=-2; grid.bmax=5;
grid.J=20; grid.amin=0; grid.amax=10;
grid.Nz=2; grid.zmin=0.8; grid.zmax=1.3;
grid.z=linspace(grid.zmin,grid.zmax,grid.Nz);
grid.la_mat=ones(grid.Nz,grid.Nz)*(1/3/(grid.Nz-1)) ...
    + eye(grid.Nz,grid.Nz)*(-1/3-1/3/(grid.Nz-1));
grid.ramax=0.09; grid.ramin=0.02;
grid.wjtmax=1.3; grid.wjtmin=0.8;

param.ga=2; param.phi_l=5; param.alphal=1; param.alphap=1;
param.frisch_l=0.2; param.rho=0.05; param.rho_pi=1.25;
param.epsilon=10; param.theta=100; param.delta=0.025;
param.istar=0.015; param.pistar=0.0075;
param.max_phi=0.3; param.max_sigmau=0.5;
param.smooth_method=0; param.reg_method=0;
param.GDP_multiplier=1000; param.POP_multiplier=100;
param.Ztratio=1; param.GovInv_ratio=1;

init.alpha=0.6; init.rb_gap=0.07; init.rah=0.09; init.ra=0.09;
init.it=0.02; init.rb=0.02; init.rk=0.1; init.wjt=0.6;
init.w=20; init.Tt=0.1; init.Zt=6; init.pit=0.02;
init.pit_1=0.02; init.totalpit=0.02; init.epsilon_pi=0;
init.tau=0.05; init.At=2; init.Bt=1; init.mt=0.9;
init.Lt=0.8; init.Ct=4; init.GovInv=1000;
init.GovSurplus=0; init.inter_prv_ratio=0.5;
init.Lt_mat=zeros(31,31); init.corptau=0.25;

grids=cell(1,31); inits=cell(1,31);
for i=1:31
    grids{i}=grid; inits{i}=init;
end
prepared=struct('param',param,'grids',{grids},'num',num,'CHI',CHI,'inits',{inits});
end
