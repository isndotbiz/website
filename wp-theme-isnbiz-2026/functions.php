<?php
/**
 * ISN.BIZ 2026 Theme Functions
 *
 * @package ISN_BIZ_2026
 * @since 1.0.0
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Theme Setup
 */
function isnbiz_theme_setup() {
    // Add default posts and comments RSS feed links to head
    add_theme_support('automatic-feed-links');

    // Let WordPress manage the document title
    add_theme_support('title-tag');

    // Enable support for Post Thumbnails
    add_theme_support('post-thumbnails');

    // Enable support for custom logo
    add_theme_support('custom-logo', array(
        'height'      => 100,
        'width'       => 400,
        'flex-height' => true,
        'flex-width'  => true,
    ));

    // Register navigation menus
    register_nav_menus(array(
        'primary' => esc_html__('Primary Menu', 'isnbiz-2026'),
        'footer'  => esc_html__('Footer Menu', 'isnbiz-2026'),
    ));

    // Add support for editor styles
    add_theme_support('editor-styles');

    // Add support for wide alignment
    add_theme_support('align-wide');

    // Add support for responsive embeds
    add_theme_support('responsive-embeds');

    // Set content width
    if (!isset($content_width)) {
        $content_width = 1400;
    }
}
add_action('after_setup_theme', 'isnbiz_theme_setup');

/**
 * Enqueue Styles and Scripts
 */
function isnbiz_enqueue_assets() {
    // Google Fonts
    wp_enqueue_style(
        'isnbiz-google-fonts',
        'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Archivo+Black&family=IBM+Plex+Sans:wght@300;400;600;700&display=swap',
        array(),
        null
    );

    // Main stylesheet
    wp_enqueue_style(
        'isnbiz-style',
        get_stylesheet_uri(),
        array('isnbiz-google-fonts'),
        wp_get_theme()->get('Version')
    );

    // Main JavaScript
    wp_enqueue_script(
        'isnbiz-main-js',
        get_template_directory_uri() . '/assets/js/main.js',
        array(),
        wp_get_theme()->get('Version'),
        true
    );

    // Localize script for AJAX
    wp_localize_script('isnbiz-main-js', 'isnbizAjax', array(
        'ajaxurl' => admin_url('admin-ajax.php'),
        'nonce'   => wp_create_nonce('isnbiz-nonce')
    ));
}
add_action('wp_enqueue_scripts', 'isnbiz_enqueue_assets');

/**
 * Helper function for S3 asset URLs
 */
function isnbiz_s3_url($path = '') {
    $base_url = 'https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com/premium_v3/';
    return esc_url($base_url . ltrim($path, '/'));
}

/**
 * Remove WordPress bloat
 */
function isnbiz_remove_wp_bloat() {
    // Remove emoji scripts
    remove_action('wp_head', 'print_emoji_detection_script', 7);
    remove_action('wp_print_styles', 'print_emoji_styles');
    remove_action('admin_print_scripts', 'print_emoji_detection_script');
    remove_action('admin_print_styles', 'print_emoji_styles');

    // Remove Windows Live Writer manifest
    remove_action('wp_head', 'wlwmanifest_link');

    // Remove WordPress generator meta tag
    remove_action('wp_head', 'wp_generator');

    // Remove shortlink
    remove_action('wp_head', 'wp_shortlink_wp_head');

    // Remove REST API link
    remove_action('wp_head', 'rest_output_link_wp_head');
    remove_action('wp_head', 'wp_oembed_add_discovery_links');

    // Remove RSS feed links (we'll add them back manually if needed)
    remove_action('wp_head', 'feed_links', 2);
    remove_action('wp_head', 'feed_links_extra', 3);
}
add_action('init', 'isnbiz_remove_wp_bloat');

/**
 * Custom navigation walker for accessibility
 */
