/* ================================
   ENHANCED INTERACTIONS & ANIMATIONS
   ISN.BIZ Premium JavaScript
   ================================ */

document.addEventListener('DOMContentLoaded', function() {

    // ================================
    // SCROLL PROGRESS INDICATOR
    // ================================
    const createScrollProgress = () => {
        const progress = document.createElement('div');
        progress.className = 'scroll-progress';
        document.body.appendChild(progress);

        window.addEventListener('scroll', () => {
            const winScroll = document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            progress.style.width = scrolled + '%';
        }, { passive: true });
    };

    // ================================
    // SCROLL-TRIGGERED ANIMATIONS
    // ================================
    const observeElements = () => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        });

        // Observe all sections
        document.querySelectorAll('.section').forEach(section => {
            observer.observe(section);
        });

        // Observe solution cards for staggered animation
        document.querySelectorAll('.solution-card').forEach((card, index) => {
            card.style.transitionDelay = `${index * 0.1}s`;
            observer.observe(card);
        });

        // Observe portfolio items
        document.querySelectorAll('.portfolio-item').forEach((item, index) => {
            item.style.transitionDelay = `${index * 0.15}s`;
            observer.observe(item);
        });
    };

    // ================================
    // NAVIGATION SCROLL EFFECT
    // ================================
    const enhanceNavigation = () => {
        const nav = document.querySelector('.nav');
        let lastScroll = 0;

        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;

            if (currentScroll > 100) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }

            lastScroll = currentScroll;
        }, { passive: true });
    };

    // ================================
    // PARALLAX EFFECTS
    // ================================
    const createParallax = () => {
        const parallaxElements = document.querySelectorAll('.parallax');

        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;

            parallaxElements.forEach(el => {
                const speed = el.dataset.speed || 0.5;
                el.style.transform = `translateY(${scrolled * speed}px)`;
            });
        }, { passive: true });
    };

    // ================================
    // STAT NUMBER ANIMATION
    // ================================
    const animateNumbers = () => {
        const stats = document.querySelectorAll('.stat-number');

        const animateValue = (element, start, end, duration) => {
            const range = end - start;
            const increment = range / (duration / 16);
            let current = start;

            const timer = setInterval(() => {
                current += increment;
                if (current >= end) {
                    element.textContent = end;
                    clearInterval(timer);
                } else {
                    element.textContent = Math.floor(current);
                }
            }, 16);
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                    entry.target.classList.add('counted');
                    const text = entry.target.textContent;
                    const num = parseInt(text);

                    if (!isNaN(num)) {
                        entry.target.textContent = '0';
                        setTimeout(() => {
                            animateValue(entry.target, 0, num, 2000);
                        }, 300);
                    }
                }
            });
        }, { threshold: 0.5 });

        stats.forEach(stat => observer.observe(stat));
    };

    // ================================
    // MAGNETIC BUTTONS
    // ================================
    const createMagneticButtons = () => {
        const buttons = document.querySelectorAll('.btn');

        buttons.forEach(button => {
            button.addEventListener('mousemove', (e) => {
                const rect = button.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;

                button.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px) translateY(-2px)`;
            });

            button.addEventListener('mouseleave', () => {
                button.style.transform = '';
            });
        });
    };

    // ================================
    // SMOOTH SCROLL WITH OFFSET
    // ================================
    const enhancedSmoothScroll = () => {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    const navHeight = document.querySelector('.nav').offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    };

    // ================================
    // CURSOR TRAIL EFFECT
    // ================================
    const createCursorTrail = () => {
        const coords = { x: 0, y: 0 };
        const circles = document.querySelectorAll('.cursor-circle');

        if (circles.length === 0) {
            // Create cursor trail circles
            for (let i = 0; i < 8; i++) {
                const circle = document.createElement('div');
                circle.className = 'cursor-circle';
                circle.style.cssText = `
                    position: fixed;
                    width: ${8 - i}px;
                    height: ${8 - i}px;
                    border-radius: 50%;
                    background: rgba(30, 159, 242, ${0.5 - i * 0.06});
                    pointer-events: none;
                    z-index: 9998;
                    transition: transform 0.${2 + i}s ease-out;
                `;
                document.body.appendChild(circle);
            }
        }

        window.addEventListener('mousemove', (e) => {
            coords.x = e.clientX;
            coords.y = e.clientY;
        });

        const circles2 = document.querySelectorAll('.cursor-circle');
        circles2.forEach((circle, index) => {
            circle.animate({
                left: [circle.offsetLeft + 'px', coords.x + 'px'],
                top: [circle.offsetTop + 'px', coords.y + 'px']
            }, {
                duration: 1000 - index * 100,
                fill: 'forwards',
                easing: 'ease-out'
            });
        });

        setInterval(() => {
            circles2.forEach((circle) => {
                circle.style.left = coords.x + 'px';
                circle.style.top = coords.y + 'px';
            });
        }, 50);
    };

    // ================================
    // TECH GRID ANIMATION
    // ================================
    const createTechGrid = () => {
        const sections = document.querySelectorAll('.section');

        sections.forEach(section => {
            if (!section.querySelector('.tech-grid-bg')) {
                const grid = document.createElement('div');
                grid.className = 'tech-grid-bg';
                grid.style.cssText = `
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background-image:
                        linear-gradient(rgba(30, 159, 242, 0.02) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(30, 159, 242, 0.02) 1px, transparent 1px);
                    background-size: 40px 40px;
                    pointer-events: none;
                    opacity: 0;
                    transition: opacity 0.6s;
                `;
                section.style.position = 'relative';
                section.insertBefore(grid, section.firstChild);
            }
        });
    };

    // ================================
    // FORM HANDLING (Enhanced)
    // ================================
    const enhanceForm = () => {
        const contactForm = document.getElementById('contactForm');
        if (contactForm) {
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();

                // Add loading state
                const submitBtn = this.querySelector('button[type="submit"]');
                const originalText = submitBtn.textContent;
                submitBtn.textContent = 'Sending...';
                submitBtn.disabled = true;
                submitBtn.style.opacity = '0.6';

                // Simulate submission (replace with actual backend)
                setTimeout(() => {
                    submitBtn.textContent = '✓ Sent!';
                    submitBtn.style.background = 'linear-gradient(135deg, #10B981, #059669)';

                    setTimeout(() => {
                        contactForm.reset();
                        submitBtn.textContent = originalText;
                        submitBtn.disabled = false;
                        submitBtn.style.opacity = '1';
                        submitBtn.style.background = '';
                    }, 2000);
                }, 1000);
            });

            // Add floating labels effect
            const inputs = contactForm.querySelectorAll('input, textarea, select');
            inputs.forEach(input => {
                input.addEventListener('focus', function() {
                    this.parentElement.classList.add('focused');
                });

                input.addEventListener('blur', function() {
                    if (!this.value) {
                        this.parentElement.classList.remove('focused');
                    }
                });
            });
        }
    };

    // ================================
    // MOBILE MENU ENHANCEMENT
    // ================================
    const enhanceMobileMenu = () => {
        const toggle = document.querySelector('.nav-toggle');
        const menu = document.querySelector('.nav-menu');

        if (toggle && menu) {
            toggle.addEventListener('click', () => {
                const isOpen = toggle.getAttribute('aria-expanded') === 'true';
                toggle.setAttribute('aria-expanded', !isOpen);
                menu.classList.toggle('active');
                document.body.style.overflow = isOpen ? '' : 'hidden';

                // Animate menu items
                if (!isOpen) {
                    menu.querySelectorAll('li').forEach((item, index) => {
                        item.style.animation = `fadeInLeft 0.4s cubic-bezier(0.16, 1, 0.3, 1) ${index * 0.1}s both`;
                    });
                }
            });

            // Close menu when clicking a link
            menu.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    toggle.setAttribute('aria-expanded', 'false');
                    menu.classList.remove('active');
                    document.body.style.overflow = '';
                });
            });
        }
    };

    // ================================
    // INITIALIZE ALL ENHANCEMENTS
    // ================================

    createScrollProgress();
    observeElements();
    enhanceNavigation();
    createParallax();
    animateNumbers();
    createMagneticButtons();
    enhancedSmoothScroll();
    createTechGrid();
    enhanceForm();
    enhanceMobileMenu();

    // Only enable cursor trail on desktop
    if (window.innerWidth > 1024) {
        createCursorTrail();
    }

    console.log('✨ Enhanced interactions loaded');
});

// ================================
// PERFORMANCE: Passive listeners
// ================================
window.addEventListener('scroll', () => {}, { passive: true });
window.addEventListener('touchstart', () => {}, { passive: true });
