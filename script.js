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

    // Enforce full rows only in card grids (no partial rows)
    function enforceFullRows() {
        document.querySelectorAll('.portfolio-grid, .solutions-grid').forEach(function(grid) {
            var cards = grid.querySelectorAll('.portfolio-card, .solution-card');
            if (!cards.length) return;
            // Detect column count from computed grid
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
