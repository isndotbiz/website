// SpiritAtlas slider — app videos from B2 CDN.
// Videos are optimized for web: 480x832 portrait / 832x480 landscape, <500KB each.
const SA_VIDEO_CDN = 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/videos/app-ready';

window.spiritAtlasSliderData = [
    {
        id: 'home-dashboard',
        title: 'Cosmic Command Center',
        caption: 'The home screen — Daily Horoscope, Breathwork, Soul Connection, Numerology, and Astrology at a glance.',
        src: 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/app-screenshots/clean_home.webp',
        video: `${SA_VIDEO_CDN}/bg_splash_onboarding.mp4`,
        alt: 'Spirit Atlas home dashboard showing cosmic content categories',
        placeholder: 'linear-gradient(135deg, #0a0f1a 0%, #1a2a4a 50%, #0d1117 100%)',
        loading: 'eager'
    },
    {
        id: 'chakra-system',
        title: 'Chakra Energy System',
        caption: 'Seven primary chakras with guided meditations, energy visualizations, and detailed educational content.',
        src: 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/app-screenshots/nav_breathwork.webp',
        video: `${SA_VIDEO_CDN}/chakra_crown.mp4`,
        alt: 'Spirit Atlas chakra system with energy visualizations',
        placeholder: 'linear-gradient(135deg, #0d1117 0%, #1a3a6a 50%, #5b2091 100%)'
    },
    {
        id: 'dmt-entities',
        title: 'DMT Entity Archive',
        caption: 'Twelve interdimensional entities with animated portraits, sacred geometry, and deep spiritual lore.',
        src: 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/app-screenshots/nav_profiles.webp',
        video: `${SA_VIDEO_CDN}/dmt_entity_crystalline.mp4`,
        alt: 'Spirit Atlas DMT entity with crystalline energy visualization',
        placeholder: 'linear-gradient(135deg, #0a0f1a 0%, #1E9FF2 30%, #0d1117 100%)'
    },
    {
        id: 'zodiac-readings',
        title: 'Zodiac Guidance Engine',
        caption: 'AI-generated daily horoscope readings with personalized zodiac guidance across all twelve signs.',
        src: 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/app-screenshots/nav_horoscope.webp',
        video: `${SA_VIDEO_CDN}/zodiac_aquarius.mp4`,
        alt: 'Spirit Atlas zodiac reading with cosmic guidance',
        placeholder: 'linear-gradient(135deg, #0d1117 0%, #1E9FF2 50%, #0a0f1a 100%)'
    },
    {
        id: 'soul-connection',
        title: 'Soul Connection Analysis',
        caption: 'Compare two profiles across numerology, astrology, tantra, and energy systems — AI-generated compatibility.',
        src: 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/app-screenshots/nav_connection.webp',
        video: `${SA_VIDEO_CDN}/element_fire.mp4`,
        alt: 'Spirit Atlas compatibility analysis with profile selection',
        placeholder: 'linear-gradient(135deg, #0d1117 0%, #FF2D55 30%, #1a0a2e 100%)'
    },
    {
        id: 'archetype-cards',
        title: 'Archetype Card System',
        caption: 'Twelve unique archetype cards with animated reveals, personality insights, and spiritual guidance.',
        src: 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/app-screenshots/content_tantra.webp',
        video: `${SA_VIDEO_CDN}/archetype_card_7_harmonizer.mp4`,
        alt: 'Spirit Atlas archetype card with animated spiritual imagery',
        placeholder: 'linear-gradient(135deg, #1a0a2e 0%, #4a1a8a 50%, #0d1117 100%)'
    },
    {
        id: 'numerology-engine',
        title: 'Numerology Deep Dive',
        caption: 'Sacred number analysis with life path calculations, personal year cycles, and compatibility scoring.',
        src: 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/app-screenshots/nav_settings.webp',
        video: `${SA_VIDEO_CDN}/numerology_card_1.mp4`,
        alt: 'Spirit Atlas numerology with sacred geometry visualizations',
        placeholder: 'linear-gradient(135deg, #0a0f1a 0%, #1a2a4a 50%, #5b2091 100%)'
    },
    {
        id: 'element-system',
        title: 'Elemental Forces',
        caption: 'Earth, Fire, Water, and Ether — explore the fundamental elements with immersive animated content.',
        src: 'https://b2cdn.isn.biz/file/isnbiz-cdn/spiritatlas/app-screenshots/clean_home_scrolled.webp',
        video: `${SA_VIDEO_CDN}/element_earth.mp4`,
        alt: 'Spirit Atlas elemental forces with earth energy visualization',
        placeholder: 'linear-gradient(135deg, #0a0f1a 0%, #2a1f5e 50%, #5FDFDF 100%)'
    }
];
