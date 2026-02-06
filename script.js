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