class ISNBIZ_Walker_Nav_Menu extends Walker_Nav_Menu {
    function start_el(&$output, $item, $depth = 0, $args = null, $id = 0) {
        $indent = ($depth) ? str_repeat("\t", $depth) : '';

        $classes = empty($item->classes) ? array() : (array) $item->classes;
        $classes[] = 'menu-item-' . $item->ID;

        $class_names = join(' ', apply_filters('nav_menu_css_class', array_filter($classes), $item, $args, $depth));
        $class_names = $class_names ? ' class="' . esc_attr($class_names) . '"' : '';

        $id = apply_filters('nav_menu_item_id', 'menu-item-' . $item->ID, $item, $args, $depth);
        $id = $id ? ' id="' . esc_attr($id) . '"' : '';

        $output .= $indent . '<li' . $id . $class_names . ' role="none">';

        $atts = array();
        $atts['title']  = !empty($item->attr_title) ? $item->attr_title : '';
        $atts['target'] = !empty($item->target) ? $item->target : '';
        $atts['rel']    = !empty($item->xfn) ? $item->xfn : '';
        $atts['href']   = !empty($item->url) ? $item->url : '';
        $atts['role']   = 'menuitem';

        // Check if current page
        if (in_array('current-menu-item', $classes)) {
            $atts['aria-current'] = 'page';
            $atts['class'] = 'active';
        }

        $atts = apply_filters('nav_menu_link_attributes', $atts, $item, $args, $depth);

        $attributes = '';
        foreach ($atts as $attr => $value) {
            if (!empty($value)) {
                $value = ('href' === $attr) ? esc_url($value) : esc_attr($value);
                $attributes .= ' ' . $attr . '="' . $value . '"';
            }
        }

        $item_output = $args->before;
        $item_output .= '<a' . $attributes . '>';
        $item_output .= $args->link_before . apply_filters('the_title', $item->title, $item->ID) . $args->link_after;
        $item_output .= '</a>';
        $item_output .= $args->after;

        $output .= apply_filters('walker_nav_menu_start_el', $item_output, $item, $depth, $args);
    }
}

/**
 * Contact Form Handler
 */
function isnbiz_handle_contact_form() {
    check_ajax_referer('isnbiz-contact-form', 'nonce');

    $name = sanitize_text_field($_POST['name']);
    $email = sanitize_email($_POST['email']);
    $company = sanitize_text_field($_POST['company']);
    $interest = sanitize_text_field($_POST['interest']);
    $message = sanitize_textarea_field($_POST['message']);

    // Basic validation
    if (empty($name) || empty($email) || empty($message)) {
        wp_send_json_error('Please fill in all required fields.');
    }

    if (!is_email($email)) {
        wp_send_json_error('Please enter a valid email address.');
    }

    // Prepare email
    $to = get_option('admin_email');
    $subject = 'Contact Form Submission from ' . $name;
    $body = "Name: $name\n";
    $body .= "Email: $email\n";
    $body .= "Company: $company\n";
    $body .= "Interest: $interest\n\n";
    $body .= "Message:\n$message";

    $headers = array('Content-Type: text/plain; charset=UTF-8');

    // Send email
    if (wp_mail($to, $subject, $body, $headers)) {
        wp_send_json_success('Thank you for your message. We will contact you within 24 hours.');
    } else {
        wp_send_json_error('Sorry, there was an error sending your message. Please try again.');
    }
}
add_action('wp_ajax_isnbiz_contact_form', 'isnbiz_handle_contact_form');
add_action('wp_ajax_nopriv_isnbiz_contact_form', 'isnbiz_handle_contact_form');

/**
 * Add preconnect for external domains
 */
function isnbiz_resource_hints($urls, $relation_type) {
    if ('preconnect' === $relation_type) {
        $urls[] = array(
            'href' => 'https://fonts.googleapis.com',
            'crossorigin',
        );
        $urls[] = array(
            'href' => 'https://fonts.gstatic.com',
            'crossorigin',
        );
        $urls[] = array(
            'href' => 'https://isnbiz-assets-1769962280.s3.us-east-1.amazonaws.com',
            'crossorigin',
        );
    }
    return $urls;
}
add_filter('wp_resource_hints', 'isnbiz_resource_hints', 10, 2);

/**
 * Register widget areas
 */
function isnbiz_widgets_init() {
    register_sidebar(array(
        'name'          => esc_html__('Footer Widget Area', 'isnbiz-2026'),
        'id'            => 'footer-widgets',
        'description'   => esc_html__('Add widgets here to appear in your footer.', 'isnbiz-2026'),
        'before_widget' => '<div id="%1$s" class="widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h4 class="widget-title">',
        'after_title'   => '</h4>',
    ));
}
add_action('widgets_init', 'isnbiz_widgets_init');

/**
 * Add WCAG skip link support
 */
function isnbiz_skip_link() {
    echo '<a href="#about" class="skip-link screen-reader-text">' . esc_html__('Skip to main content', 'isnbiz-2026') . '</a>';
}
add_action('wp_body_open', 'isnbiz_skip_link');

/**
 * Custom excerpt length
 */
function isnbiz_excerpt_length($length) {
    return 40;
}
add_filter('excerpt_length', 'isnbiz_excerpt_length', 999);

/**
 * Custom excerpt more string
 */
function isnbiz_excerpt_more($more) {
    return '...';
}
add_filter('excerpt_more', 'isnbiz_excerpt_more');
