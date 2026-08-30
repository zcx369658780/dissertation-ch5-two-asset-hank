function manifest=mp4b_path_equivalence_smoke(logical_root,physical_root,smoke_root)
% Infrastructure-only source-path smoke. No model or solver is invoked.
arguments
    logical_root (1,1) string
    physical_root (1,1) string
    smoke_root (1,1) string
end
if isfolder(smoke_root) || isfile(smoke_root)
    error('MP4B:NoOverwrite','smoke_root must not exist');
end
if ~isfolder(logical_root) || ~isfolder(physical_root)
    error('MP4B:PathEquivalence','verified protected roots must exist');
end
mkdir(smoke_root);
old_path=path; cleanup=onCleanup(@() path(old_path));
addpath(logical_root);
global N_prov; %#ok<GVMIS> source-faithful binding required by protected route
N_prov=31;
if ~isequal(N_prov,31); error('MP4B:SourceBinding','N_prov mismatch'); end
helpers={'load_GDPdata','load_distdata','mpHANK_equilibrium_2000', ...
    'HANK_mp_1eq','HANK_mp_1turn','HANK_2ASSETS_HJB'};
allowed=[normalize_root(logical_root),normalize_root(physical_root)];
resolved=cell(1,numel(helpers));
for i=1:numel(helpers)
    logical_file=fullfile(logical_root,helpers{i}+'.m');
    physical_file=fullfile(physical_root,helpers{i}+'.m');
    resolved{i}=which(helpers{i});
    if isempty(resolved{i}) || ~isfile(logical_file) || ~isfile(physical_file) ...
            || ~strcmp(fileread(logical_file),fileread(physical_file)) ...
            || ~any(normalize_root(string(fileparts(resolved{i}))) == allowed)
        error('MP4B:PathEquivalence','helper is outside exact verified root pair');
    end
end
manifest=struct('marker','MP4B_LOGICAL_PHYSICAL_PATH_EQUIVALENCE_SMOKE_PASS', ...
    'logical_protected_root',logical_root,'physical_protected_root',physical_root, ...
    'N_prov',N_prov,'helpers',{helpers},'resolved_helpers',{resolved}, ...
    'scientific_model_calls',0);
fid=fopen(fullfile(smoke_root,'path_equivalence_smoke_manifest.json'),'w');
if fid<0; error('MP4B:NoOverwrite','cannot create smoke manifest'); end
cleanup_file=onCleanup(@() fclose(fid));
fprintf(fid,'%s\n',jsonencode(manifest));
end

function value=normalize_root(value)
value=lower(replace(string(value),'/','\'));
value=strip(value,'right','\');
end
