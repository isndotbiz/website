<?php
/**
 * Template part for displaying portfolio preview (first 6 projects)
 *
 * @package ISN_BIZ_2026
 */

$projects = array(
    array(
        'number' => '01',
        'title' => __('AI Market Intelligence Engine', 'isnbiz-2026'),
        'description' => __('Proprietary AI pipeline that autonomously discovers and scores revenue opportunities across multiple data sources using local LLM inference and RAG-based semantic search — delivering institutional-grade market intelligence at zero marginal cost per query.', 'isnbiz-2026'),
        'tags' => array('Python', 'ChromaDB', 'Local LLM', 'RAG'),
        'image' => 'portfolio/opportunity_bot.webp'
    ),
    array(
        'number' => '02',
        'title' => __('Enterprise AI/ML Infrastructure Platform', 'isnbiz-2026'),
        'description' => __('Production-grade on-premise computing platform powering 50+ containerized services across AI inference, multi-database orchestration, and full observability — eliminating six-figure annual cloud dependency while maintaining enterprise SLA standards.', 'isnbiz-2026'),
        'tags' => array('Docker', 'TrueNAS Scale', 'ZFS', 'Ollama'),
        'image' => 'portfolio/infrastructure.webp'
    ),
    array(
        'number' => '03',
        'title' => __('Automated Compliance & Credit Intelligence', 'isnbiz-2026'),
        'description' => __('Zero-trust credential management system automating multi-bureau credit data aggregation through Playwright browser orchestration and 1Password vault integration — reducing compliance processing time by 95% with auditable, enterprise-grade security.', 'isnbiz-2026'),
        'tags' => array('Python', 'Playwright', '1Password CLI'),
        'image' => 'portfolio/credit_automation.webp'
    ),
    array(
        'number' => '04',
        'title' => __('Payment Fraud Intelligence Platform', 'isnbiz-2026'),
        'description' => __('Real-time BIN enrichment and fraud analytics engine serving the $32B payment fraud prevention market — combining automated feed ingestion, Neutrino API enrichment, and live risk scoring dashboards for e-commerce transaction security.', 'isnbiz-2026'),
        'tags' => array('Python', 'Flask', 'PostgreSQL', 'Chart.js'),
        'image' => 'portfolio/rag_bi.webp'
    ),
    array(
        'number' => '05',
        'title' => __('Privacy-First Consumer Mobile Platform', 'isnbiz-2026'),
        'description' => __('Enterprise-architected Android application showcasing Clean Architecture mastery with encrypted local storage, consent-gated AI routing, and 100+ custom density-optimized assets — demonstrating production mobile engineering at the highest standard.', 'isnbiz-2026'),
        'tags' => array('Kotlin', 'Jetpack Compose', 'Hilt', 'Android SDK 34'),
        'image' => 'portfolio/androidaps_health.webp'
    ),
    array(
        'number' => '06',
        'title' => __('AI Content Production Pipeline', 'isnbiz-2026'),
        'description' => __('End-to-end automated content factory converting raw sources into production-ready video assets using multi-provider AI orchestration (fal.ai, ElevenLabs, Runway) — targeting the $12B creator economy with 10x content velocity at fractional production costs.', 'isnbiz-2026'),
        'tags' => array('Node.js', 'fal.ai', 'ElevenLabs', 'AWS S3'),
        'image' => 'portfolio/infrastructure.webp'
    ),
);

foreach ($projects as $project) :
?>
<div class="portfolio-card">
    <div class="portfolio-image">
        <img src="<?php echo isnbiz_s3_url($project['image']); ?>" alt="<?php echo esc_attr($project['title']); ?>" loading="lazy">
    </div>
    <div class="portfolio-number"><?php echo esc_html($project['number']); ?></div>
    <h3><?php echo esc_html($project['title']); ?></h3>
    <p><?php echo esc_html($project['description']); ?></p>
    <div class="portfolio-tags">
        <?php foreach ($project['tags'] as $tag) : ?>
            <span class="tag"><?php echo esc_html($tag); ?></span>
        <?php endforeach; ?>
    </div>
</div>
<?php endforeach; ?>
