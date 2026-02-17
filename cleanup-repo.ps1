# cleanup-repo.ps1
# Archives non-production files, deletes recreatable files, unracks dev-only docs, and shrinks git repo.
# Run from the ISNBIZ_Files directory.

param(
    [switch]$DryRun,
    [switch]$SkipGitGc
)

$ErrorActionPreference = "Stop"
$RepoRoot = $PSScriptRoot
if (-not $RepoRoot) { $RepoRoot = Get-Location }

Write-Host "`n=== ISN.BIZ Repo Cleanup ===" -ForegroundColor Cyan
if ($DryRun) { Write-Host "[DRY RUN] No changes will be made.`n" -ForegroundColor Yellow }

# --- Step 1: Archive non-production directories ---
$ArchiveDate = Get-Date -Format "yyyy-MM-dd"
$ArchiveDir = Join-Path $RepoRoot "Archive\$ArchiveDate"

$DirsToArchive = @(
    "backups",
    "generated_founders",
    "assets",
    "screenshots",
    "SpiritAtlas",
    "spiritatlas_screenshots",
    "docs",
    "scripts"
)

Write-Host "`n--- Step 1: Archive non-production directories ---" -ForegroundColor Green

$HasArchivable = $false
foreach ($dir in $DirsToArchive) {
    $srcPath = Join-Path $RepoRoot $dir
    if (Test-Path $srcPath) {
        $HasArchivable = $true
        break
    }
}

if ($HasArchivable) {
    if (-not $DryRun) {
        New-Item -ItemType Directory -Path $ArchiveDir -Force | Out-Null
    }
    Write-Host "Archive target: $ArchiveDir"

    foreach ($dir in $DirsToArchive) {
        $srcPath = Join-Path $RepoRoot $dir
        if (Test-Path $srcPath) {
            $destPath = Join-Path $ArchiveDir $dir
            $size = (Get-ChildItem -Recurse -File $srcPath | Measure-Object -Property Length -Sum).Sum
            $sizeMB = [math]::Round($size / 1MB, 1)
            Write-Host "  Moving $dir ($sizeMB MB) -> Archive/$ArchiveDate/$dir"
            if (-not $DryRun) {
                Move-Item -Path $srcPath -Destination $destPath -Force
            }
        } else {
            Write-Host "  Skipping $dir (not found)" -ForegroundColor DarkGray
        }
    }
} else {
    Write-Host "  No directories to archive." -ForegroundColor DarkGray
}

# --- Step 2: Delete recreatable / temporary files ---
Write-Host "`n--- Step 2: Delete recreatable files ---" -ForegroundColor Green

$DirsToDelete = @(
    "venv_fal",
    "node_modules",
    "playwright-report",
    "test-results",
    "1password_import"
)

$FilesToDelete = @(
    ".op_env_fal.tmp"
)

foreach ($dir in $DirsToDelete) {
    $path = Join-Path $RepoRoot $dir
    if (Test-Path $path) {
        $size = (Get-ChildItem -Recurse -File $path | Measure-Object -Property Length -Sum).Sum
        $sizeMB = [math]::Round($size / 1MB, 1)
        Write-Host "  Deleting $dir ($sizeMB MB)"
        if (-not $DryRun) {
            Remove-Item -Recurse -Force $path
        }
    } else {
        Write-Host "  Skipping $dir (not found)" -ForegroundColor DarkGray
    }
}

foreach ($file in $FilesToDelete) {
    $path = Join-Path $RepoRoot $file
    if (Test-Path $path) {
        Write-Host "  Deleting $file"
        if (-not $DryRun) {
            Remove-Item -Force $path
        }
    } else {
        Write-Host "  Skipping $file (not found)" -ForegroundColor DarkGray
    }
}

# --- Step 3: Untrack dev-only files from git ---
Write-Host "`n--- Step 3: Untrack dev-only files from git ---" -ForegroundColor Green

$FilesToUntrack = @(
    "DEPLOYMENT_GAPS.md",
    "DEPLOYMENT_SUMMARY_2026-02-06.md",
    "SERVICES_PAGE_FIXES.md",
    "schema-breadcrumb.json",
    "schema-organization.json",
    "schema-services.json",
    "schema-team.json",
    "schema-website.json"
)

