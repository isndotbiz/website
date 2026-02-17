# Auto-commit script with conventional commit messages
# Usage: .\auto-commit.ps1 "optional custom message"

param([string]$CustomMessage = "")

$status = git status --short
if (-not $status) {
    Write-Host "No changes to commit" -ForegroundColor Yellow
    exit 0
}

# Determine commit type based on changes
$commitType = "chore"
$scope = ""
$subject = "update files"

$diff = git diff --name-only HEAD
if ($diff -match "\.html$") {
    $commitType = "fix"
    $scope = "content"
    $subject = "update website content"
}
if ($diff -match "\.(webp|png|jpg)$") {
    $commitType = "feat"
    $scope = "assets"
    $subject = "update visual assets"
}
if ($diff -match "\.css$") {
    $commitType = "style"
    $scope = "design"
    $subject = "update styles"
}
if ($diff -match "test|spec") {
    $commitType = "test"
    $scope = "qa"
    $subject = "update tests"
}
if ($diff -match "\.md$") {
    $commitType = "docs"
    $subject = "update documentation"
}

if ($CustomMessage) { $subject = $CustomMessage }

$scopeStr = if ($scope) { "($scope)" } else { "" }
$message = "${commitType}${scopeStr}: $subject

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

Write-Host "`n📝 Commit Message:" -ForegroundColor Cyan
Write-Host $message

git add .
git commit -m $message
git push

Write-Host "`n✅ Committed and pushed!" -ForegroundColor Green
