# PowerShell version of S3 URL fix script for Windows
# Fix S3 URL backslashes in ISN.BIZ website

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "ISN.BIZ S3 URL Backslash Fix" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Backup files first
Write-Host "Creating backups..." -ForegroundColor Yellow
$files = @("alicia.html", "bri.html", "jonathan.html", "lilly.html", "index.html", "portfolio-grid.html")
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

foreach ($file in $files) {
    if (Test-Path $file) {
        Copy-Item $file "$file.backup_$timestamp"
        Write-Host "  ✓ Backed up $file" -ForegroundColor Green
    }
}
Write-Host ""

# Fix backslashes in founder pages and index
Write-Host "Fixing backslashes in S3 URLs..." -ForegroundColor Yellow
$founderFiles = @("alicia.html", "bri.html", "jonathan.html", "lilly.html", "index.html")

foreach ($file in $founderFiles) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        $content = $content -replace 'founders\\', 'founders/'
        Set-Content -Path $file -Value $content -NoNewline
        Write-Host "  ✓ Fixed $file" -ForegroundColor Green
    }
}
Write-Host ""

# Fix portfolio-grid.html duplicate URL prefix
Write-Host "Fixing duplicate URL prefix in portfolio-grid.html..." -ForegroundColor Yellow
if (Test-Path "portfolio-grid.html") {
    $content = Get-Content "portfolio-grid.html" -Raw
    $content = $content -replace 'premium_v3/https://isnbiz-assets', 'https://isnbiz-assets'
    Set-Content -Path "portfolio-grid.html" -Value $content -NoNewline
    Write-Host "  ✓ Fixed portfolio-grid.html" -ForegroundColor Green
}
Write-Host ""

# Report changes
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Changes Applied:" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "1. Replaced founders\ with founders/ in:"
Write-Host "   - alicia.html"
Write-Host "   - bri.html"
Write-Host "   - jonathan.html"
Write-Host "   - lilly.html"
Write-Host "   - index.html"
Write-Host ""
Write-Host "2. Removed duplicate URL prefix in:"
Write-Host "   - portfolio-grid.html"
Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "1. Review changes with: git diff"
Write-Host "2. Test website: python test_website.py"
Write-Host "3. If satisfied, commit: git add . && git commit -m 'Fix S3 URL path separators'"
Write-Host "4. Upload missing S3 files (see WEBSITE_TEST_ANALYSIS.md)"
Write-Host ""
Write-Host "Backups created with .backup_$timestamp extension" -ForegroundColor Yellow
Write-Host "✓ Fix complete!" -ForegroundColor Green
