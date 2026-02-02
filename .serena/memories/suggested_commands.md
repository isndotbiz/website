# Suggested Commands for Development

## Windows-Specific Notes
This project is developed on **Windows** (D:\workspace\ISNBIZ_Files). Commands below use Windows-compatible syntax where applicable.

## Local Development

### View Website Locally
```bash
# Windows: Open in default browser
start index.html

# Or specific page
start about.html
start services.html
start portfolio.html
start investors.html
start contact.html

# WSL/Linux alternative (if in WSL2):
explorer.exe index.html
```

### Python Virtual Environment (for asset generation)
```bash
# Activate venv (Windows cmd)
venv_fal\Scripts\activate

# Activate venv (PowerShell)
venv_fal\Scripts\Activate.ps1

# Activate venv (Git Bash / WSL)
source venv_fal/Scripts/activate

# Deactivate
deactivate

# Install dependencies
pip install -r requirements_assets.txt
```

### Asset Generation (Optional)
```bash
# Prerequisites: Activate venv first
source venv_fal/Scripts/activate

# Generate assets with Python scripts
python generate_premium_assets.py
python upload_assets_to_s3.py
python verify_s3_urls.py

# Or use shell scripts (Git Bash / WSL)
bash generate_and_upload_premium_assets.sh
```

## Git Workflow

### Check Status
```bash
cd /d/workspace/ISNBIZ_Files  # Windows
cd /mnt/d/workspace/ISNBIZ_Files  # WSL

git status
git log --oneline -10
git branch
```

### Make Changes
```bash
# Stage specific files (PREFERRED)
git add index.html
git add styles.css
git add script.js

# Stage all changes (use carefully)
git add .

# Commit with message
git commit -m "feat: Add new section to homepage"
git commit -m "fix: Mobile menu toggle issue"
git commit -m "docs: Update README"

# Push to remote
git push
git push origin main
```

### Create Branch
```bash
# Create and switch to new branch
git checkout -b feature/new-section
git checkout -b fix/mobile-bug

# Switch branches
git checkout main
git checkout feature/new-section

# Merge branch (from main)
git checkout main
git merge feature/new-section
```

## Deployment

### Deploy to Netlify (Recommended)

**Method 1: Netlify CLI**
```bash
# Install Netlify CLI (one-time)
npm install -g netlify-cli

# Login to Netlify
netlify login

# Deploy (production)
netlify deploy --prod

# Deploy (preview)
netlify deploy
```

**Method 2: Git-based (auto-deploy)**
```bash
# Push to GitHub (Netlify will auto-deploy)
git add .
git commit -m "Update website"
git push origin main
```

### Deploy to Kusanagi (Alternative)
```bash
# Use provided deployment script
bash deploy-to-kusanagi.sh

# Or manually with rsync (example)
rsync -avz --exclude 'venv_fal' --exclude '.git' \
  ./ user@kusanagi-server:/path/to/webroot/
```

## File Operations (Windows-specific)

### List Files
```bash
# Windows cmd
dir
dir /b  # Brief listing

# PowerShell
ls
Get-ChildItem

# Git Bash / WSL
ls -la
ls -lh
```

### Search Files
```bash
# Find files by name (PowerShell)
Get-ChildItem -Recurse -Filter "*.html"

# Search content (PowerShell)
Select-String -Path "*.html" -Pattern "contact"

# Git Bash / WSL
find . -name "*.html"
grep -r "contact" *.html
```

### Copy/Move Files
```bash
# Windows cmd
copy styles.css styles.backup.css
move old.html archive\

# PowerShell
Copy-Item styles.css styles.backup.css
Move-Item old.html archive\

# Git Bash / WSL
cp styles.css styles.backup.css
mv old.html archive/
```

## Quality Checks

### Validate HTML
```bash
# Online validator
# Visit: https://validator.w3.org/
# Upload: index.html

# Or use local validator (if installed)
html5validator *.html
```

### Check Accessibility (WCAG)
```bash
# Online checker
# Visit: https://wave.webaim.org/
# Enter URL or upload HTML

# Check contrast
# Visit: https://webaim.org/resources/contrastchecker/
```

### Check Links
```bash
# Manual: Open each page and test all links

# Or use online tool
# Visit: https://validator.w3.org/checklink
```

