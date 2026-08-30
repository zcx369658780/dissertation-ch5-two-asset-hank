function mp4b_write_presolver_manifest(canonical_path, output_path)
% Write a source-literal prepared-state manifest only; never run a solver.
if isfile(output_path)
    error('MP4B:NoOverwrite','manifest already exists');
end
canonical=jsondecode(fileread(canonical_path));
prepared=mp4b_build_source_prepared_state();
manifest.schema='CH5_MP4B_PRESOLVER_MANIFEST_V1';
manifest.canonical_sha256='507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48';
manifest.binding=canonical.binding;
manifest.province_order=canonical.province_order;
hash_values=struct2cell(canonical.source_hashes);
manifest.source_hashes=struct('filled_workbook',hash_values{1}, ...
    'regression_workbook',hash_values{2},'distance_workbook',hash_values{3});
manifest.scalars=canonical.scalars;
manifest.vectors=canonical.vectors;
manifest.matrices=canonical.matrices;
manifest.param=prepared.param;
manifest.grid=prepared.grids{1};
manifest.num=prepared.num;
manifest.CHI=prepared.CHI;
manifest.init=prepared.inits{1};
manifest.province_count=numel(prepared.inits);
fid=fopen(output_path,'w');
if fid<0; error('MP4B:NoOverwrite','cannot create manifest'); end
cleanup=onCleanup(@() fclose(fid));
fprintf(fid,'%s\n',jsonencode(manifest));
end
