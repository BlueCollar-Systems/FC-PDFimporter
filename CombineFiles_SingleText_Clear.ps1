$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -LiteralPath $scriptDir

$root = (Resolve-Path '.').Path
$outFile = Join-Path $root 'Full_Folder_Log.txt'
$selfPs1 = (Resolve-Path $MyInvocation.MyCommand.Path).Path
$selfBat = Join-Path $root 'Run_CombineFiles_SingleText_Clear.bat'
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Write-Line {
    param(
        [System.IO.StreamWriter]$Writer,
        [string]$Text
    )
    $Writer.WriteLine($Text)
}

function Get-RelativePath {
    param(
        [string]$BasePath,
        [string]$TargetPath
    )
    $baseResolved = (Resolve-Path -LiteralPath $BasePath).Path.TrimEnd('\') + '\'
    $targetResolved = (Resolve-Path -LiteralPath $TargetPath).Path
    $baseUri = New-Object System.Uri($baseResolved)
    $targetUri = New-Object System.Uri($targetResolved)
    return [System.Uri]::UnescapeDataString(
        $baseUri.MakeRelativeUri($targetUri).ToString().Replace('/', '\')
    )
}

function Test-IsBinaryFile {
    param([string]$Path)

    try {
        $fs = [System.IO.File]::Open($Path, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, [System.IO.FileShare]::ReadWrite)
        try {
            $length = [Math]::Min(8192, [int]$fs.Length)
            if ($length -le 0) { return $false }

            $buffer = New-Object byte[] $length
            [void]$fs.Read($buffer, 0, $length)

            foreach ($b in $buffer) {
                if ($b -eq 0) { return $true }
                if (($b -lt 9) -or (($b -gt 13) -and ($b -lt 32))) { return $true }
            }
            return $false
        }
        finally {
            $fs.Dispose()
        }
    }
    catch {
        return $true
    }
}

function Get-Sha256 {
    param([string]$Path)

    try {
        return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
    }
    catch {
        return 'unavailable'
    }
}

function Write-FileBlock {
    param(
        [System.IO.StreamWriter]$Writer,
        [string]$FilePath,
        [string]$RootPath
    )

    $item = Get-Item -LiteralPath $FilePath -Force
    $relative = Get-RelativePath -BasePath $RootPath -TargetPath $FilePath
    $extension = $item.Extension
    if ([string]::IsNullOrEmpty($extension)) { $extension = '[no extension]' }
    $sha = Get-Sha256 -Path $FilePath
    $isBinary = Test-IsBinaryFile -Path $FilePath

    Write-Line $Writer '================================================================'
    Write-Line $Writer 'FILE_BEGIN'
    Write-Line $Writer ('ABSOLUTE_PATH: ' + $item.FullName)
    Write-Line $Writer ('RELATIVE_PATH: ' + $relative)
    Write-Line $Writer ('PARENT_FOLDER: ' + $item.DirectoryName)
    Write-Line $Writer ('FILE_NAME: ' + $item.Name)
    Write-Line $Writer ('EXTENSION: ' + $extension)
    Write-Line $Writer ('SIZE_BYTES: ' + $item.Length)
    Write-Line $Writer ('LAST_WRITE_TIME: ' + $item.LastWriteTime.ToString('yyyy-MM-dd HH:mm:ss.fff'))
    Write-Line $Writer ('SHA256: ' + $sha)
    if ($isBinary) {
        Write-Line $Writer 'CONTENT_KIND: binary_base64'
    }
    else {
        Write-Line $Writer 'CONTENT_KIND: text'
    }
    Write-Line $Writer 'CONTENT_START'

    if ($isBinary) {
        $bytes = [System.IO.File]::ReadAllBytes($FilePath)
        $b64 = [System.Convert]::ToBase64String($bytes)
        Write-Line $Writer '```base64'
        for ($i = 0; $i -lt $b64.Length; $i += 120) {
            $take = [Math]::Min(120, $b64.Length - $i)
            Write-Line $Writer ($b64.Substring($i, $take))
        }
        Write-Line $Writer '```'
    }
    else {
        Write-Line $Writer '```text'
        try {
            $reader = New-Object System.IO.StreamReader($FilePath, $true)
            try {
                while (-not $reader.EndOfStream) {
                    $line = $reader.ReadLine()
                    if ($null -eq $line) { $line = '' }
                    Write-Line $Writer $line
                }
            }
            finally {
                $reader.Dispose()
            }
        }
        catch {
            Write-Line $Writer ('[READ_ERROR] ' + $_.Exception.Message)
        }
        Write-Line $Writer '```'
    }

    Write-Line $Writer 'CONTENT_END'
    Write-Line $Writer 'FILE_END'
    Write-Line $Writer ''
}

$writer = New-Object System.IO.StreamWriter($outFile, $false, $utf8NoBom)

try {
    Write-Line $writer 'FULL_FOLDER_LOG'
    Write-Line $writer ('ROOT_FOLDER: ' + $root)
    Write-Line $writer ('GENERATED_AT: ' + (Get-Date).ToString('yyyy-MM-dd HH:mm:ss.fff'))
    Write-Line $writer ''

    Write-Line $writer '=============================='
    Write-Line $writer 'FOLDER_TREE'
    Write-Line $writer '=============================='

    Get-ChildItem -LiteralPath $root -Recurse -Force |
        Sort-Object FullName |
        ForEach-Object {
            $relative = Get-RelativePath -BasePath $root -TargetPath $_.FullName
            if ($_.PSIsContainer) {
                Write-Line $writer ('[DIR]  ' + $relative)
            }
            else {
                Write-Line $writer ('[FILE] ' + $relative)
            }
        }

    Write-Line $writer ''
    Write-Line $writer '=============================='
    Write-Line $writer 'FILE_CONTENTS'
    Write-Line $writer '=============================='

    $files = Get-ChildItem -LiteralPath $root -File -Recurse -Force |
        Sort-Object FullName |
        Where-Object {
            $_.FullName -ne $outFile -and
            $_.FullName -ne $selfPs1 -and
            $_.FullName -ne $selfBat
        }

    foreach ($file in $files) {
        Write-FileBlock -Writer $writer -FilePath $file.FullName -RootPath $root
    }
}
finally {
    $writer.Dispose()
}

Write-Host ''
Write-Host 'Done.'
Write-Host ('Created: ' + $outFile)
