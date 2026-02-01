/* ========================================
   VIDEO & SLIDER COMPONENTS SCRIPTS
   iSN.BiZ Inc - Modern Web Components
   ======================================== */

// ========================================
// Initialize AOS (Animate On Scroll)
// ========================================
AOS.init({
    duration: 1000,
    easing: 'ease-out-cubic',
    once: true,
    offset: 100,
    disable: 'mobile' // Disable on mobile for performance
});

// ========================================
// COMPONENT 1: HERO VIDEO BACKGROUND
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    const heroVideo = document.getElementById('hero-video');
    const videoToggle = document.getElementById('video-toggle');
    const playIcon = videoToggle.querySelector('.play-icon');
    const pauseIcon = videoToggle.querySelector('.pause-icon');

    // Autoplay video on desktop only
    if (window.innerWidth > 768 && heroVideo) {
        heroVideo.play().catch(error => {
            console.log('Autoplay prevented:', error);
            // Show play icon if autoplay fails
            playIcon.classList.remove('hidden');
            pauseIcon.classList.add('hidden');
        });

        // Set initial button state (playing)
        playIcon.classList.add('hidden');
        pauseIcon.classList.remove('hidden');
    }

    // Video play/pause toggle
    if (videoToggle && heroVideo) {
        videoToggle.addEventListener('click', function() {
            if (heroVideo.paused) {
                heroVideo.play();
                playIcon.classList.add('hidden');
                pauseIcon.classList.remove('hidden');
                videoToggle.setAttribute('aria-label', 'Pause background video');
            } else {
                heroVideo.pause();
                playIcon.classList.remove('hidden');
                pauseIcon.classList.add('hidden');
                videoToggle.setAttribute('aria-label', 'Play background video');
            }
        });
    }

    // Pause video on visibility change (performance)
    document.addEventListener('visibilitychange', function() {
        if (document.hidden && heroVideo) {
            heroVideo.pause();
        } else if (!document.hidden && heroVideo && window.innerWidth > 768) {
            heroVideo.play().catch(e => console.log('Play prevented:', e));
        }
    });
});

// ========================================
// COMPONENT 2: ANIMATED STATISTICS
// ========================================

// Animated Counter Function
function animateCounter(element, start, end, duration) {
    let startTime = null;
    const suffix = element.parentElement.querySelector('.stat-suffix');
    const suffixText = suffix ? suffix.textContent : '';

    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const progress = Math.min(timeElapsed / duration, 1);

        // Easing function (easeOutCubic)
        const easeOutCubic = 1 - Math.pow(1 - progress, 3);
        const current = Math.floor(easeOutCubic * (end - start) + start);

        element.textContent = current.toLocaleString();

        if (progress < 1) {
            requestAnimationFrame(animation);
        } else {
            element.textContent = end.toLocaleString();
        }
    }

    requestAnimationFrame(animation);
}

// Intersection Observer for Stats
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statNumber = entry.target.querySelector('.stat-number');
            const targetValue = parseInt(statNumber.getAttribute('data-count'));

            animateCounter(statNumber, 0, targetValue, 2000);

            // Unobserve after animation
            statsObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.5
});

// Observe all stat cards
document.querySelectorAll('.stat-card').forEach(card => {
    statsObserver.observe(card);
});

// ========================================
// COMPONENT 3: TESTIMONIAL SLIDER
// ========================================

const testimonialSwiper = new Swiper('.testimonial-swiper', {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true
    },
    pagination: {
        el: '.testimonial-pagination',
        clickable: true,
        dynamicBullets: true
    },
    navigation: {
        nextEl: '.testimonial-next',
        prevEl: '.testimonial-prev',
    },
    breakpoints: {
        768: {
            slidesPerView: 1
        },
        992: {
            slidesPerView: 1
        }
    },
    effect: 'fade',
    fadeEffect: {
        crossFade: true
    },
    // Accessibility
    a11y: {
        prevSlideMessage: 'Previous testimonial',
        nextSlideMessage: 'Next testimonial',
        firstSlideMessage: 'This is the first testimonial',
        lastSlideMessage: 'This is the last testimonial',
        paginationBulletMessage: 'Go to testimonial {{index}}'
    }
});

// Testimonial autoplay toggle (accessibility)
const testimonialToggle = document.getElementById('testimonial-toggle');
if (testimonialToggle) {
    const playIcon = testimonialToggle.querySelector('.play-icon');
    const pauseIcon = testimonialToggle.querySelector('.pause-icon');
    let isPlaying = true;

    testimonialToggle.addEventListener('click', function() {
        if (isPlaying) {
            testimonialSwiper.autoplay.stop();
            playIcon.classList.remove('hidden');
            pauseIcon.classList.add('hidden');
            testimonialToggle.setAttribute('aria-label', 'Play testimonial slider');
            isPlaying = false;
        } else {
            testimonialSwiper.autoplay.start();
            playIcon.classList.add('hidden');
            pauseIcon.classList.remove('hidden');
            testimonialToggle.setAttribute('aria-label', 'Pause testimonial slider');
            isPlaying = true;
        }
    });
}

