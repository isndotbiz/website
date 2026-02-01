<!-- Footer -->
<footer class="footer">
    <div class="container">
        <div class="footer-grid">
            <div class="footer-column">
                <img src="<?php echo isnbiz_s3_url('logos/footer_logo.webp'); ?>" alt="<?php bloginfo('name'); ?> Logo" class="footer-logo">
                <p class="footer-description"><?php bloginfo('description'); ?></p>
                <div class="footer-credentials">
                    <p><strong>DUNS:</strong> 080513772</p>
                    <p><strong>UBI:</strong> 603-522-339</p>
                    <p><strong>EIN:</strong> 47-4530188</p>
                </div>
            </div>
            <div class="footer-column">
                <h4><?php esc_html_e('Company', 'isnbiz-2026'); ?></h4>
                <ul class="footer-links">
                    <li><a href="<?php echo esc_url(home_url('/about')); ?>"><?php esc_html_e('About Us', 'isnbiz-2026'); ?></a></li>
                    <li><a href="<?php echo esc_url(home_url('/services')); ?>"><?php esc_html_e('Services', 'isnbiz-2026'); ?></a></li>
                    <li><a href="<?php echo esc_url(home_url('/portfolio')); ?>"><?php esc_html_e('Portfolio', 'isnbiz-2026'); ?></a></li>
                    <li><a href="<?php echo esc_url(home_url('/investors')); ?>"><?php esc_html_e('Investors', 'isnbiz-2026'); ?></a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4><?php esc_html_e('Resources', 'isnbiz-2026'); ?></h4>
                <ul class="footer-links">
                    <li><a href="<?php echo esc_url(home_url('/contact')); ?>"><?php esc_html_e('Contact', 'isnbiz-2026'); ?></a></li>
                    <li><a href="<?php echo esc_url(home_url('/contact')); ?>"><?php esc_html_e('Request Demo', 'isnbiz-2026'); ?></a></li>
                    <li><a href="<?php echo esc_url(home_url('/investors')); ?>"><?php esc_html_e('Pitch Deck', 'isnbiz-2026'); ?></a></li>
                    <li><a href="<?php echo esc_url(home_url('/investors')); ?>"><?php esc_html_e('Investor Relations', 'isnbiz-2026'); ?></a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4><?php esc_html_e('Legal', 'isnbiz-2026'); ?></h4>
                <ul class="footer-links">
                    <li><a href="<?php echo esc_url(home_url('/privacy')); ?>"><?php esc_html_e('Privacy Policy', 'isnbiz-2026'); ?></a></li>
                    <li><a href="<?php echo esc_url(home_url('/terms')); ?>"><?php esc_html_e('Terms of Service', 'isnbiz-2026'); ?></a></li>
                    <li><a href="<?php echo esc_url(home_url('/security')); ?>"><?php esc_html_e('Security', 'isnbiz-2026'); ?></a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; <?php echo date('Y'); ?> <?php bloginfo('name'); ?>. <?php esc_html_e('All rights reserved.', 'isnbiz-2026'); ?></p>
            <p><?php esc_html_e('Founded July 8, 2015 | Seattle, Washington', 'isnbiz-2026'); ?></p>
        </div>
    </div>
</footer>

<script>
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const syncNavState = () => {
        const isOpen = navMenu.classList.contains('active');
        navToggle.setAttribute('aria-expanded', isOpen.toString());
    };

    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        syncNavState();
    });

    // Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                syncNavState();
            }
        });
    });

    // Sticky Navigation
    const nav = document.querySelector('.nav');
    const navHeight = nav.offsetHeight;

    window.addEventListener('scroll', () => {
        if (window.scrollY > navHeight) {
            nav.classList.add('nav-sticky');
        } else {
            nav.classList.remove('nav-sticky');
        }
    });

    // Intersection Observer for Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observe all sections
    document.querySelectorAll('.section').forEach(section => {
        observer.observe(section);
    });
</script>

<?php wp_footer(); ?>
</body>
</html>
