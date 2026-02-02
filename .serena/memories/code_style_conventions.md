# Code Style and Conventions

## HTML Style

### Structure
- **Semantic HTML5** - Use proper semantic elements (`<nav>`, `<section>`, `<article>`, `<header>`, `<footer>`)
- **WCAG 2.1 AA Compliant** - All accessibility requirements met
- **Indentation:** 4 spaces
- **Comments:** Section markers with clear labels

### Patterns
```html
<!-- Section Comment -->
<section class="section-name">
    <div class="container">
        <h2>Section Title</h2>
        <p>Content here...</p>
    </div>
</section>
```

### Accessibility Requirements
- **Skip links:** Provided for keyboard navigation
- **ARIA labels:** Used on interactive elements (nav-toggle, form inputs)
- **Alt text:** Required on ALL images
- **Focus states:** Visible outlines (never `outline: none` without replacement)
- **Semantic headings:** Proper hierarchy (h1 → h2 → h3)

### Meta Tags Pattern
```html
<meta name="description" content="...">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://isnbiz-assets...">
<meta name="twitter:card" content="summary_large_image">
```

## CSS Style

### Methodology: Neo-Technical Brutalism
- **Custom Properties** - All colors, fonts, spacing in `:root`
- **Mobile-First** - Base styles for mobile, media queries for larger screens
- **BEM-inspired naming** - `.section-name`, `.section-name__element`, `.section-name--modifier`

### File Organization
```css
/* 1. CSS Variables (`:root`)
   2. Reset/Base styles
   3. Typography
   4. Layout (container, grid, flex)
   5. Components (buttons, cards, forms)
   6. Sections (hero, about, portfolio, etc.)
   7. Media queries (grouped at end)
   8. Utilities */
```

### Naming Conventions
- **Sections:** `.hero`, `.about`, `.solutions`, `.portfolio`, `.investors`, `.contact`
- **Components:** `.card`, `.button`, `.nav`, `.form`
- **Modifiers:** `.button--primary`, `.card--featured`
- **States:** `.is-active`, `.is-open`, `.is-loading`

### Colors
**ALWAYS use CSS custom properties, NEVER hardcode hex values:**
```css
/* CORRECT */
color: var(--color-blue);
background: var(--color-charcoal);

/* WRONG */
color: #1E9FF2;
background: #0D1117;
```

### Typography
- **Minimum font-size:** 1rem (16px) for WCAG compliance
- **Line height:** 1.6 for body text, 1.2 for headings
- **Font stacks:** Use CSS variables (`var(--font-mono)`, `var(--font-display)`, `var(--font-body)`)

### Responsive Breakpoints
```css
/* Mobile: < 480px (base styles) */
/* Tablet: 480px - 768px */
@media (min-width: 480px) { ... }

/* Desktop: 768px - 992px */
@media (min-width: 768px) { ... }

/* Large: 992px - 1200px */
@media (min-width: 992px) { ... }

/* XL: > 1200px */
@media (min-width: 1200px) { ... }
```

### Animations
- **Always provide:** `prefers-reduced-motion` alternative
- **Duration:** 0.3s for most transitions
- **Easing:** `cubic-bezier(0.4, 0, 0.2, 1)` or CSS custom property `var(--transition)`

```css
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

## JavaScript Style

### Approach
- **Vanilla JS** - No frameworks, no build tools
- **ES6+** - Modern JavaScript (arrow functions, const/let, template literals)
- **Progressive Enhancement** - Site works without JS

### Patterns
```javascript
// Use addEventListener, NOT inline handlers
document.addEventListener('DOMContentLoaded', function() {
    const element = document.getElementById('elementId');
    if (element) {
        element.addEventListener('click', handleClick);
    }
});

// Arrow functions for callbacks
const handleClick = (e) => {
    e.preventDefault();
    // Handle event
};

// Use querySelectorAll for multiple elements
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', handleNavigation);
});
```

### Code Organization
1. **DOMContentLoaded wrapper** - All code inside this
2. **Feature detection** - Check if elements exist before using
3. **Event delegation** - When appropriate
4. **Descriptive names** - `contactForm` not `form1`

### Current Features
- **Form handling:** Prevent default, show alert (placeholder), reset form
- **Smooth scrolling:** For anchor links
- **Mobile menu toggle:** (if implemented in nav)

## Git Conventions

### Commit Messages
```bash
# Format: <type>: <description>

# Types:
feat: Add new feature
fix: Bug fix
docs: Documentation update
style: Code style changes (formatting, no logic change)
refactor: Code refactoring
perf: Performance improvement
test: Add or update tests
chore: Maintenance tasks

# Examples:
git commit -m "feat: Add investor section to homepage"
git commit -m "fix: Mobile menu toggle on iOS Safari"
git commit -m "docs: Update deployment instructions"
git commit -m "style: Format CSS according to style guide"
```

### Branch Strategy
```bash
# Main branch: main (production-ready)
# Feature branches: feature/description
# Fix branches: fix/description
# Hotfix branches: hotfix/description

git checkout -b feature/add-blog-section
git checkout -b fix/mobile-nav-issue
```

## Asset Guidelines

### Images
- **Format:** WebP preferred (with fallback if needed)
- **Hosting:** S3 bucket (isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com)
- **Naming:** Descriptive, lowercase, hyphens (not underscores)
  - `hero-background.webp` not `HeroBackground.webp`
- **Alt text:** Always required, descriptive

### Logos
- **Location:** S3 /premium_v3/logos/
- **Variants:** navbar_logo.webp, favicon.webp, apple_touch_icon.webp
- **Usage:** Always via S3 URLs, not local paths

## Design Principles

1. **Brutalist Aesthetic** - Bold, functional, asymmetric
2. **High Contrast** - Ensure readability (WCAG AAA where possible)
3. **Technical Feel** - Monospace fonts, grid patterns, industrial textures
4. **Investor-Ready** - Professional, trustworthy, clear CTAs
5. **Performance First** - Minimal JS, optimized assets, fast load

## Documentation Standards

### Code Comments
```html
<!-- ================================
     SECTION NAME
     Description of section purpose
     ================================ -->

```

```css
/* ================================
   COMPONENT NAME
   ================================ */

/* Modifier: description */
```

```javascript
// Feature: Description
// Handles: What it does
```

### File Headers
```css
/* ================================
   NEO-TECHNICAL BRUTALISM DESIGN
   ISN.BIZ - Distinctive Frontend
   ================================ */
```

## Common Patterns

### Button Pattern
```html
<a href="#contact" class="button button--primary">
    Contact Us
</a>
```

### Card Pattern
```html
<div class="card">
    <h3 class="card__title">Title</h3>
    <p class="card__description">Description</p>
</div>
```

### Form Pattern
```html
<form id="contactForm" class="form">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" required>
    
    <button type="submit" class="button button--primary">
        Submit
    </button>
</form>
```

## Anti-Patterns (DON'T DO THIS)

❌ Hardcode colors: `color: #1E9FF2`
✅ Use variables: `color: var(--color-blue)`

❌ Inline styles: `<div style="color: red">`
✅ CSS classes: `<div class="error-message">`

❌ Inline JS: `<button onclick="handleClick()">`
✅ addEventListener: `button.addEventListener('click', handleClick)`

❌ Non-semantic: `<div class="title">`
✅ Semantic: `<h2 class="title">`

❌ No alt text: `<img src="logo.png">`
✅ Descriptive alt: `<img src="logo.png" alt="ISN.BIZ Inc Logo">`
