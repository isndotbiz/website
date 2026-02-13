(() => {
    const updateReleaseCountdown = () => {
        const badge = document.querySelector('[data-release-countdown]');
        if (!badge) return;
        const releaseDate = new Date('2026-04-01T00:00:00');
        const now = new Date();
        const msPerDay = 24 * 60 * 60 * 1000;
        const days = Math.max(0, Math.ceil((releaseDate.getTime() - now.getTime()) / msPerDay));
        badge.textContent = days > 0 ? `Release in ${days} days • Apr 1, 2026` : 'Released • Apr 1, 2026';
    };
    const escapeHtml = (value = '') => String(value)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');

    const buildSlideMarkup = (slidesConfig) => {
        return slidesConfig.map((slide, index) => {
            const companionA = slidesConfig[(index + 1) % slidesConfig.length];
            const companionB = slidesConfig[(index + 2) % slidesConfig.length];
            const companionC = slidesConfig[(index + 3) % slidesConfig.length];
            const hasImage = typeof slide.src === 'string' && slide.src.trim().length > 0;
            const loading = slide.loading || (index === 0 ? 'eager' : 'lazy');
            const safeTitle = escapeHtml(slide.title || `SpiritAtlas Preview ${index + 1}`);
            const safeCaption = escapeHtml(slide.caption || 'Replace with your latest app screenshot.');
            const safeAlt = escapeHtml(slide.alt || slide.title || `SpiritAtlas slide ${index + 1}`);
            const safePlaceholder = escapeHtml(slide.placeholder || 'linear-gradient(135deg, #122d52 0%, #305dab 55%, #7229ba 100%)');
            const safeSrc = hasImage ? escapeHtml(slide.src) : '';
            const safeWideSrc = typeof slide.wideSrc === 'string' && slide.wideSrc.trim().length > 0 ? escapeHtml(slide.wideSrc) : '';
            const companionASrc = companionA?.src ? escapeHtml(companionA.src) : '';
            const companionAAlt = escapeHtml(companionA?.alt || companionA?.title || 'SpiritAtlas companion screenshot');
            const companionATitle = escapeHtml(companionA?.title || 'Next spiritual screen');
            const companionBSrc = companionB?.src ? escapeHtml(companionB.src) : '';
            const companionBAlt = escapeHtml(companionB?.alt || companionB?.title || 'SpiritAtlas companion screenshot');
            const companionBTitle = escapeHtml(companionB?.title || 'Next spiritual screen');
            const companionCSrc = companionC?.src ? escapeHtml(companionC.src) : '';
            const companionCAlt = escapeHtml(companionC?.alt || companionC?.title || 'SpiritAtlas companion screenshot');
            const companionCTitle = escapeHtml(companionC?.title || 'Next spiritual screen');

            return `
                <div class="slide${index === 0 ? ' active' : ''}" role="option" id="slide-${escapeHtml(slide.id)}" aria-selected="${index === 0}" aria-posinset="${index + 1}" aria-setsize="${slidesConfig.length}" tabindex="${index === 0 ? '0' : '-1'}" data-slide-id="${escapeHtml(slide.id)}">
                    <figure class="slide-figure${safeWideSrc ? ' has-wide' : ''}">
                        <div class="slide-placeholder" style="background:${safePlaceholder};" aria-hidden="true"></div>
                        ${safeWideSrc
                            ? `<img class="slide-wide-img" src="${safeWideSrc}" alt="${safeAlt}" loading="${loading}" decoding="async" width="1920" height="1080">`
                            : `<div class="slide-layout">
                                <div class="slide-media">
                                    <div class="slide-phone-strip">
                                        <figure class="slide-phone-card is-primary">
                                            ${hasImage
                                                ? `<img src="${safeSrc}" alt="${safeAlt}" loading="${loading}" decoding="async" width="1080" height="2400">`
                                                : `<div class="slide-image-fallback" role="img" aria-label="${safeAlt}">Screenshot placeholder ready for next upload</div>`
                                            }
                                            <figcaption>${safeTitle}</figcaption>
                                        </figure>
                                        <figure class="slide-phone-card">
                                            ${companionASrc ? `<img src="${companionASrc}" alt="${companionAAlt}" loading="lazy" decoding="async" width="540" height="1200">` : ''}
                                            <figcaption>${companionATitle}</figcaption>
                                        </figure>
                                        <figure class="slide-phone-card">
                                            ${companionBSrc ? `<img src="${companionBSrc}" alt="${companionBAlt}" loading="lazy" decoding="async" width="540" height="1200">` : ''}
                                            <figcaption>${companionBTitle}</figcaption>
                                        </figure>
                                    </div>
                                </div>
                                <aside class="slide-aside">
                                    <div class="slide-aside-card">
                                        <span class="slide-kicker">Ancient Wisdom &bull; AI Clarity</span>
                                        <h4>${safeTitle}</h4>
                                        <p>${safeCaption}</p>
                                    </div>
                                </aside>
                            </div>`
                        }
                        <figcaption class="slide-caption">
                            <strong>${safeTitle}</strong>
                            <span>${safeCaption}</span>
                        </figcaption>
                    </figure>
                </div>
            `;
        }).join('');
    };

    const buildDotsMarkup = (slidesConfig) => {
        return slidesConfig.map((slide, index) => {
            const label = escapeHtml(slide.title || `SpiritAtlas Preview ${index + 1}`);
            return `<button class="dot${index === 0 ? ' active' : ''}" type="button" aria-label="Go to slide ${index + 1}: ${label}" aria-current="${index === 0}" data-slide-to="${index}"></button>`;
        }).join('');
    };

    const initHeroSlider = (slider, slidesConfig) => {
        if (!slider) return;
        const track = slider.querySelector('[data-slider-track]');
        const dotsContainer = slider.querySelector('[data-slider-dots]');
        const prevBtn = slider.querySelector('[data-slider-prev]');
        const nextBtn = slider.querySelector('[data-slider-next]');
        const toggleBtn = slider.querySelector('[data-slider-toggle]');
        const announcer = slider.querySelector('[data-slider-announcer]');
        const progressBar = slider.querySelector('[data-slider-progress]');

        if (!track || !dotsContainer) return;
        if (!slidesConfig.length) return;

        track.innerHTML = buildSlideMarkup(slidesConfig);
        dotsContainer.innerHTML = buildDotsMarkup(slidesConfig);

        const slides = Array.from(track.querySelectorAll('.slide'));
        const dots = Array.from(dotsContainer.querySelectorAll('.dot'));
        const totalSlides = slides.length;
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        const autoPlayDelayMs = 7000;

        let currentIndex = 0;
        let autoPlayTimer = null;
        let isPaused = prefersReducedMotion;
        let userInteracted = false;
        let progressRaf = null;
        let progressStart = performance.now();
        let touchStartX = null;

        const updatePauseButton = () => {
            if (!toggleBtn) return;
            toggleBtn.textContent = isPaused ? 'Play' : 'Pause';
            toggleBtn.setAttribute('aria-pressed', String(isPaused));
            toggleBtn.setAttribute('aria-label', isPaused ? 'Resume slide autoplay' : 'Pause slide autoplay');
        };

        const clearAutoPlay = () => {
            if (autoPlayTimer) {
                clearInterval(autoPlayTimer);
                autoPlayTimer = null;
            }
            if (progressRaf) {
                cancelAnimationFrame(progressRaf);
                progressRaf = null;
            }
        };

        const setProgress = (value) => {
            if (!progressBar) return;
            const clamped = Math.max(0, Math.min(100, value));
            progressBar.style.width = `${clamped}%`;
        };

        const runProgress = () => {
            if (isPaused || userInteracted || totalSlides < 2) return;
            const elapsed = performance.now() - progressStart;
            const pct = (elapsed / autoPlayDelayMs) * 100;
            setProgress(pct);
            progressRaf = requestAnimationFrame(runProgress);
        };

        const restartAutoPlay = () => {
            clearAutoPlay();
            if (isPaused || userInteracted || totalSlides < 2) return;
            progressStart = performance.now();
            setProgress(0);
            autoPlayTimer = setInterval(() => {
                updateSlider(currentIndex + 1);
                progressStart = performance.now();
                setProgress(0);
            }, autoPlayDelayMs);
            progressRaf = requestAnimationFrame(runProgress);
        };

        const updateSlider = (index) => {
            const normalizedIndex = ((index % totalSlides) + totalSlides) % totalSlides;

            slides.forEach((slide, slideIndex) => {
                const isActive = slideIndex === normalizedIndex;
                slide.classList.toggle('active', isActive);
                slide.setAttribute('aria-selected', String(isActive));
                slide.setAttribute('tabindex', isActive ? '0' : '-1');
            });

            dots.forEach((dot, dotIndex) => {
                const isActive = dotIndex === normalizedIndex;
                dot.classList.toggle('active', isActive);
                dot.setAttribute('aria-current', String(isActive));
            });

            track.style.transform = `translateX(-${normalizedIndex * 100}%)`;
            track.setAttribute('aria-activedescendant', `slide-${slidesConfig[normalizedIndex].id}`);
            if (announcer) {
                const activeSlide = slidesConfig[normalizedIndex];
                announcer.textContent = `Slide ${normalizedIndex + 1} of ${totalSlides}: ${activeSlide.title}. ${activeSlide.caption}`;
            }
            currentIndex = normalizedIndex;
        };

        const pauseTemporarily = () => {
            if (!isPaused) clearAutoPlay();
        };

        const resumeTemporarily = () => {
            if (!isPaused) restartAutoPlay();
        };

        prevBtn?.addEventListener('click', () => {
            userInteracted = true;
            updateSlider(currentIndex - 1);
            restartAutoPlay();
        });

        nextBtn?.addEventListener('click', () => {
            userInteracted = true;
            updateSlider(currentIndex + 1);
            restartAutoPlay();
        });

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                userInteracted = true;
                updateSlider(index);
                restartAutoPlay();
            });
        });

        toggleBtn?.addEventListener('click', () => {
            isPaused = !isPaused;
            userInteracted = isPaused;
            updatePauseButton();
            setProgress(0);
            restartAutoPlay();
        });

        slider.addEventListener('touchstart', (event) => {
            touchStartX = event.touches?.[0]?.clientX ?? null;
        }, { passive: true });

        slider.addEventListener('touchend', (event) => {
            if (touchStartX == null) return;
            const touchEndX = event.changedTouches?.[0]?.clientX ?? touchStartX;
            const deltaX = touchEndX - touchStartX;
            touchStartX = null;
            if (Math.abs(deltaX) < 40) return;
            userInteracted = true;
            if (deltaX > 0) {
                updateSlider(currentIndex - 1);
            } else {
                updateSlider(currentIndex + 1);
            }
            restartAutoPlay();
        }, { passive: true });

        slider.addEventListener('mouseenter', pauseTemporarily);
        slider.addEventListener('mouseleave', resumeTemporarily);
        slider.addEventListener('focusin', pauseTemporarily);
        slider.addEventListener('focusout', (event) => {
            if (!slider.contains(event.relatedTarget) && !userInteracted) {
                resumeTemporarily();
            }
        });

        slider.addEventListener('keydown', (event) => {
            if (event.key === 'ArrowLeft') {
                event.preventDefault();
                userInteracted = true;
                updateSlider(currentIndex - 1);
                restartAutoPlay();
            } else if (event.key === 'ArrowRight') {
                event.preventDefault();
                userInteracted = true;
                updateSlider(currentIndex + 1);
                restartAutoPlay();
            } else if (event.key === 'Home') {
                event.preventDefault();
                userInteracted = true;
                updateSlider(0);
                restartAutoPlay();
            } else if (event.key === 'End') {
                event.preventDefault();
                userInteracted = true;
                updateSlider(totalSlides - 1);
                restartAutoPlay();
            }
        });

        slider.addEventListener('mousemove', (event) => {
            if (prefersReducedMotion) return;
            const rect = slider.getBoundingClientRect();
            const x = ((event.clientX - rect.left) / rect.width) - 0.5;
            const y = ((event.clientY - rect.top) / rect.height) - 0.5;
            slider.style.setProperty('--sa-parallax-x', `${(x * 8).toFixed(2)}px`);
            slider.style.setProperty('--sa-parallax-y', `${(y * 6).toFixed(2)}px`);
        });

        slider.addEventListener('mouseleave', () => {
            slider.style.setProperty('--sa-parallax-x', '0px');
            slider.style.setProperty('--sa-parallax-y', '0px');
        });

        updatePauseButton();
        updateSlider(0);
        setProgress(0);
        restartAutoPlay();
    };

    const initAllHeroSliders = () => {
        updateReleaseCountdown();
        const slidesConfig = (window.spiritAtlasSliderData || []).filter(slide => slide && slide.id);
        if (!slidesConfig.length) return;
        document.querySelectorAll('[data-hero-slider]').forEach(slider => {
            initHeroSlider(slider, slidesConfig);
        });
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAllHeroSliders);
    } else {
        initAllHeroSliders();
    }
})();
