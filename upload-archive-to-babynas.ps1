# upload-archive-to-babynas.ps1
# Uploads Archive/ directory to Baby NAS via SCP.
# Requires SSH key access to Baby NAS (keys stored in 1Password).

param(
    [string]$NasUser = "jdmal",
    [string]$NasHost = "100.95.3.18",
    [string]$NasPath = "/mnt/tank/archives/isnbiz",
    [switch]$DeleteAfterUpload,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$RepoRoot = $PSScriptRoot
if (-not $RepoRoot) { $RepoRoot = Get-Location }

$ArchiveDir = Join-Path $RepoRoot "Archive"

Write-Host "`n=== Upload Archive to Baby NAS ===" -ForegroundColor Cyan
if ($DryRun) { Write-Host "[DRY RUN] No changes will be made.`n" -ForegroundColor Yellow }

# --- Check archive exists ---
if (-not (Test-Path $ArchiveDir)) {
    Write-Host "No Archive/ directory found. Run cleanup-repo.ps1 first." -ForegroundColor Red
    exit 1
}

$archiveSize = (Get-ChildItem -Recurse -File $ArchiveDir | Measure-Object -Property Length -Sum).Sum
$archiveSizeMB = [math]::Round($archiveSize / 1MB, 1)
Write-Host "Archive size: $archiveSizeMB MB"
Write-Host "Target: ${NasUser}@${NasHost}:${NasPath}/`n"

# --- Test SSH connectivity ---
Write-Host "--- Testing SSH connectivity ---" -ForegroundColor Green
if (-not $DryRun) {
    try {
        $sshTest = ssh -o ConnectTimeout=10 -o BatchMode=yes "${NasUser}@${NasHost}" "echo OK" 2>&1
        if ($sshTest -ne "OK") {
            Write-Host "SSH connection failed. Check your SSH keys." -ForegroundColor Red
            Write-Host "Keys are stored in 1Password. Try:" -ForegroundColor Yellow
            Write-Host "  ssh-add ~/.ssh/id_ed25519  (or the key from 1Password)" -ForegroundColor Yellow
            Write-Host "  Alternative user: truenas_admin@${NasHost}" -ForegroundColor Yellow
            exit 1
        }
        Write-Host "  SSH connection OK" -ForegroundColor Green
    } catch {
        Write-Host "  SSH connection failed: $_" -ForegroundColor Red
        exit 1
    }
}

# --- Ensure remote directory exists ---
Write-Host "`n--- Ensuring remote directory exists ---" -ForegroundColor Green
if (-not $DryRun) {
    ssh "${NasUser}@${NasHost}" "mkdir -p ${NasPath}"
    Write-Host "  Remote directory ready: ${NasPath}"
}

# --- Upload via SCP ---
Write-Host "`n--- Uploading archive ---" -ForegroundColor Green

$archiveSubDirs = Get-ChildItem -Directory $ArchiveDir
foreach ($subDir in $archiveSubDirs) {
    Write-Host "  Uploading $($subDir.Name)..."
    if (-not $DryRun) {
        scp -r "$($subDir.FullName)" "${NasUser}@${NasHost}:${NasPath}/"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "  SCP failed for $($subDir.Name)" -ForegroundColor Red
            exit 1
        }
    }
}

# --- Verify upload ---
Write-Host "`n--- Verifying upload ---" -ForegroundColor Green
if (-not $DryRun) {
    $remoteList = ssh "${NasUser}@${NasHost}" "ls -la ${NasPath}/"
    Write-Host $remoteList
    Write-Host "`n  Upload verified." -ForegroundColor Green
}

# --- Optionally delete local archive ---
if ($DeleteAfterUpload) {
    Write-Host "`n--- Deleting local archive ---" -ForegroundColor Green
    if (-not $DryRun) {
        $confirm = Read-Host "Delete local Archive/ ($archiveSizeMB MB)? (y/N)"
        if ($confirm -eq "y") {
            Remove-Item -Recurse -Force $ArchiveDir
            Write-Host "  Local archive deleted." -ForegroundColor Green
        } else {
            Write-Host "  Kept local archive." -ForegroundColor Yellow
        }
    }
}

# --- Summary ---
Write-Host "`n=== Upload Complete ===" -ForegroundColor Cyan
if ($DryRun) {
    Write-Host "This was a DRY RUN. Re-run without -DryRun to apply." -ForegroundColor Yellow
} else {
    Write-Host "Archive uploaded to ${NasUser}@${NasHost}:${NasPath}/"
    if (-not $DeleteAfterUpload) {
        Write-Host "Local archive retained. To delete: .\upload-archive-to-babynas.ps1 -DeleteAfterUpload"
    }
}
Write-Host ""
