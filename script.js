document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you! We will contact you within 24 hours.');
            contactForm.reset();
        });
    }
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) target.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // Scroll-triggered section visibility (required by enhanced-animations.css)
    var sections = document.querySelectorAll('.section');
    if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });
        sections.forEach(function(s) { observer.observe(s); });
    } else {
        sections.forEach(function(s) { s.classList.add('visible'); });
    }

    // Nav scroll effect
    var nav = document.querySelector('.nav');
    if (nav) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });
    }

    // Mobile nav toggle
    var toggle = document.querySelector('.nav-toggle');
    var menu = document.querySelector('.nav-menu');
    if (toggle && menu) {
        toggle.addEventListener('click', function() {
            var expanded = toggle.getAttribute('aria-expanded') === 'true';
            toggle.setAttribute('aria-expanded', !expanded);
            menu.classList.toggle('active');
        });
    }

    // HROC benefactor banner — injected above the footer on every page
    // except /hroc-files itself. iSN.BiZ Inc directs charitable proceeds to HROC Inc (501(c)(3)).
    (function injectHrocBanner() {
        if (document.getElementById('hroc-benefactor-banner')) return;
        var path = window.location.pathname.replace(/\/+$/, '') || '/';
        if (path === '/hroc-files') return;
        var footer = document.querySelector('footer.footer');
        if (!footer) return;
        var banner = document.createElement('section');
        banner.id = 'hroc-benefactor-banner';
        banner.setAttribute('aria-label', 'HROC 501(c)(3) beneficiary');
        banner.style.cssText = 'background: var(--color-charcoal); border-top: 1px solid rgba(95, 223, 223, 0.18); padding: 1.25rem 1rem;';
        banner.innerHTML = [
            '<div class="container" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:0.5rem 0.85rem;text-align:center;">',
            '  <span style="color: var(--color-cyan); font-family: \'JetBrains Mono\', monospace; letter-spacing: 0.05em; text-transform: uppercase; font-size: 0.78rem; padding: 0.22rem 0.6rem; border: 1px solid rgba(95, 223, 223, 0.3); border-radius: 999px;">501(c)(3) Beneficiary</span>',
            '  <span style="color: rgba(240,244,248,0.88); font-size: 0.95rem;">iSN.BiZ Inc directs charitable proceeds to <a href="/hroc-files" style="color: var(--color-cyan); text-decoration: underline;">HROC Inc</a> &mdash; harm-reduction operations for vulnerable communities.</span>',
            '</div>'
        ].join('');
        footer.parentNode.insertBefore(banner, footer);
    })();

    // Enforce full rows only in card grids (no partial rows)
    function enforceFullRows() {
        document.querySelectorAll('.portfolio-grid, .solutions-grid').forEach(function(grid) {
            var cards = grid.querySelectorAll('.portfolio-card, .solution-card');
            if (!cards.length) return;
            var cols = getComputedStyle(grid).gridTemplateColumns.split(' ').length;
            var total = cards.length;
            var visible = Math.floor(total / cols) * cols;
            cards.forEach(function(card, i) {
                card.style.display = i < visible ? '' : 'none';
            });
        });
    }
    enforceFullRows();
    window.addEventListener('resize', enforceFullRows);
});
