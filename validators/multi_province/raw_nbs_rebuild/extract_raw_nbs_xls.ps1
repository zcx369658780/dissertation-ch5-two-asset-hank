param(
    [Parameter(Mandatory = $true)][string]$SourceRoot,
    [Parameter(Mandatory = $true)][string]$OutputJson
)

$ErrorActionPreference = 'Stop'

$specs = @(
    @{ key = 'gdp'; file = '地区生产总值 亿元.xls'; indicator = '地区生产总值'; unit = '亿元' },
    @{ key = 'investment'; file = '固定资本形成总额 亿元.xls'; indicator = '固定资本形成总额'; unit = '亿元' },
    @{ key = 'depreciation'; file = '固定资产折旧 亿元.xls'; indicator = '固定资产折旧'; unit = '亿元' },
    @{ key = 'population'; file = '年末常住人口 万人.xls'; indicator = '年末常住人口'; unit = '万人' }
)

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false
$sources = @()

try {
    foreach ($spec in $specs) {
        $path = Join-Path $SourceRoot $spec.file
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            throw "Required raw source does not exist: $path"
        }

        $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
        $item = Get-Item -LiteralPath $path
        $workbook = $excel.Workbooks.Open($path, 0, $true)
        try {
            if ($workbook.Worksheets.Count -ne 1) {
                throw "Expected exactly one worksheet in $path"
            }
            $sheet = $workbook.Worksheets.Item(1)
            try {
                $used = $sheet.UsedRange
                try {
                    $headers = @{}
                    for ($column = 2; $column -le $used.Columns.Count; $column++) {
                        $header = [string]$used.Cells.Item(4, $column).Text
                        if ($header -match '^([0-9]{4})年$') {
                            $headers[[int]$Matches[1]] = $column
                        }
                    }
                    if ($headers.Count -eq 0) {
                        throw "No year headers detected in $path"
                    }

                    $records = @()
                    $notes = @()
                    for ($row = 5; $row -le $used.Rows.Count; $row++) {
                        $province = [string]$used.Cells.Item($row, 1).Text
                        if ($province -match '^(数据来源|注：)') {
                            $notes += $province
                            continue
                        }
                        if ([string]::IsNullOrWhiteSpace($province)) { continue }
                        foreach ($year in ($headers.Keys | Sort-Object)) {
                            $cell = $used.Cells.Item($row, $headers[$year])
                            $value = $cell.Value2
                            $numericValue = $null
                            if ($null -ne $value -and -not [string]::IsNullOrWhiteSpace([string]$value)) {
                                if ($value -isnot [ValueType]) {
                                    throw "Non-numeric observation at $($spec.file), $province, ${year}: $value"
                                }
                                $numericValue = [double]$value
                            }
                            $records += [ordered]@{
                                source_province_name = $province
                                year = [int]$year
                                raw_value = $numericValue
                                display_text = [string]$cell.Text
                            }
                        }
                    }

                    $sources += [ordered]@{
                        key = $spec.key
                        actual_path = $item.FullName
                        filename = $item.Name
                        sha256 = $hash
                        bytes = [int64]$item.Length
                        last_write_time = $item.LastWriteTime.ToString('o')
                        workbook_format = 'BIFF8_XLS'
                        sheet_name = [string]$sheet.Name
                        used_rows = [int]$used.Rows.Count
                        used_columns = [int]$used.Columns.Count
                        header_row = 4
                        province_start_row = 5
                        year_orientation = 'columns_descending_in_source'
                        province_orientation = 'rows'
                        indicator = $spec.indicator
                        original_unit = $spec.unit
                        advertised_time_text = [string]$used.Cells.Item(3, 1).Text
                        header_years = @($headers.Keys | Sort-Object)
                        notes = $notes
                        records = $records
                    }
                }
                finally {
                    [Runtime.InteropServices.Marshal]::FinalReleaseComObject($used) | Out-Null
                }
            }
            finally {
                [Runtime.InteropServices.Marshal]::FinalReleaseComObject($sheet) | Out-Null
            }
        }
        finally {
            $workbook.Close($false)
            [Runtime.InteropServices.Marshal]::FinalReleaseComObject($workbook) | Out-Null
        }
    }
}
finally {
    $excel.Quit()
    [Runtime.InteropServices.Marshal]::FinalReleaseComObject($excel) | Out-Null
}

$payload = [ordered]@{
    schema = 'CH5_RAW_NBS_XLS_EXTRACTION_V1'
    extraction_utc = [DateTime]::UtcNow.ToString('o')
    extraction_method = 'Microsoft Excel COM 16 read-only Workbooks.Open(path, UpdateLinks=0, ReadOnly=true); Value2'
    source_root = (Get-Item -LiteralPath $SourceRoot).FullName
    sources = $sources
}

$parent = Split-Path -Parent $OutputJson
if (-not (Test-Path -LiteralPath $parent)) {
    New-Item -ItemType Directory -Path $parent | Out-Null
}
$json = $payload | ConvertTo-Json -Depth 8
[IO.File]::WriteAllText($OutputJson, $json, [Text.UTF8Encoding]::new($false))
Write-Output $OutputJson
