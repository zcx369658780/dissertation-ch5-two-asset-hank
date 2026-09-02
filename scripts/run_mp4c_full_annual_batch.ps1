param([ValidateRange(1,64)][int]$Workers=4,[string]$OutputRoot="",[string]$DataRoot="",[string]$RuntimeCache="",[string]$Python="python")
$ErrorActionPreference='Stop'
$repoRoot=(Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if ([string]::IsNullOrWhiteSpace($DataRoot)) {$DataRoot=Join-Path $repoRoot 'data_local\matlab_primary_source_snapshot'}
if ([string]::IsNullOrWhiteSpace($RuntimeCache)) {
    $runtimeCacheDir=Join-Path $repoRoot 'data_local\matlab_runtime_snapshot'
    $runtimeCacheCandidates=@(Get-ChildItem -LiteralPath $runtimeCacheDir -File | Where-Object {$_.Name -like '*_1000_100_0.mat'})
    if ($runtimeCacheCandidates.Count -ne 1) {throw "Expected exactly one *_1000_100_0.mat runtime cache under: $runtimeCacheDir"}
    $RuntimeCache=$runtimeCacheCandidates[0].FullName
}
if ([string]::IsNullOrWhiteSpace($OutputRoot)) {$stamp=Get-Date -Format 'yyyyMMdd-HHmmss';$OutputRoot="D:\ProjectTemp\ch5-mp4c-full-annual-batch-$stamp"}
if ((Test-Path -LiteralPath $OutputRoot) -and -not (Test-Path -LiteralPath (Join-Path $OutputRoot 'batch_manifest.json'))) {throw "Existing output root is not a resumable MP4C batch: $OutputRoot"}
$started=Get-Date;$cpu=Get-CimInstance Win32_Processor|Select-Object -First 1;$computer=Get-CimInstance Win32_ComputerSystem
Write-Host "Batch start: $($started.ToString('o'))";Write-Host "Python: $Python";Write-Host "Workers: $Workers";Write-Host 'Years: 2009-2023';Write-Host "Output root: $OutputRoot";Write-Host "Data root: $DataRoot";Write-Host "Runtime cache: $RuntimeCache";Write-Host "CPU: $($cpu.Name)";Write-Host "Installed RAM bytes: $($computer.TotalPhysicalMemory)"
& $Python (Join-Path $repoRoot 'validators\multi_province\mp4c_run_full_annual_batch.py') --data-root $DataRoot --runtime-cache $RuntimeCache --output-root $OutputRoot --workers $Workers
$exit=$LASTEXITCODE;$ended=Get-Date
if ($exit -eq 0 -and (Test-Path -LiteralPath (Join-Path $OutputRoot 'batch_timing.json'))) {Write-Host "Scientific batch wall clock is recorded in batch_timing.json"} else {Write-Host "Batch did not complete; no scientific timing claim is made."}
Write-Host "Total launcher wall clock: $(($ended-$started).TotalSeconds) seconds";Write-Host "Output root: $OutputRoot";exit $exit
