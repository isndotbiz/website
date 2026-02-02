<?php
/**
 * The template for displaying all pages
 *
 * @package ISN_BIZ_2026
 */

get_header();
?>

<section class="hero portfolio-hero">
    <div class="hero-background"></div>
    <div class="container hero-container">
        <div class="hero-content">
            <div class="hero-logo">
                <img src="<?php echo isnbiz_s3_url('logos/hero_logo.webp'); ?>" alt="<?php bloginfo('name'); ?> - Innovation Solutions Systems" class="hero-logo-img">
            </div>
            <h1 class="hero-title"><?php the_title(); ?></h1>
            <?php if (has_excerpt()) : ?>
                <p class="hero-subtitle"><?php the_excerpt(); ?></p>
            <?php endif; ?>
        </div>
    </div>
</section>

<section class="section about">
    <div class="container">
        <?php
        while (have_posts()) : the_post();
            the_content();
        endwhile;
        ?>
    </div>
</section>

<?php
get_footer();
