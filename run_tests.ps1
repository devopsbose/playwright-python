# run_tests.ps1 — test runner helper for Windows
param(
    [string]$Browser  = "chromium",
    [int]   $Workers  = 4,
    [string]$Marker   = "",
    [switch]$Headed,
    [switch]$AllBrowsers
)

$env:HEADLESS = if ($Headed) { "false" } else { "true" }

$browserArgs = if ($AllBrowsers) {
    "--browser chromium --browser firefox --browser webkit"
} else {
    "--browser $Browser"
}

$markerArg = if ($Marker) { "-m $Marker" } else { "" }

$cmd = "pytest $browserArgs -n $Workers $markerArg"
Write-Host "Running: $cmd" -ForegroundColor Cyan
Invoke-Expression $cmd
