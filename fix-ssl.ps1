# SSL Fix Script - ISN.BIZ + HROC
# Run this in PowerShell: .\fix-ssl.ps1
# Or provide your Netlify token: .\fix-ssl.ps1 -NetlifyToken "your_token_here"

param(
    [string]$NetlifyToken = ""
)

$CF_TOKEN   = "FUsbCPBplDQXB4fuk3Pn16J4Gpm2tBOwgLI1H7Vj"  # DNS token (fallback)
$CF_EMAIL   = "jdmallin25x40@gmail.com"
$CF_GLOBAL  = "b90eb8d819ae0c4ab1c14a481db66b99b2d38"
$CF_ZONE_ISN  = "a2efe184e74443f824ef58f1c862eb5a"
$CF_ZONE_HROC = "0da5d1116d7e40e8c77615ce8a757cd1"
$NETLIFY_ISN  = "4d860499-0d6c-49cd-864f-69a0b7a2b3fe"
$NETLIFY_HROC = "f5c7828a-b18a-41c1-a8bc-c64e5beb13ba"

$cfHeaders = @{
    "X-Auth-Email" = $CF_EMAIL
    "X-Auth-Key"   = $CF_GLOBAL
    "Content-Type" = "application/json"
}

function CF-Get($zone, $path) {
    $uri = "https://api.cloudflare.com/client/v4/zones/$zone/$path"
    try { (Invoke-RestMethod -Uri $uri -Headers $cfHeaders -Method GET) } catch { Write-Host "ERROR: $_" -ForegroundColor Red }
}

function CF-Patch($zone, $path, $body) {
    $uri = "https://api.cloudflare.com/client/v4/zones/$zone/$path"
    try { (Invoke-RestMethod -Uri $uri -Headers $cfHeaders -Method PATCH -Body ($body | ConvertTo-Json)) } catch { Write-Host "ERROR: $_" -ForegroundColor Red }
}

# =============================================
# STEP 1: CHECK ZONE STATUS
# =============================================
Write-Host "`n=== CHECKING ZONE STATUS ===" -ForegroundColor Cyan

$isnZone = CF-Get $CF_ZONE_ISN "?"
if ($isnZone.result) {
    Write-Host "isn.biz zone: $($isnZone.result.status) (paused: $($isnZone.result.paused))" -ForegroundColor $(if ($isnZone.result.status -eq "active") { "Green" } else { "Red" })
}

$hrocZone = CF-Get $CF_ZONE_HROC "?"
if ($hrocZone.result) {
    Write-Host "hrocinc.org zone: $($hrocZone.result.status) (paused: $($hrocZone.result.paused))" -ForegroundColor $(if ($hrocZone.result.status -eq "active") { "Green" } else { "Red" })
}

# =============================================
# STEP 2: CHECK CURRENT SSL SETTINGS
# =============================================
Write-Host "`n=== CURRENT SSL SETTINGS ===" -ForegroundColor Cyan

$isnSSL  = CF-Get $CF_ZONE_ISN  "settings/ssl"
$hrocSSL = CF-Get $CF_ZONE_HROC "settings/ssl"
Write-Host "isn.biz SSL mode:    $($isnSSL.result.value)"
Write-Host "hrocinc.org SSL mode: $($hrocSSL.result.value)"

# =============================================
# STEP 3: SET SSL TO "FULL" FOR BOTH
# =============================================
Write-Host "`n=== SETTING SSL TO FULL ===" -ForegroundColor Cyan

$r1 = CF-Patch $CF_ZONE_ISN  "settings/ssl" @{ value = "full" }
if ($r1.success) { Write-Host "isn.biz SSL -> full: OK" -ForegroundColor Green }
else             { Write-Host "isn.biz SSL set failed: $($r1.errors)" -ForegroundColor Red }

$r2 = CF-Patch $CF_ZONE_HROC "settings/ssl" @{ value = "full" }
if ($r2.success) { Write-Host "hrocinc.org SSL -> full: OK" -ForegroundColor Green }
else             { Write-Host "hrocinc.org SSL set failed: $($r2.errors)" -ForegroundColor Red }

