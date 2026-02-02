# Task Completion Workflow

## What to Do When a Task is Completed

This checklist ensures quality and consistency after completing any development task on the ISN.BIZ website.

## 1. Code Quality Checks

### HTML Validation
```bash
# Test locally first
start index.html  # Or whichever page you modified

# Check for:
- [ ] Proper semantic HTML structure
- [ ] All closing tags present
- [ ] No broken links
- [ ] All images have alt text
- [ ] Forms have proper labels and IDs
```

### CSS Validation
```bash
# Check styles.css for:
- [ ] No hardcoded colors (use CSS variables)
- [ ] Responsive design works (test at 480px, 768px, 992px, 1200px)
- [ ] Animations have prefers-reduced-motion alternative
- [ ] Font sizes >= 1rem (16px) for WCAG compliance
- [ ] Proper indentation and formatting
```

### JavaScript Validation
```bash
# Check script.js for:
- [ ] No console errors (F12 in browser)
- [ ] Event listeners properly attached
- [ ] Feature detection (check if elements exist before using)
- [ ] No inline event handlers
- [ ] Code is inside DOMContentLoaded wrapper
```

## 2. Accessibility Checks (WCAG 2.1 AA)

```bash
# Checklist:
- [ ] All images have descriptive alt text
- [ ] Forms have proper labels (for/id matching)
- [ ] Focus states visible (outline or custom focus styles)
- [ ] Heading hierarchy correct (h1 → h2 → h3)
- [ ] Color contrast ratios meet 4.5:1 (text) or 3:1 (large text)
- [ ] Skip navigation link present and working
- [ ] ARIA labels on interactive elements (buttons, nav toggle)
- [ ] Keyboard navigation works (Tab, Enter, Space)
```

### Test Keyboard Navigation
1. Tab through all interactive elements
2. Verify focus is visible at each step
3. Enter/Space activates buttons and links
4. Escape closes modals/menus (if applicable)

## 3. Browser Testing

### Test in Multiple Browsers
```bash
# Windows browsers:
start chrome index.html       # Google Chrome
start msedge index.html       # Microsoft Edge
start firefox index.html      # Mozilla Firefox

# Test checklist:
- [ ] Chrome (latest)
- [ ] Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (if available via Mac or BrowserStack)
```

### Test Responsive Design
```bash
# Chrome DevTools (F12 > Toggle device toolbar)
- [ ] Mobile (375px - 480px)
- [ ] Tablet (768px - 992px)
- [ ] Desktop (1200px+)
- [ ] Test portrait and landscape orientations
```

### Test on Real Devices
```bash
- [ ] iOS Safari (iPhone/iPad)
- [ ] Android Chrome (phone/tablet)
- [ ] Check touch interactions work properly
```

## 4. Performance Checks

### Lighthouse Audit
```bash
# Chrome DevTools > Lighthouse tab
# Run audit and verify:
- [ ] Performance score: 90+
- [ ] Accessibility score: 100
- [ ] Best Practices score: 90+
- [ ] SEO score: 90+
```

### Load Time Test
```bash
# Check in Network tab (F12):
- [ ] Total page size < 500KB
- [ ] Load time < 3 seconds
- [ ] Images are optimized (WebP format)
- [ ] No render-blocking resources
```

## 5. Content Verification

### Text Review
```bash
- [ ] No typos or grammatical errors
- [ ] Company information is accurate (DUNS, UBI, EIN)
- [ ] Contact information is current
- [ ] CTAs are clear and compelling
- [ ] Links open in appropriate target (_self or _blank)
```

### Image Verification
```bash
- [ ] All images loading from S3 correctly
- [ ] Images are appropriate size/quality
- [ ] WebP format with fallback (if needed)
- [ ] Alt text is descriptive
- [ ] OG images (1200x630px) for social sharing
```

## 6. Git Workflow

### Before Committing
```bash
# Review changes
git status
git diff

# Check what you're committing:
- [ ] Only relevant files are staged
- [ ] No sensitive data (API keys, passwords)
- [ ] No debug code left in (console.log, alert, etc.)
- [ ] No commented-out code (unless intentional)
```

### Commit Changes
```bash
# Stage specific files (preferred)
git add index.html
git add styles.css
git add script.js

# Commit with clear message
git commit -m "feat: Add new investor section"
# or
git commit -m "fix: Mobile menu toggle issue on iOS"
# or
git commit -m "style: Update button hover effects"

# Push to remote
git push origin main
```

