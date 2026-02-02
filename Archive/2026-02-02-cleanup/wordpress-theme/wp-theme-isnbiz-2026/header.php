<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    <link rel="icon" type="image/webp" href="<?php echo isnbiz_s3_url('logos/favicon.webp'); ?>">
    <link rel="apple-touch-icon" href="<?php echo isnbiz_s3_url('logos/apple_touch_icon.webp'); ?>">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- WCAG FIX: Skip navigation link for keyboard users -->
<a href="#about" class="skip-link"><?php esc_html_e('Skip to main content', 'isnbiz-2026'); ?></a>

<!-- Navigation -->
<nav class="nav">
    <div class="container nav-container">
        <div class="logo">
            <?php if (has_custom_logo()) : ?>
                <?php the_custom_logo(); ?>
            <?php else : ?>
                <a href="<?php echo esc_url(home_url('/')); ?>">
                    <img src="<?php echo isnbiz_s3_url('logos/navbar_logo.webp'); ?>" alt="<?php bloginfo('name'); ?> Logo" class="logo-img">
                </a>
            <?php endif; ?>
        </div>
        <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="primary-navigation" type="button">
            <span></span>
            <span></span>
            <span></span>
        </button>
        <?php
        wp_nav_menu(array(
            'theme_location' => 'primary',
            'menu_id'        => 'primary-navigation',
            'menu_class'     => 'nav-menu',
            'container'      => false,
            'walker'         => new ISNBIZ_Walker_Nav_Menu(),
            'fallback_cb'    => function() {
                echo '<ul class="nav-menu" id="primary-navigation">';
                echo '<li role="none"><a href="' . esc_url(home_url('/about')) . '" role="menuitem">About</a></li>';
                echo '<li role="none"><a href="' . esc_url(home_url('/services')) . '" role="menuitem">Services</a></li>';
                echo '<li role="none"><a href="' . esc_url(home_url('/portfolio')) . '" role="menuitem">Portfolio</a></li>';
                echo '<li role="none"><a href="' . esc_url(home_url('/investors')) . '" role="menuitem">Investors</a></li>';
                echo '<li role="none"><a href="' . esc_url(home_url('/contact')) . '" class="nav-cta" role="menuitem">Contact</a></li>';
                echo '</ul>';
            }
        ));
        ?>
    </div>
</nav>
