function st = mp4b_calendar2009_stationary_wrapper(protected_root, physical_protected_root, run_root, canonical_sha256, prepared)
% Validation-only corrected calendar-2009 entry. Defining this function runs nothing.
% Source contract: load_GDPdata.m:74-137 and mpHANK_equilibrium_2000.m:22-72.

arguments
    protected_root (1,1) string
    physical_protected_root (1,1) string
    run_root (1,1) string
    canonical_sha256 (1,1) string
    prepared (1,1) struct
end

calendar_year = 2009;
analysis_index = 1;
data_year = 10;
data_MAT_index = 1;
regression_vintage_key = 10;

required = {'param','grids','num','CHI','inits'};
if ~all(isfield(prepared, required))
    error('MP4B:MissingPreparedState', 'prepared must explicitly supply param/grids/num/CHI/inits');
end
if strlength(canonical_sha256) ~= 64
    error('MP4B:CanonicalIdentity', 'canonical_sha256 must be an explicit SHA-256 identity');
end
if ~isfolder(protected_root) || ~isfolder(physical_protected_root)
    error('MP4B:ProtectedRoot', 'verified protected roots do not exist');
end
if isfolder(run_root) || isfile(run_root)
    error('MP4B:NoOverwrite', 'run_root must not already exist');
end
mkdir(run_root);

old_path = path;
cleanup = onCleanup(@() path(old_path));
addpath(protected_root);
global N_prov; %#ok<GVMIS> source-faithful binding required by protected route
N_prov = 31;
if ~isequal(N_prov,31)
    error('MP4B:SourceBinding','source-required global N_prov must equal 31');
end
required_helpers = {'load_GDPdata','load_distdata','mpHANK_equilibrium_2000', ...
    'HANK_mp_1eq','HANK_mp_1turn','HANK_2ASSETS_HJB'};
allowed_roots = [normalize_root(protected_root),normalize_root(physical_protected_root)];
for helper_index = 1:numel(required_helpers)
    resolved = which(required_helpers{helper_index});
    logical_file = fullfile(protected_root,[required_helpers{helper_index} '.m']);
    physical_file = fullfile(physical_protected_root,[required_helpers{helper_index} '.m']);
    if isempty(resolved) || ~isfile(logical_file) || ~isfile(physical_file) ...
            || ~strcmp(fileread(logical_file),fileread(physical_file)) ...
            || ~any(normalize_root(string(fileparts(resolved))) == allowed_roots)
        error('MP4B:SourceBinding','protected helper did not resolve under protected_root');
    end
end
param = prepared.param;
data_MAT = load_GDPdata(param.GDP_multiplier, param.POP_multiplier, 0.096, ...
    param.smooth_method, param.reg_method);
selected = data_MAT{data_MAT_index};

manifest.schema = 'CH5_MP4B_MATLAB_PRESOLVER_MANIFEST_V1';
manifest.calendar_year = calendar_year;
manifest.analysis_index = analysis_index;
manifest.workbook_data_row_index = data_year;
manifest.data_MAT_index = data_MAT_index;
manifest.output_filename_year = calendar_year;
manifest.regression_vintage_key = regression_vintage_key;
manifest.canonical_sha256 = canonical_sha256;
manifest.source_bindings = struct('N_prov',N_prov, ...
    'logical_protected_root',protected_root, ...
    'physical_protected_root',physical_protected_root, ...
    'path_binding','finite_verified_logical_physical_pair');
manifest.province_order = selected.prvname;
manifest.GDP = selected.GDP{4}(data_year,:);
manifest.CAP = selected.CAP{4}(data_year,:);
manifest.POP = selected.POP{4}(data_year,:);
manifest.log_pgdp = selected.log_pgdp{4}(data_year,:);
manifest.log_pcap = selected.log_pcap{4}(data_year,:);
manifest.IND_alpha = selected.IND_alpha{4}(1,:);
manifest.IND_Zt = selected.IND_Zt{4}(1,:);
manifest.required_trace_fields = {'Ct','Lt','At','Bt','AtTax','convergent', ...
    'Lt_mat','Lt_supply','Kt_supply','rah','Yt','Kt','mt','KNratio','wjt', ...
    'rk','ra','Govinc','w','rb','GovSurplus','controller_history'};

manifest_path = fullfile(run_root, 'matlab_presolver_manifest.json');
fid = fopen(manifest_path, 'w');
if fid < 0
    error('MP4B:NoOverwrite', 'cannot exclusively create pre-solver manifest');
end
close_manifest = onCleanup(@() fclose(fid));
fprintf(fid, '%s\n', jsonencode(manifest));
clear close_manifest;

% The protected annual wrapper is deliberately bypassed: it would pass ii=1 as data_year=1.
st = mpHANK_equilibrium_2000(param, prepared.grids, prepared.num, prepared.CHI, ...
    prepared.inits, selected, 4, data_year);

output_path = fullfile(run_root, 'matlab_calendar2009_stationary_output.mat');
if isfile(output_path)
    error('MP4B:NoOverwrite', 'stationary output already exists');
end
save(output_path, 'st', 'manifest', '-v7.3');
end

function value=normalize_root(value)
value=lower(replace(string(value),'/','\'));
value=strip(value,'right','\');
end
