# deploy-workflow.ps1
# Standard deployment workflow for ISN.BIZ website.
# Stages changes, commits, pushes to GitHub, and deploys to Netlify.

param(
    [string]$CommitMessage,
    [switch]$SkipTests,
    [switch]$SkipNetlify,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$RepoRoot = $PSScriptRoot
if (-not $RepoRoot) { $RepoRoot = Get-Location }

Write-Host "`n=== ISN.BIZ Deploy Workflow ===" -ForegroundColor Cyan
if ($DryRun) { Write-Host "[DRY RUN] No changes will be made.`n" -ForegroundColor Yellow }

# --- Production files to deploy ---
$ProductionPatterns = @(
    "*.html",
    "*.css",
    "*.js",
    "js/",
    "netlify.toml",
    ".netlifyignore",
    ".gitignore",
    "robots.txt",
    "sitemap.xml",
    "CLAUDE.md",
    "README.md",
    ".serena/",
    "package.json",
    "package-lock.json",
    "playwright.config.js",
    "tests/",
    ".env.tpl"
)

# --- Step 1: Check for uncommitted changes ---
Write-Host "`n--- Step 1: Check git status ---" -ForegroundColor Green

Push-Location $RepoRoot
$gitStatus = git status --porcelain
if (-not $gitStatus) {
    Write-Host "  No changes to deploy." -ForegroundColor Yellow
    Pop-Location
    exit 0
}

Write-Host "Changes detected:"
git status --short
Pop-Location

# --- Step 2: Run tests (optional) ---
if (-not $SkipTests) {
    Write-Host "`n--- Step 2: Run tests ---" -ForegroundColor Green

    # Check if Playwright is available
    Push-Location $RepoRoot
    if (Test-Path "package.json") {
        $hasPlaywright = (Get-Content "package.json" -Raw) -match "playwright"
        if ($hasPlaywright -and (Test-Path "node_modules")) {
            Write-Host "  Running Playwright tests..."
            if (-not $DryRun) {
                npm test
                if ($LASTEXITCODE -ne 0) {
                    Write-Host "  Tests failed. Fix issues before deploying." -ForegroundColor Red
                    Pop-Location
                    exit 1
                }
                Write-Host "  Tests passed." -ForegroundColor Green
            }
        } else {
            Write-Host "  No tests configured or node_modules missing. Skipping." -ForegroundColor DarkGray
        }
    }
    Pop-Location
} else {
    Write-Host "`n--- Step 2: Tests skipped (--SkipTests) ---" -ForegroundColor Yellow
}

# --- Step 3: Stage production files ---
Write-Host "`n--- Step 3: Stage production files ---" -ForegroundColor Green

Push-Location $RepoRoot
foreach ($pattern in $ProductionPatterns) {
    if (Test-Path $pattern) {
        Write-Host "  git add $pattern"
        if (-not $DryRun) {
            git add $pattern 2>$null
        }
    }
}
Pop-Location

# --- Step 4: Commit ---
Write-Host "`n--- Step 4: Commit changes ---" -ForegroundColor Green

if (-not $CommitMessage) {
    Write-Host "  No commit message provided. Prompting..." -ForegroundColor Yellow
    $CommitMessage = Read-Host "Commit message"
    if (-not $CommitMessage) {
        Write-Host "  Commit message required. Aborting." -ForegroundColor Red
        exit 1
    }
}

Push-Location $RepoRoot
Write-Host "  Commit: $CommitMessage"
if (-not $DryRun) {
    git commit -m "$CommitMessage"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  Commit failed. Check git status." -ForegroundColor Red
        Pop-Location
        exit 1
    }
}
Pop-Location

# --- Step 5: Push to GitHub ---
Write-Host "`n--- Step 5: Push to GitHub ---" -ForegroundColor Green

Push-Location $RepoRoot
$currentBranch = git branch --show-current
Write-Host "  Pushing to origin/$currentBranch..."
if (-not $DryRun) {
    git push origin $currentBranch
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  Push failed. Check git remote configuration." -ForegroundColor Red
        Pop-Location
        exit 1
    }
    Write-Host "  Push successful." -ForegroundColor Green
}
Pop-Location

# --- Step 6: Deploy to Netlify ---
if (-not $SkipNetlify) {
    Write-Host "`n--- Step 6: Deploy to Netlify ---" -ForegroundColor Green

    # Check if Netlify CLI is available
    $netlifyAvailable = Get-Command netlify -ErrorAction SilentlyContinue
    if (-not $netlifyAvailable) {
        Write-Host "  Netlify CLI not found. Install with: npm install -g netlify-cli" -ForegroundColor Yellow
        Write-Host "  Skipping Netlify deploy." -ForegroundColor Yellow
    } else {
        Write-Host "  Deploying to Netlify..."
        if (-not $DryRun) {
            Push-Location $RepoRoot
            netlify deploy --prod
            if ($LASTEXITCODE -ne 0) {
                Write-Host "  Netlify deploy failed. Check netlify CLI authentication." -ForegroundColor Red
                Pop-Location
                exit 1
            }
            Write-Host "  Netlify deploy successful." -ForegroundColor Green
            Pop-Location
        }
    }
} else {
    Write-Host "`n--- Step 6: Netlify deploy skipped (--SkipNetlify) ---" -ForegroundColor Yellow
}

# --- Step 7: Verify deployment ---
if (-not $SkipNetlify -and -not $DryRun) {
    Write-Host "`n--- Step 7: Verify deployment ---" -ForegroundColor Green

    $curlAvailable = Get-Command curl -ErrorAction SilentlyContinue
    if ($curlAvailable) {
        Write-Host "  Checking https://isn.biz..."
        Start-Sleep -Seconds 5  # Give Netlify time to propagate
        $response = curl -sI https://isn.biz 2>$null | Select-String "HTTP/2 200"
        if ($response) {
            Write-Host "  Site is live: https://isn.biz" -ForegroundColor Green
        } else {
            Write-Host "  Site may not be live yet. Check manually: https://isn.biz" -ForegroundColor Yellow
        }
    }
}

# --- Summary ---
Write-Host "`n=== Deploy Complete ===" -ForegroundColor Cyan
if ($DryRun) {
    Write-Host "This was a DRY RUN. Re-run without -DryRun to deploy." -ForegroundColor Yellow
} else {
    Write-Host "Successfully deployed ISN.BIZ website!"
    Write-Host "  - Committed: $CommitMessage"
    Write-Host "  - Pushed to: origin/$currentBranch"
    if (-not $SkipNetlify) {
        Write-Host "  - Deployed to: https://isn.biz"
    }
}
Write-Host ""
