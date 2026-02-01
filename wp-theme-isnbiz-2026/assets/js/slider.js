/**
 * Slider & Gallery Initialization - Swiper 11
 * iSN.BiZ Inc - 2026
 *
 * Modern, performance-optimized slider implementations
 * with accessibility and mobile-first design
 */

// ================================
// Utility: Reduced Motion Detection
// ================================
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Adjust autoplay and transition speeds based on user preference
const getAutoplayDelay = (defaultDelay) => prefersReducedMotion ? 0 : defaultDelay;
const getTransitionSpeed = (defaultSpeed) => prefersReducedMotion ? 0 : defaultSpeed;

// ================================
// 1. Portfolio Project Slider (Coverflow Effect)
// ================================
const portfolioSwiper = new Swiper('.portfolio-swiper', {
    // Coverflow 3D effect
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',

    // Coverflow settings
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
    },

    // Autoplay with pause on interaction
    autoplay: {
        delay: getAutoplayDelay(5000),
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
    },

    // Speed and smooth transitions
    speed: getTransitionSpeed(600),

    // Pagination
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullets: true,
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // Keyboard control
    keyboard: {
        enabled: true,
        onlyInViewport: true,
    },

    // Mouse wheel control
    mousewheel: {
        enabled: false,
        sensitivity: 1,
    },

    // Loop mode
    loop: true,

    // Accessibility
    a11y: {
        prevSlideMessage: 'Previous project',
        nextSlideMessage: 'Next project',
        firstSlideMessage: 'This is the first project',
        lastSlideMessage: 'This is the last project',
        paginationBulletMessage: 'Go to project {{index}}',
    },

    // Events
    on: {
        init: function() {
            console.log('Portfolio slider initialized');
        },
        slideChange: function() {
            // Optional: track analytics
            if (window.gtag) {
                gtag('event', 'slider_change', {
                    'event_category': 'portfolio',
                    'event_label': 'slide_' + (this.realIndex + 1)
                });
            }
        },
    },
});

// ================================
// 2. Technology Stack Carousel
// ================================
const techSwiper = new Swiper('.tech-swiper', {
    // Responsive slides per view
    slidesPerView: 2,
    spaceBetween: 20,

    // Infinite loop
    loop: true,

    // Autoplay
    autoplay: {
        delay: getAutoplayDelay(2500),
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
    },

    // Speed
    speed: getTransitionSpeed(500),

    // Free mode for natural scrolling
    freeMode: {
        enabled: true,
        momentum: true,
        momentumRatio: 0.5,
        momentumVelocityRatio: 0.5,
    },

    // Responsive breakpoints
    breakpoints: {
        // Mobile
        480: {
            slidesPerView: 2,
            spaceBetween: 15,
        },
        // Tablet
        640: {
            slidesPerView: 3,
            spaceBetween: 20,
        },
        // Desktop
        768: {
            slidesPerView: 4,
            spaceBetween: 20,
        },
        // Large desktop
        1024: {
            slidesPerView: 5,
            spaceBetween: 20,
        },
        1280: {
            slidesPerView: 6,
            spaceBetween: 20,
        },
    },

    // Accessibility
    a11y: {
        enabled: true,
    },

    on: {
        init: function() {
            console.log('Technology carousel initialized');
        },
    },
});

// ================================
// 3. Thumbnail Gallery (Synchronized Sliders)
// ================================

// Initialize thumbnail slider first
const galleryThumbs = new Swiper('.gallery-thumbs', {
    spaceBetween: 10,
    slidesPerView: 4,
    freeMode: true,
    watchSlidesProgress: true,

    // Responsive breakpoints
    breakpoints: {
        320: {
            slidesPerView: 3,
        },
        640: {
            slidesPerView: 4,
        },
        1024: {
            slidesPerView: 5,
        },
    },

    on: {
        init: function() {
            console.log('Gallery thumbnails initialized');
        },
    },
});