# =============================================
# STEP 4: ENABLE ALWAYS USE HTTPS
# =============================================
Write-Host "`n=== ENABLING ALWAYS USE HTTPS ===" -ForegroundColor Cyan

$r3 = CF-Patch $CF_ZONE_ISN  "settings/always_use_https" @{ value = "on" }
$r4 = CF-Patch $CF_ZONE_HROC "settings/always_use_https" @{ value = "on" }
Write-Host "isn.biz always_use_https:    $( if ($r3.success) { 'OK' } else { $r3.errors } )"
Write-Host "hrocinc.org always_use_https: $( if ($r4.success) { 'OK' } else { $r4.errors } )"

# =============================================
# STEP 4b: ENABLE CLOUDFLARE PROXY ON isn.biz A RECORD
# (This gives Cloudflare Universal SSL immediately - no cert wait)
# =============================================
Write-Host "`n=== ENABLING CLOUDFLARE PROXY ON isn.biz ===" -ForegroundColor Cyan

$records = CF-Get $CF_ZONE_ISN "dns_records?type=A&name=isn.biz"
if ($records.result) {
    $rec = $records.result[0]
    Write-Host "Current A record: $($rec.name) -> $($rec.content) (proxied: $($rec.proxied))"

    if (-not $rec.proxied) {
        $update = @{ type="A"; name="isn.biz"; content=$rec.content; ttl=1; proxied=$true }
        $r = Invoke-RestMethod -Uri "https://api.cloudflare.com/client/v4/zones/$CF_ZONE_ISN/dns_records/$($rec.id)" `
            -Headers $cfHeaders -Method PUT -Body ($update | ConvertTo-Json)
        if ($r.success) { Write-Host "Cloudflare proxy ENABLED for isn.biz -> SSL now served by Cloudflare" -ForegroundColor Green }
        else             { Write-Host "Failed: $($r.errors)" -ForegroundColor Red }
    } else {
        Write-Host "Already proxied - OK" -ForegroundColor Green
    }
} else {
    Write-Host "Could not fetch DNS records: $($records.errors)" -ForegroundColor Red
}

# =============================================
# STEP 5: NETLIFY SSL PROVISIONING
# =============================================
Write-Host "`n=== NETLIFY SSL ===" -ForegroundColor Cyan

if (-not $NetlifyToken) {
    Write-Host "No Netlify token provided. Get it from 1Password ('Netlify' item)." -ForegroundColor Yellow
    Write-Host "Then re-run: .\fix-ssl.ps1 -NetlifyToken YOUR_TOKEN" -ForegroundColor Yellow
} else {
    $nlHeaders = @{ "Authorization" = "Bearer $NetlifyToken" }

    try {
        Invoke-RestMethod -Uri "https://api.netlify.com/api/v1/sites/$NETLIFY_ISN/ssl" `
            -Headers $nlHeaders -Method POST | Out-Null
        Write-Host "isn.biz Netlify SSL provisioned: OK" -ForegroundColor Green
    } catch { Write-Host "isn.biz Netlify SSL: $_" -ForegroundColor Red }

    try {
        Invoke-RestMethod -Uri "https://api.netlify.com/api/v1/sites/$NETLIFY_HROC/ssl" `
            -Headers $nlHeaders -Method POST | Out-Null
        Write-Host "hrocinc.org Netlify SSL provisioned: OK" -ForegroundColor Green
    } catch { Write-Host "hrocinc.org Netlify SSL: $_" -ForegroundColor Red }
}

# =============================================
# STEP 6: VERIFY SITES ARE REACHABLE
# =============================================
Write-Host "`n=== VERIFYING SITES ===" -ForegroundColor Cyan

foreach ($url in @("https://isn.biz", "https://hrocinc.org", "https://isndotbiz.netlify.app", "https://hrocinc.netlify.app")) {
    try {
        $resp = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 10 -SkipCertificateCheck
        Write-Host "$url : $($resp.StatusCode)" -ForegroundColor Green
    } catch {
        Write-Host "$url : FAILED - $_" -ForegroundColor Red
    }
}

Write-Host "`nDone. If Cloudflare SSL is now 'full', wait 1-2 min then recheck the sites." -ForegroundColor Cyan
