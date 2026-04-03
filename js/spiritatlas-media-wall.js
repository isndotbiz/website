(function () {
    function humanizeBase(base) {
        return base
            .replace(/^(16x9|9x16|1x1)_/i, '')
            .replace(/\b\d+\b/g, ' ')
            .replace(/_/g, ' ')
            .replace(/\s+/g, ' ')
            .trim()
            .replace(/\b[a-z]/g, function (m) {
                return m.toUpperCase();
            })
            .slice(0, 64);
    }

    function formatCategory(category) {
        return category
            .replace(/_/g, ' ')
            .replace(/\b\w/g, function (m) {
                return m.toUpperCase();
            });
    }

    function createImageCard(item) {
        var card = document.createElement('article');
        card.className = 'spirit-media-card spirit-media-' + item.orientation;

        var image = document.createElement('img');
        image.src = item.src;
        image.alt = humanizeBase(item.base) + ' visual';
        image.loading = 'lazy';
        image.decoding = 'async';
        image.onerror = function () {
            card.style.display = 'none';
        };

        var meta = document.createElement('div');
        meta.className = 'spirit-media-meta';
        meta.innerHTML =
            '<span>' + formatCategory(item.category) + '</span>' +
            '<strong>' + humanizeBase(item.base) + '</strong>';

        card.appendChild(image);
        card.appendChild(meta);
        return card;
    }

    function createVideoCard(item) {
        var card = document.createElement('article');
        card.className = 'spirit-video-card spirit-media-' + item.orientation;

        var video = document.createElement('video');
        video.src = item.src;
        video.muted = true;
        video.loop = true;
        video.playsInline = true;
        video.controls = true;
        video.preload = 'none';

        video.onerror = function () {
            card.style.display = 'none';
        };

        card.addEventListener('mouseenter', function () {
            video.play().catch(function () {});
        });
        card.addEventListener('mouseleave', function () {
            video.pause();
        });

        if ('IntersectionObserver' in window) {
            var observer = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        video.preload = 'metadata';
                        observer.unobserve(video);
                    }
                });
            }, { rootMargin: '200px' });
            observer.observe(video);
        }

        var meta = document.createElement('div');
        meta.className = 'spirit-media-meta';
        meta.innerHTML =
            '<span>' + formatCategory(item.category) + '</span>' +
            '<strong>' + humanizeBase(item.base) + '</strong>';

        card.appendChild(video);
        card.appendChild(meta);
        return card;
    }

    function buildCategoryOptions(select, items) {
        var categories = Array.from(new Set(items.map(function (item) { return item.category; }))).sort();
        var first = document.createElement('option');
        first.value = 'all';
        first.textContent = 'All Categories';
        select.appendChild(first);

        categories.forEach(function (category) {
            var option = document.createElement('option');
            option.value = category;
            option.textContent = formatCategory(category);
            select.appendChild(option);
        });
    }

    function setupMediaWall(media) {
        var imageGrid = document.getElementById('spirit-image-grid');
        var videoGrid = document.getElementById('spirit-video-grid');
        var signatureGrid = document.getElementById('spirit-signature-grid');
        var imageLoadMore = document.getElementById('spirit-images-load-more');
        var videoLoadMore = document.getElementById('spirit-videos-load-more');
        var orientationButtons = Array.from(document.querySelectorAll('[data-spirit-orientation]'));
        var categorySelect = document.getElementById('spirit-image-category');

        if (!imageGrid || !videoGrid || !signatureGrid || !imageLoadMore || !videoLoadMore || !categorySelect) {
            return;
        }

        var imageStats = document.querySelectorAll('[data-spirit-image-count]');
        var videoStats = document.querySelectorAll('[data-spirit-video-count]');
        var landscapeStats = document.querySelectorAll('[data-spirit-landscape-count]');
        var portraitStats = document.querySelectorAll('[data-spirit-portrait-count]');
        var squareStats = document.querySelectorAll('[data-spirit-square-count]');

        imageStats.forEach(function (el) { el.textContent = String(media.imageCount); });
        videoStats.forEach(function (el) { el.textContent = String(media.videoCount); });
        landscapeStats.forEach(function (el) { el.textContent = String(media.imageOrientationCounts.landscape || 0); });
        portraitStats.forEach(function (el) { el.textContent = String(media.imageOrientationCounts.portrait || 0); });
        squareStats.forEach(function (el) { el.textContent = String(media.imageOrientationCounts.square || 0); });

        buildCategoryOptions(categorySelect, media.images);

        var signaturePool = media.images.filter(function (item) {
            return item.orientation === 'portrait' && (
                item.category === 'dmt_entities_24' ||
                item.category === 'archetypes_24' ||
                item.category === 'zodiac_24'
            );
        }).slice(0, 16);

        signaturePool.forEach(function (item) {
            signatureGrid.appendChild(createImageCard(item));
        });

        var imageState = {
            orientation: 'all',
            category: 'all',
            index: 0,
            pageSize: 96
        };

        var videoState = {
            index: 0,
            pageSize: 24
        };

        function getFilteredImages() {
            return media.images.filter(function (item) {
                var orientationOk = imageState.orientation === 'all' || item.orientation === imageState.orientation;
                var categoryOk = imageState.category === 'all' || item.category === imageState.category;
                return orientationOk && categoryOk;
            });
        }

        function renderNextImages(reset) {
            if (reset) {
                imageState.index = 0;
                imageGrid.innerHTML = '';
            }

            var filtered = getFilteredImages();
            var next = filtered.slice(imageState.index, imageState.index + imageState.pageSize);
            next.forEach(function (item) {
                imageGrid.appendChild(createImageCard(item));
            });

            imageState.index += next.length;
            imageLoadMore.disabled = imageState.index >= filtered.length;
            imageLoadMore.textContent = imageState.index >= filtered.length
                ? 'All Matching Images Loaded'
                : 'Load More Final Images';
        }

        function renderNextVideos(reset) {
            if (reset) {
                videoState.index = 0;
                videoGrid.innerHTML = '';
            }

            var next = media.videos.slice(videoState.index, videoState.index + videoState.pageSize);
            next.forEach(function (item) {
                videoGrid.appendChild(createVideoCard(item));
            });

            videoState.index += next.length;
            videoLoadMore.disabled = videoState.index >= media.videos.length;
            videoLoadMore.textContent = videoState.index >= media.videos.length
                ? 'All Final Videos Loaded'
                : 'Load More Final Videos';
        }

        orientationButtons.forEach(function (button) {
            button.addEventListener('click', function () {
                orientationButtons.forEach(function (node) { node.classList.remove('is-active'); });
                button.classList.add('is-active');
                imageState.orientation = button.getAttribute('data-spirit-orientation') || 'all';
                renderNextImages(true);
            });
        });

        categorySelect.addEventListener('change', function () {
            imageState.category = categorySelect.value;
            renderNextImages(true);
        });

        imageLoadMore.addEventListener('click', function () {
            renderNextImages(false);
        });

        videoLoadMore.addEventListener('click', function () {
            renderNextVideos(false);
        });

        renderNextImages(true);
        renderNextVideos(true);

        var heroImage = document.getElementById('spirit-hero-image');
        if (heroImage && media.images.length) {
            var heroCandidate = media.images.find(function (item) {
                return item.rel === 'backgrounds_24/9x16_002_bg_home.png';
            }) || media.images[0];
            heroImage.src = heroCandidate.src;
            heroImage.alt = 'Spirit Atlas final app visual';
        }

        var sideImages = [
            { id: 'spirit-flow-image-1', rel: 'archetypes_24/9x16_001_onboarding_11_visionary.png' },
            { id: 'spirit-flow-image-2', rel: 'dmt_entities_24/9x16_010_dmt_entity_oracle.png' },
            { id: 'spirit-flow-image-3', rel: 'zodiac_24/01.png' }
        ];

        sideImages.forEach(function (target) {
            var node = document.getElementById(target.id);
            if (!node) {
                return;
            }
            var match = media.images.find(function (item) {
                return item.rel === target.rel;
            });
            if (match) {
                node.src = match.src;
                node.alt = humanizeBase(match.base) + ' final app visual';
            }
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        if (!window.SPIRIT_ATLAS_FINAL_MEDIA) {
            return;
        }
        setupMediaWall(window.SPIRIT_ATLAS_FINAL_MEDIA);
    });
})();