### Commit Message Format
```
<type>: <short description>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation update
- style: Code style/formatting (no logic change)
- refactor: Code refactoring
- perf: Performance improvement
- test: Add/update tests
- chore: Maintenance tasks
```

## 7. Deployment Preparation

### Pre-Deploy Checklist
```bash
- [ ] All changes committed and pushed
- [ ] Tested locally in multiple browsers
- [ ] Accessibility checks passed
- [ ] Performance checks passed
- [ ] No console errors or warnings
- [ ] All links working
- [ ] Forms functioning correctly
- [ ] Mobile responsiveness verified
```

### Deploy to Netlify
```bash
# Option 1: Auto-deploy via Git
git push origin main
# Netlify will auto-deploy if connected to repo

# Option 2: Manual deploy via CLI
netlify deploy --prod

# Option 3: Drag-and-drop to Netlify dashboard
# Visit https://app.netlify.com/
```

### Post-Deploy Verification
```bash
# After deployment:
- [ ] Visit live URL and verify changes
- [ ] Test all modified pages
- [ ] Check mobile version on real device
- [ ] Verify forms still work
- [ ] Check SSL certificate (HTTPS)
- [ ] Run Lighthouse audit on live site
```

## 8. Documentation Updates

### Update Project Documentation
```bash
# If significant changes made:
- [ ] Update README.md
- [ ] Update CLAUDE.md (if architecture changed)
- [ ] Add/update comments in code
- [ ] Create/update docs/ file if needed
```

### Document Decisions
```bash
# If you made important decisions:
- [ ] Document why you chose a particular approach
- [ ] Add comments explaining complex code
- [ ] Update style guide if new patterns introduced
```

## 9. Cleanup

### Remove Temporary Files
```bash
# Check for and remove:
- [ ] Backup files (*.bak, *~, *.tmp)
- [ ] Test files not needed in production
- [ ] Debug scripts or temporary code
- [ ] Unused images or assets
```

### Optimize Assets
```bash
# If added new images:
- [ ] Convert to WebP format
- [ ] Optimize file size
- [ ] Upload to S3
- [ ] Update HTML with S3 URLs
- [ ] Verify images load correctly
```

## 10. Communication

### Update Stakeholders
```bash
# If applicable:
- [ ] Notify team of changes
- [ ] Update project status
- [ ] Share preview link if needed
- [ ] Document any breaking changes
```

## Quick Checklist (for Small Changes)

For minor updates, use this abbreviated checklist:

```bash
□ Test locally (open in browser)
□ No console errors (F12)
□ Works on mobile (Chrome DevTools)
□ Git status clean
□ Commit with clear message
□ Push to remote
□ Verify live site (if auto-deploy)
```

## Automation Opportunities

### Pre-commit Hooks (Optional)
Consider setting up Git hooks for:
- HTML validation
- CSS linting
- JavaScript linting
- Accessibility checks

### CI/CD Pipeline (Optional)
For larger teams, consider:
- GitHub Actions
- Netlify build plugins
- Automated Lighthouse audits

## Common Issues and Solutions

### "Changes not showing on live site"
```bash
# Solution 1: Hard refresh browser
Ctrl+Shift+R (Chrome/Edge)
Cmd+Shift+R (Mac)

# Solution 2: Clear browser cache
# Chrome: Settings > Privacy > Clear browsing data

# Solution 3: Check deployment status
netlify status
netlify logs
```

### "CSS not applying"
```bash
# Check:
1. Browser cache (hard refresh)
2. CSS file path is correct
3. No CSS syntax errors (check browser console)
4. Specificity issues (use DevTools to inspect)
```

### "Form not working"
```bash
# Check:
1. JavaScript console for errors
2. Form ID matches JavaScript
3. Event listeners attached
4. Form backend configured (if not using alert placeholder)
```

## When to Skip Steps

### Skip if:
- Fixing typo in documentation
- Updating comments only
- Making config changes (not code)

### Don't skip:
- Any code changes (HTML/CSS/JS)
- Changes affecting user-facing content
- Changes affecting functionality

## Final Reminder

**Always prioritize:**
1. **User experience** - Does it work well?
2. **Accessibility** - Can everyone use it?
3. **Performance** - Is it fast?
4. **Quality** - Is the code clean and maintainable?

When in doubt, test more thoroughly rather than less.