// ========================================
// COMPONENT 4: PORTFOLIO CAROUSEL
// ========================================

const portfolioSwiper = new Swiper('.portfolio-swiper', {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true
    },
    pagination: {
        el: '.portfolio-pagination',
        clickable: true,
        dynamicBullets: true
    },
    navigation: {
        nextEl: '.portfolio-button-next',
        prevEl: '.portfolio-button-prev',
    },
    breakpoints: {
        640: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 30
        }
    },
    // Lazy loading
    lazy: {
        loadPrevNext: true,
        loadPrevNextAmount: 2
    },
    // Accessibility
    a11y: {
        prevSlideMessage: 'Previous project',
        nextSlideMessage: 'Next project',
        paginationBulletMessage: 'Go to project {{index}}'
    }
});

// ========================================
// COMPONENT 5: VIDEO PLAYER (PLYR)
// ========================================

const productDemoVideo = document.getElementById('product-demo-video');
if (productDemoVideo) {
    const player = new Plyr(productDemoVideo, {
        controls: [
            'play-large',
            'play',
            'progress',
            'current-time',
            'duration',
            'mute',
            'volume',
            'captions',
            'settings',
            'pip',
            'airplay',
            'fullscreen'
        ],
        settings: ['captions', 'quality', 'speed'],
        captions: {
            active: true,
            language: 'en',
            update: true
        },
        quality: {
            default: 720,
            options: [1080, 720, 480]
        },
        speed: {
            selected: 1,
            options: [0.5, 0.75, 1, 1.25, 1.5, 2]
        },
        tooltips: {
            controls: true,
            seek: true
        },
        // Analytics tracking
        listeners: {
            play: () => console.log('Video played'),
            pause: () => console.log('Video paused'),
            ended: () => console.log('Video ended')
        }
    });

    // Track video engagement
    player.on('play', function() {
        // Send to analytics (Google Analytics, etc.)
        if (typeof gtag !== 'undefined') {
            gtag('event', 'video_play', {
                'event_category': 'engagement',
                'event_label': 'Product Demo Video'
            });
        }
    });

    player.on('ended', function() {
        // Track video completion
        if (typeof gtag !== 'undefined') {
            gtag('event', 'video_complete', {
                'event_category': 'engagement',
                'event_label': 'Product Demo Video'
            });
        }
    });
}

// ========================================
// COMPONENT 6: PARALLAX EFFECTS (GSAP)
// ========================================

// Register GSAP ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Hero parallax on scroll
gsap.to('.hero-video-overlay', {
    opacity: 1,
    scrollTrigger: {
        trigger: '.hero-video-section',
        start: 'top top',
        end: 'bottom top',
        scrub: 1
    }
});

// Parallax section layers
if (document.querySelector('.parallax-section')) {
    // Background layer (slower)
    gsap.to('.parallax-bg', {
        y: 200,
        scrollTrigger: {
            trigger: '.parallax-section',
            start: 'top bottom',
            end: 'bottom top',
            scrub: 1
        }
    });

    // Content layer (normal speed)
    gsap.to('.parallax-content', {
        y: 0,
        scrollTrigger: {
            trigger: '.parallax-section',
            start: 'top bottom',
            end: 'bottom top',
            scrub: 1
        }
    });

    // Foreground layer (faster)
    gsap.to('.parallax-fg', {
        y: -150,
        scrollTrigger: {
            trigger: '.parallax-section',
            start: 'top bottom',
            end: 'bottom top',
            scrub: 1
        }
    });

    // Parallax shapes rotation
    gsap.to('.parallax-shape', {
        rotation: 360,
        duration: 20,
        ease: 'none',
        repeat: -1
    });

    // Individual shape movements
    gsap.to('.shape-1', {
        x: 50,
        y: -50,
        scrollTrigger: {
            trigger: '.parallax-section',
            start: 'top bottom',
            end: 'bottom top',
            scrub: 2
        }
    });

    gsap.to('.shape-2', {
        x: -30,
        y: 30,
        scrollTrigger: {
            trigger: '.parallax-section',
            start: 'top bottom',
            end: 'bottom top',
            scrub: 1.5
        }
    });
}

// Fade in sections on scroll
gsap.utils.toArray('.section').forEach(section => {
    gsap.from(section, {
        opacity: 0,
        y: 50,
        duration: 1,
        scrollTrigger: {
            trigger: section,
            start: 'top 80%',
            end: 'top 50%',
            toggleActions: 'play none none reverse'
        }
    });
});

// Stats counter with ScrollTrigger
gsap.from('.stat-card', {
    scale: 0.8,
    opacity: 0,
    duration: 0.6,
    stagger: 0.1,
    scrollTrigger: {
        trigger: '.stats-section',
        start: 'top 70%',
        toggleActions: 'play none none reverse'
    }
});

// ========================================
// COMPONENT 7: LOADING ANIMATION
// ========================================