// Initialize main gallery slider
const galleryMain = new Swiper('.gallery-main', {
    spaceBetween: 10,

    // Speed
    speed: getTransitionSpeed(500),

    // Navigation
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // Sync with thumbnails
    thumbs: {
        swiper: galleryThumbs,
    },

    // Lazy loading
    lazy: {
        loadPrevNext: true,
        loadPrevNextAmount: 2,
    },

    // Keyboard
    keyboard: {
        enabled: true,
    },

    // Accessibility
    a11y: {
        enabled: true,
        prevSlideMessage: 'Previous image',
        nextSlideMessage: 'Next image',
    },

    on: {
        init: function() {
            console.log('Gallery main slider initialized');
        },
        lazyImageReady: function(swiper, slideEl, imageEl) {
            console.log('Image loaded:', imageEl);
        },
    },
});

// ================================
// Performance Optimizations
// ================================

// Pause autoplay when tab is not visible
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        // Pause all autoplay sliders
        if (portfolioSwiper.autoplay) portfolioSwiper.autoplay.stop();
        if (techSwiper.autoplay) techSwiper.autoplay.stop();
    } else {
        // Resume autoplay when tab becomes visible
        if (portfolioSwiper.autoplay) portfolioSwiper.autoplay.start();
        if (techSwiper.autoplay) techSwiper.autoplay.start();
    }
});

// ================================
// Intersection Observer for Lazy Initialization
// ================================

/**
 * Optional: Initialize sliders only when they enter viewport
 * Uncomment this section for even better performance
 */
/*
const sliderObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const slider = entry.target;

            // Initialize the slider when it enters viewport
            if (slider.classList.contains('portfolio-swiper') && !portfolioSwiper.initialized) {
                portfolioSwiper.init();
            }

            // Unobserve after initialization
            sliderObserver.unobserve(slider);
        }
    });
}, {
    rootMargin: '50px'
});

// Observe slider containers
document.querySelectorAll('.swiper').forEach(slider => {
    sliderObserver.observe(slider);
});
*/

// ================================
// Accessibility Enhancements
// ================================

// Add ARIA labels dynamically
document.querySelectorAll('.swiper').forEach(slider => {
    slider.setAttribute('role', 'region');
    slider.setAttribute('aria-label', 'Image carousel');
});

// Ensure all interactive elements have proper focus indicators
const focusableElements = document.querySelectorAll(
    '.swiper-button-prev, .swiper-button-next, .swiper-pagination-bullet'
);

focusableElements.forEach(element => {
    element.setAttribute('tabindex', '0');
});

// ================================
// Debug Mode (Development Only)
// ================================

// Enable detailed logging in development
const DEBUG = false; // Set to true for development

if (DEBUG) {
    console.log('Swiper Instances:', {
        portfolio: portfolioSwiper,
        tech: techSwiper,
        galleryMain: galleryMain,
        galleryThumbs: galleryThumbs,
    });

    // Log breakpoint changes
    const logBreakpoint = (swiper) => {
        console.log('Breakpoint changed:', {
            name: swiper.currentBreakpoint,
            params: swiper.params,
        });
    };

    portfolioSwiper.on('breakpoint', logBreakpoint);
    techSwiper.on('breakpoint', logBreakpoint);
}

// ================================
// Export for External Access (if using modules)
// ================================

// Uncomment if using ES6 modules
/*
export {
    portfolioSwiper,
    techSwiper,
    galleryMain,
    galleryThumbs,
};
*/

// Make available globally for debugging
if (typeof window !== 'undefined') {
    window.swiperInstances = {
        portfolio: portfolioSwiper,
        tech: techSwiper,
        galleryMain: galleryMain,
        galleryThumbs: galleryThumbs,
    };
}

console.log('✅ All sliders initialized successfully');
console.log('📱 Reduced motion:', prefersReducedMotion ? 'ENABLED' : 'DISABLED');
console.log('🎨 Swiper version:', Swiper.version || '11.x');
