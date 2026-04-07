(function () {
    function normalizeAssetUrl(url) {
        if (!url) return '';
        return String(url).replace(/^\/(https?:\/\/)/i, '$1');
    }

    function humanizeBase(base) {
        return base
            .replace(/^(16x9|9x16|1x1)_/i, '')
            .replace(/\b\d+\b/g, ' ')
            .replace(/_/g, ' ')
            .replace(/\s+/g, ' ')
            .trim()
            .replace(/\b[a-z]/g, function (m) { return m.toUpperCase(); })
            .slice(0, 64);
    }

    function formatCategory(category) {
        return category.replace(/_/g, ' ').replace(/\b\w/g, function (m) { return m.toUpperCase(); });
    }

    function createImageCard(item) {
        var card = document.createElement('article');
        card.className = 'spirit-media-card spirit-media-' + item.orientation;

        var image = document.createElement('img');
        image.src = normalizeAssetUrl(item.src);
        image.alt = humanizeBase(item.base) + ' visual';
        image.loading = 'lazy';
        image.decoding = 'async';
        image.onerror = function () { card.style.display = 'none'; };

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
        video.src = normalizeAssetUrl(item.src);
        video.muted = true;
        video.loop = true;
        video.playsInline = true;
        video.controls = true;
        video.preload = 'none';
        video.onerror = function () { card.style.display = 'none'; };

        card.addEventListener('mouseenter', function () { video.play().catch(function () {}); });
        card.addEventListener('mouseleave', function () { video.pause(); });

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

    // Create a section header label inside a grid container
    function makeOrientationLabel(text) {
        var label = document.createElement('p');
        label.className = 'spirit-orientation-label';
        label.textContent = text;
        return label;
    }

    // Render items grouped strictly by orientation, each group in its own grid
    function renderGroupedItems(container, items, createCardFn, loadMoreBtn, state) {
        if (state.reset) {
            container.innerHTML = '';
            state.index = 0;
            state.reset = false;
        }

        var remaining = items.slice(state.index, state.index + state.pageSize);
        if (!remaining.length) {
            loadMoreBtn.disabled = true;
            loadMoreBtn.textContent = 'All Loaded';
            return;
        }

        // Group remaining by orientation
        var groups = { portrait: [], landscape: [], square: [] };
        remaining.forEach(function (item) {
            var o = item.orientation;
            if (!groups[o]) groups[o] = [];
            groups[o].push(item);
        });

        var order = ['portrait', 'landscape', 'square'];
        order.forEach(function (orient) {
            var group = groups[orient];
            if (!group || !group.length) return;

            var label = makeOrientationLabel(
                orient === 'portrait' ? 'Portrait (9:16)' :
                orient === 'landscape' ? 'Landscape (16:9)' : 'Square (1:1)'
            );
            container.appendChild(label);

            var grid = document.createElement('div');
            grid.className = 'spirit-subgrid spirit-subgrid-' + orient;
            group.forEach(function (item) { grid.appendChild(createCardFn(item)); });
            container.appendChild(grid);
        });

        state.index += remaining.length;
        loadMoreBtn.disabled = state.index >= items.length;
        loadMoreBtn.textContent = state.index >= items.length ? 'All Loaded' : 'Load More';
    }

    function setupMediaWall(media) {
        var imageGrid = document.getElementById('spirit-image-grid');
        var videoGrid = document.getElementById('spirit-video-grid');
        var signatureGrid = document.getElementById('spirit-signature-grid');
        var imageLoadMore = document.getElementById('spirit-images-load-more');
        var videoLoadMore = document.getElementById('spirit-videos-load-more');
        var orientationButtons = Array.from(document.querySelectorAll('[data-spirit-orientation]'));
        var categorySelect = document.getElementById('spirit-image-category');

        if (!imageGrid || !videoGrid || !signatureGrid || !imageLoadMore || !videoLoadMore || !categorySelect) return;

        // Update stat counters
        document.querySelectorAll('[data-spirit-image-count]').forEach(function (el) { el.textContent = String(media.imageCount); });
        document.querySelectorAll('[data-spirit-video-count]').forEach(function (el) { el.textContent = String(media.videoCount); });
        document.querySelectorAll('[data-spirit-landscape-count]').forEach(function (el) { el.textContent = String(media.imageOrientationCounts.landscape || 0); });
        document.querySelectorAll('[data-spirit-portrait-count]').forEach(function (el) { el.textContent = String(media.imageOrientationCounts.portrait || 0); });
        document.querySelectorAll('[data-spirit-square-count]').forEach(function (el) { el.textContent = String(media.imageOrientationCounts.square || 0); });

        buildCategoryOptions(categorySelect, media.images);

        // Signature grid — portrait only, 4 cards
        var signaturePool = media.images.filter(function (item) {
            return item.orientation === 'portrait' && (
                item.category === 'dmt_entities_24' ||
                item.category === 'archetypes_24' ||
                item.category === 'zodiac_24'
            );
        }).slice(0, 4);
        signaturePool.forEach(function (item) { signatureGrid.appendChild(createImageCard(item)); });

        var imageFilter = { orientation: 'all', category: 'all' };

        function getFilteredImages() {
            return media.images.filter(function (item) {
                var oOk = imageFilter.orientation === 'all' || item.orientation === imageFilter.orientation;
                var cOk = imageFilter.category === 'all' || item.category === imageFilter.category;
                return oOk && cOk;
            });
        }

        var imageState = { index: 0, pageSize: 96, reset: true };
        var videoState = { index: 0, pageSize: 24, reset: true };

        function renderImages(reset) {
            imageState.reset = reset;
            if (reset) imageGrid.innerHTML = '';
            renderGroupedItems(imageGrid, getFilteredImages(), createImageCard, imageLoadMore, imageState);
        }

        function renderVideos(reset) {
            videoState.reset = reset;
            if (reset) videoGrid.innerHTML = '';
            renderGroupedItems(videoGrid, media.videos, createVideoCard, videoLoadMore, videoState);
        }

        orientationButtons.forEach(function (button) {
            button.addEventListener('click', function () {
                orientationButtons.forEach(function (node) { node.classList.remove('is-active'); });
                button.classList.add('is-active');
                imageFilter.orientation = button.getAttribute('data-spirit-orientation') || 'all';
                renderImages(true);
            });
        });

        categorySelect.addEventListener('change', function () {
            imageFilter.category = categorySelect.value;
            renderImages(true);
        });

        imageLoadMore.addEventListener('click', function () { renderImages(false); });
        videoLoadMore.addEventListener('click', function () { renderVideos(false); });

        renderImages(true);
        renderVideos(true);

        // Hero image
        var heroImage = document.getElementById('spirit-hero-image');
        if (heroImage && media.images.length) {
            var heroCandidate = media.images.find(function (item) {
                return item.rel === 'backgrounds_24/9x16_002_bg_home.webp';
            }) || media.images[0];
            heroImage.src = normalizeAssetUrl(heroCandidate.src);
            heroImage.alt = 'Spirit Atlas final app visual';
        }

        // Side flow images
        var sideImages = [
            { id: 'spirit-flow-image-1', rel: 'archetypes_24/9x16_001_onboarding_11_visionary.webp' },
            { id: 'spirit-flow-image-2', rel: 'dmt_entities_24/9x16_010_dmt_entity_oracle.webp' },
            { id: 'spirit-flow-image-3', rel: 'zodiac_24/01.webp' }
        ];
        sideImages.forEach(function (target) {
            var node = document.getElementById(target.id);
            if (!node) return;
            var match = media.images.find(function (item) { return item.rel === target.rel; });
            if (match) {
                node.src = normalizeAssetUrl(match.src);
                node.alt = humanizeBase(match.base) + ' final app visual';
            }
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        if (!window.SPIRIT_ATLAS_FINAL_MEDIA) return;
        setupMediaWall(window.SPIRIT_ATLAS_FINAL_MEDIA);
    });
})();