const loadingScreen = document.getElementById('loading-screen');
const progressBar = document.getElementById('progress-bar');
const lottieContainer = document.getElementById('lottie-loader');

// Simulate loading progress
let progress = 0;
const loadingInterval = setInterval(() => {
    progress += Math.random() * 15;
    if (progress >= 100) {
        progress = 100;
        clearInterval(loadingInterval);

        // Hide loading screen after complete
        setTimeout(() => {
            loadingScreen.classList.add('loaded');
        }, 500);
    }

    progressBar.style.width = progress + '%';
}, 200);

// Try to load Lottie animation
if (typeof lottie !== 'undefined' && lottieContainer) {
    // Try loading a Lottie animation (example URL - replace with actual animation)
    try {
        const animation = lottie.loadAnimation({
            container: lottieContainer,
            renderer: 'svg',
            loop: true,
            autoplay: true,
            // Use a generic loading animation from LottieFiles
            path: 'https://assets5.lottiefiles.com/packages/lf20_usmfx6bp.json'
        });
    } catch (error) {
        console.log('Lottie failed, using fallback spinner');
        document.querySelector('.fallback-spinner').style.display = 'block';
        lottieContainer.style.display = 'none';
    }
} else {
    // Show fallback spinner if Lottie not available
    document.querySelector('.fallback-spinner').style.display = 'block';
    if (lottieContainer) lottieContainer.style.display = 'none';
}

// Force remove loading screen after 5 seconds (fallback)
setTimeout(() => {
    loadingScreen.classList.add('loaded');
}, 5000);

// ========================================
// SMOOTH SCROLL
// ========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));

        if (target) {
            const offsetTop = target.offsetTop - 80; // Account for fixed nav

            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// ========================================
// LAZY LOADING IMAGES
// ========================================

if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// ========================================
// PERFORMANCE OPTIMIZATION
// ========================================

// Throttle scroll events
function throttle(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Debounce resize events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Update on window resize (debounced)
window.addEventListener('resize', debounce(() => {
    // Reinitialize components if needed
    ScrollTrigger.refresh();
}, 250));

// ========================================
// ACCESSIBILITY ENHANCEMENTS
// ========================================

// Skip to main content
const skipLink = document.createElement('a');
skipLink.href = '#main-content';
skipLink.className = 'skip-link';
skipLink.textContent = 'Skip to main content';
document.body.insertBefore(skipLink, document.body.firstChild);

// Keyboard navigation for sliders
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
        if (testimonialSwiper && document.activeElement.closest('.testimonial-swiper')) {
            testimonialSwiper.slidePrev();
        }
        if (portfolioSwiper && document.activeElement.closest('.portfolio-swiper')) {
            portfolioSwiper.slidePrev();
        }
    } else if (e.key === 'ArrowRight') {
        if (testimonialSwiper && document.activeElement.closest('.testimonial-swiper')) {
            testimonialSwiper.slideNext();
        }
        if (portfolioSwiper && document.activeElement.closest('.portfolio-swiper')) {
            portfolioSwiper.slideNext();
        }
    }
});

// Pause animations on prefers-reduced-motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    // Disable autoplay
    if (testimonialSwiper) testimonialSwiper.autoplay.stop();
    if (portfolioSwiper) portfolioSwiper.autoplay.stop();

    // Pause video
    const heroVideo = document.getElementById('hero-video');
    if (heroVideo) heroVideo.pause();

    // Disable AOS animations
    AOS.init({
        disable: true
    });
}

// ========================================
// ANALYTICS & TRACKING
// ========================================

// Track slider interactions
if (testimonialSwiper) {
    testimonialSwiper.on('slideChange', function() {
        if (typeof gtag !== 'undefined') {
            gtag('event', 'testimonial_view', {
                'event_category': 'engagement',
                'event_label': 'Slide ' + (testimonialSwiper.realIndex + 1)
            });
        }
    });
}

if (portfolioSwiper) {
    portfolioSwiper.on('slideChange', function() {
        if (typeof gtag !== 'undefined') {
            gtag('event', 'portfolio_view', {
                'event_category': 'engagement',
                'event_label': 'Project ' + (portfolioSwiper.realIndex + 1)
            });
        }
    });
}

// Track CTA clicks
document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        const buttonText = this.textContent.trim();
        if (typeof gtag !== 'undefined') {
            gtag('event', 'cta_click', {
                'event_category': 'engagement',
                'event_label': buttonText
            });
        }
    });
});

// ========================================
// CONSOLE BRANDING
// ========================================

console.log('%c iSN.BiZ Inc ', 'background: linear-gradient(135deg, #1E9FF2 0%, #5FDFDF 100%); color: white; font-size: 24px; padding: 10px 20px; border-radius: 8px;');
console.log('%c Building the Future with AI ', 'color: #1E9FF2; font-size: 14px; font-weight: 600;');
console.log('%c https://isn.biz ', 'color: #6c757d; font-size: 12px;');
console.log('');
console.log('Interested in working with us? Contact: info@isn.biz');