### Performance Test
```bash
# Lighthouse (Chrome DevTools)
# 1. Open Chrome DevTools (F12)
# 2. Go to "Lighthouse" tab
# 3. Run audit

# Or online
# Visit: https://web.dev/measure/
```

## Testing

### Browser Testing
```bash
# Test in multiple browsers:
start chrome index.html
start msedge index.html
start firefox index.html

# Mobile testing (Chrome DevTools)
# F12 > Toggle device toolbar (Ctrl+Shift+M)
```

### Cross-browser Compatibility
```bash
# Recommended test browsers:
# - Chrome (latest)
# - Edge (latest)
# - Firefox (latest)
# - Safari (if available)
# - Mobile: iOS Safari, Android Chrome
```

## S3 Management (Asset Updates)

### Upload to S3
```bash
# Using boto3 Python script
python upload_assets_to_s3.py

# Or AWS CLI (if installed)
aws s3 cp logo.webp s3://isnbiz-assets-1769962280/premium_v3/logos/
aws s3 sync assets/ s3://isnbiz-assets-1769962280/premium_v3/

# Verify URLs
python verify_s3_urls.py
```

### List S3 Assets
```bash
aws s3 ls s3://isnbiz-assets-1769962280/premium_v3/ --recursive
```

## Documentation

### Update Documentation
```bash
# Update CLAUDE.md when making significant changes
# Update README.md for user-facing changes
# Create docs/ files for detailed guides
```

### Generate File Tree
```bash
# PowerShell
tree /F > structure.txt

# Git Bash / WSL
tree -a > structure.txt
```

## Backup

### Create Backup
```bash
# Windows cmd - copy entire directory
xcopy /E /I D:\workspace\ISNBIZ_Files D:\backups\ISNBIZ_Files-%date%

# PowerShell
Copy-Item -Recurse D:\workspace\ISNBIZ_Files D:\backups\ISNBIZ_Files-$(Get-Date -Format 'yyyy-MM-dd')

# Git Bash / WSL - tar archive
tar -czf ../ISNBIZ_Files-backup-$(date +%Y-%m-%d).tar.gz \
  --exclude='venv_fal' --exclude='.git' .
```

## Common Tasks

### Add New Page
```bash
# 1. Create HTML file
cp index.html new-page.html

# 2. Edit content
# (use your text editor)

# 3. Update navigation in ALL pages
# Add: <li><a href="new-page.html">New Page</a></li>

# 4. Test locally
start new-page.html

# 5. Commit and push
git add new-page.html
git commit -m "feat: Add new page"
git push
```

### Update Styling
```bash
# 1. Edit styles.css
# (use your text editor)

# 2. Test locally (refresh browser)
start index.html

# 3. Check all pages
start about.html
start services.html
# etc.

# 4. Commit
git add styles.css
git commit -m "style: Update button styles"
git push
```

### Add New Asset
```bash
# 1. Prepare asset (WebP format)
# 2. Upload to S3
python upload_assets_to_s3.py

# 3. Update HTML with S3 URL
# <img src="https://isnbiz-assets-1769962280...">

# 4. Test and commit
git add index.html
git commit -m "feat: Add new hero image"
git push
```

## Troubleshooting

### Form Not Submitting
```bash
# Check browser console (F12)
# Verify script.js is loading
# Check form ID matches JavaScript
```

### Styles Not Applying
```bash
# Hard refresh browser: Ctrl+Shift+R (Chrome/Edge)
# Check browser console for CSS errors
# Verify styles.css path is correct
```

### Images Not Loading
```bash
# Check S3 URL is correct
# Verify S3 bucket permissions (public read)
# Check browser console for 404 errors
```

## Useful Aliases (Optional)

Add to `.bashrc` or `.bash_profile`:
```bash
alias cdisn='cd /mnt/d/workspace/ISNBIZ_Files'
alias gst='git status'
alias glog='git log --oneline -10'
alias deploy='netlify deploy --prod'
```

## Editor Recommendations

- **VS Code** - Recommended
  - Extensions: Live Server, Prettier, HTMLHint, CSS Peek
- **Sublime Text** - Lightweight alternative
- **Notepad++** - Windows native option

## Next Steps After Task Completion

See `task_completion_workflow.md` for checklist of what to do when a task is done.
