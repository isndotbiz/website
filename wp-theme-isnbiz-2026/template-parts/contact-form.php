<?php
/**
 * Template part for contact form
 *
 * @package ISN_BIZ_2026
 */
?>

<div class="section-header centered">
    <span class="section-label"><?php esc_html_e('Get in Touch', 'isnbiz-2026'); ?></span>
    <h2 class="section-title"><?php esc_html_e('Let\'s Start a Conversation', 'isnbiz-2026'); ?></h2>
    <p class="section-description"><?php esc_html_e('Whether you\'re interested in our solutions or investment opportunities, we\'d love to hear from you', 'isnbiz-2026'); ?></p>
</div>
<div class="contact-grid">
    <div class="contact-form-container">
        <form class="contact-form" id="contactForm">
            <?php wp_nonce_field('isnbiz-contact-form', 'contact_nonce'); ?>

            <div class="form-group">
                <label for="name"><?php esc_html_e('Full Name *', 'isnbiz-2026'); ?></label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email"><?php esc_html_e('Email Address *', 'isnbiz-2026'); ?></label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="company"><?php esc_html_e('Company', 'isnbiz-2026'); ?></label>
                <input type="text" id="company" name="company">
            </div>
            <div class="form-group">
                <label for="interest"><?php esc_html_e('I\'m interested in:', 'isnbiz-2026'); ?></label>
                <select id="interest" name="interest">
                    <option value="investment"><?php esc_html_e('Investment Opportunities', 'isnbiz-2026'); ?></option>
                    <option value="demo"><?php esc_html_e('Product Demo', 'isnbiz-2026'); ?></option>
                    <option value="partnership"><?php esc_html_e('Partnership Opportunities', 'isnbiz-2026'); ?></option>
                    <option value="services"><?php esc_html_e('Software Development Services', 'isnbiz-2026'); ?></option>
                    <option value="other"><?php esc_html_e('Other', 'isnbiz-2026'); ?></option>
                </select>
            </div>
            <div class="form-group">
                <label for="message"><?php esc_html_e('Message *', 'isnbiz-2026'); ?></label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary btn-full"><?php esc_html_e('Send Message', 'isnbiz-2026'); ?></button>
            <p class="form-privacy"><?php esc_html_e('We respect your privacy. Your information will be kept confidential.', 'isnbiz-2026'); ?></p>
        </form>
    </div>
    <div class="contact-info">
        <div class="contact-card">
            <h3><?php esc_html_e('Company Information', 'isnbiz-2026'); ?></h3>
            <div class="contact-details">
                <div class="contact-item">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle>
                    </svg>
                    <div>
                        <strong><?php esc_html_e('Headquarters', 'isnbiz-2026'); ?></strong>
                        <p><?php esc_html_e('Seattle, Washington', 'isnbiz-2026'); ?></p>
                    </div>
                </div>
                <div class="contact-item">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                        <polyline points="22,6 12,13 2,6"></polyline>
                    </svg>
                    <div>
                        <strong><?php esc_html_e('Email', 'isnbiz-2026'); ?></strong>
                        <p><a href="mailto:info@isn.biz">info@isn.biz</a></p>
                    </div>
                </div>
                <div class="contact-item">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                    </svg>
                    <div>
                        <strong><?php esc_html_e('Website', 'isnbiz-2026'); ?></strong>
                        <p><a href="https://isn.biz">isn.biz</a></p>
                    </div>
                </div>
            </div>
        </div>
        <div class="contact-card">
            <h3><?php esc_html_e('For Investors', 'isnbiz-2026'); ?></h3>
            <p><?php esc_html_e('Qualified investors can request access to our secure data room for detailed financial information, product roadmap, and due diligence materials.', 'isnbiz-2026'); ?></p>
            <a href="#contact" class="btn btn-outline btn-small"><?php esc_html_e('Request Data Room Access', 'isnbiz-2026'); ?></a>
        </div>
        <div class="contact-card">
            <h3><?php esc_html_e('Response Time', 'isnbiz-2026'); ?></h3>
            <p><?php esc_html_e('We typically respond to all inquiries within 24 business hours. For urgent matters, please indicate in your message.', 'isnbiz-2026'); ?></p>
        </div>
    </div>
</div>

<script>
// Contact Form Handler
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    formData.append('action', 'isnbiz_contact_form');
    formData.append('nonce', '<?php echo wp_create_nonce('isnbiz-contact-form'); ?>');

    fetch('<?php echo admin_url('admin-ajax.php'); ?>', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.data);
            this.reset();
        } else {
            alert(data.data || 'There was an error sending your message.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error sending your message. Please try again.');
    });
});
</script>