Push-Location $RepoRoot
foreach ($file in $FilesToUntrack) {
    $path = Join-Path $RepoRoot $file
    if (Test-Path $path) {
        # Check if git-tracked
        $tracked = git ls-files --error-unmatch $file 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  git rm --cached $file"
            if (-not $DryRun) {
                git rm --cached $file 2>$null
            }
        } else {
            Write-Host "  $file (already untracked)" -ForegroundColor DarkGray
        }
    } else {
        Write-Host "  $file (not found)" -ForegroundColor DarkGray
    }
}
Pop-Location

# --- Step 4: Update .gitignore ---
Write-Host "`n--- Step 4: Update .gitignore ---" -ForegroundColor Green

$NewIgnorePatterns = @(
    "",
    "# Dev-only markdown docs (untracked)",
    "DEPLOYMENT_GAPS.md",
    "DEPLOYMENT_SUMMARY_*.md",
    "SERVICES_PAGE_FIXES.md",
    "",
    "# Standalone schema JSON (schema is inline in HTML)",
    "schema-*.json",
    "",
    "# PowerShell workflow scripts (local-only)",
    "cleanup-repo.ps1",
    "upload-archive-to-babynas.ps1",
    "deploy-workflow.ps1",
    "CODEX_HANDOFF.ps1",
    "",
    "# Deployment notes (local-only)",
    "DEPLOYMENT_SUCCESS_*.md",
    "",
    "# 1Password / env templates (local-only)",
    ".env.1password.template",
    ".env.fal.template",
    "",
    "# Claude Code config",
    ".claude/"
)

$gitignorePath = Join-Path $RepoRoot ".gitignore"
$currentContent = Get-Content $gitignorePath -Raw

# Check if we already added these patterns
if ($currentContent -notmatch "Dev-only markdown docs") {
    Write-Host "  Appending new patterns to .gitignore"
    if (-not $DryRun) {
        $NewIgnorePatterns | Out-File -Append -Encoding utf8 $gitignorePath
    }
} else {
    Write-Host "  .gitignore already updated" -ForegroundColor DarkGray
}

# --- Step 5: Git gc ---
if (-not $SkipGitGc) {
    Write-Host "`n--- Step 5: Shrink .git with git gc ---" -ForegroundColor Green

    Push-Location $RepoRoot
    $gitSizeBefore = (Get-ChildItem -Recurse -File ".git" | Measure-Object -Property Length -Sum).Sum
    $gitSizeMBBefore = [math]::Round($gitSizeBefore / 1MB, 1)
    Write-Host "  .git size before: $gitSizeMBBefore MB"

    if (-not $DryRun) {
        Write-Host "  Running git gc --aggressive --prune=now (this may take a few minutes)..."
        git gc --aggressive --prune=now

        $gitSizeAfter = (Get-ChildItem -Recurse -File ".git" | Measure-Object -Property Length -Sum).Sum
        $gitSizeMBAfter = [math]::Round($gitSizeAfter / 1MB, 1)
        $saved = [math]::Round($gitSizeMBBefore - $gitSizeMBAfter, 1)
        Write-Host "  .git size after: $gitSizeMBAfter MB (saved $saved MB)" -ForegroundColor Green
    }
    Pop-Location
} else {
    Write-Host "`n--- Step 5: Skipped git gc (--SkipGitGc) ---" -ForegroundColor Yellow
}

# --- Summary ---
Write-Host "`n=== Cleanup Complete ===" -ForegroundColor Cyan
if ($DryRun) {
    Write-Host "This was a DRY RUN. Re-run without -DryRun to apply changes." -ForegroundColor Yellow
} else {
    Write-Host "Next steps:"
    Write-Host "  1. Review changes: git status"
    Write-Host "  2. Commit: git add .gitignore && git commit -m 'chore: cleanup repo, untrack dev-only files'"
    Write-Host "  3. Push: git push"
    Write-Host "  4. Upload archive to Baby NAS: .\upload-archive-to-babynas.ps1"
}
Write-Host ""
