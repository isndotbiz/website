(function () {
    const fs = require('fs');
    const path = require('path');

    const imageRoot = '/Users/jonathanmallinger/Workspace/Spirit-Atlas/images';
    const videoRoot = '/Users/jonathanmallinger/Workspace/Spirit-Atlas/videos';
    const imageCdnPrefix = 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/images';
    const videoCdnPrefix = 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/videos';

    const imageExt = new Set(['.png', '.jpg', '.jpeg', '.webp']);
    const videoExt = new Set(['.mp4', '.mov', '.webm', '.m4v']);

    const categoryOrientationFallback = {
        zodiac_24: 'portrait',
        zodiac_cards_24: 'landscape',
        eastern_zodiac_12: 'landscape'
    };

    function walk(dir, exts) {
        const out = [];
        const entries = fs.readdirSync(dir, { withFileTypes: true });
        for (const entry of entries) {
            if (entry.name.startsWith('.')) {
                continue;
            }
            const abs = path.join(dir, entry.name);
            if (entry.isDirectory()) {
                out.push(...walk(abs, exts));
                continue;
            }
            const ext = path.extname(entry.name).toLowerCase();
            if (exts.has(ext)) {
                out.push(abs);
            }
        }
        return out;
    }

    function orientationFor(relPath) {
        const file = relPath.toLowerCase();
        const category = relPath.split('/')[0];
        if (file.includes('16x9_')) {
            return 'landscape';
        }
        if (file.includes('9x16_')) {
            return 'portrait';
        }
        if (file.includes('1x1_')) {
            return 'square';
        }
        return categoryOrientationFallback[category] || 'portrait';
    }

    function buildEntries(root, publicPrefix, exts, mapRelPath) {
        const cleanPrefix = String(publicPrefix).replace(/\/+$/, '');
        return walk(root, exts)
            .map((abs) => {
                const rel = path.relative(root, abs).split(path.sep).join('/');
                const mappedRel = mapRelPath ? mapRelPath(rel) : rel;
                const category = rel.split('/')[0] || 'misc';
                const orientation = orientationFor(rel);
                const filename = path.basename(mappedRel);
                const base = filename.replace(path.extname(filename), '');
                return {
                    src: `${cleanPrefix}/${mappedRel}`,
                    rel: mappedRel,
                    category,
                    orientation,
                    filename,
                    base
                };
            })
            .sort((a, b) => a.rel.localeCompare(b.rel));
    }

    const images = buildEntries(
        imageRoot,
        imageCdnPrefix,
        imageExt,
        (rel) => rel.replace(/\.(png|jpg|jpeg)$/i, '.webp')
    );
    const videos = buildEntries(videoRoot, videoCdnPrefix, videoExt);

    const imageOrientationCounts = images.reduce((acc, item) => {
        acc[item.orientation] = (acc[item.orientation] || 0) + 1;
        return acc;
    }, {});

    const videoOrientationCounts = videos.reduce((acc, item) => {
        acc[item.orientation] = (acc[item.orientation] || 0) + 1;
        return acc;
    }, {});

    const media = {
        generatedAt: new Date().toISOString(),
        source: {
            imagesLocalRoot: imageRoot,
            videosLocalRoot: videoRoot,
            imagesCdnRoot: imageCdnPrefix,
            videosCdnRoot: videoCdnPrefix
        },
        imageCount: images.length,
        videoCount: videos.length,
        imageOrientationCounts,
        videoOrientationCounts,
        images,
        videos
    };

    const target = '/Users/jonathanmallinger/Workspace/isnbiz-website/js/spiritatlas-final-media.generated.js';
    const output = `window.SPIRIT_ATLAS_FINAL_MEDIA = ${JSON.stringify(media, null, 2)};\n`;
    fs.writeFileSync(target, output, 'utf8');
})();
