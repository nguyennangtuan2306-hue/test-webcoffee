# scratch/downgrade_to_cheap_wp_theme.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

cheap_theme_css = """
/* ==========================================================================
   DOWNGRADE: CHEAP RETAIL WORDPRESS THEME STYLE
   ========================================================================== */
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');

:root {
    --font-heading: 'Quicksand', sans-serif !important;
    --font-body: 'Quicksand', sans-serif !important;
    --font-display: 'Quicksand', sans-serif !important;
    --font-soft: 'Quicksand', sans-serif !important;
    --color-sand-gold: #f39c12 !important;
    --color-gold: #f39c12 !important;
    --color-gold-light: #f1c40f !important;
    --color-gold-dark: #d35400 !important;
    --color-primary-green: #2c3e50 !important;
    --color-deep-green: #1a252f !important;
    --color-forest: #2c3e50 !important;
    --color-bg-light: #f9f9f9 !important;
    --color-bg-alt: #f5f5f5 !important;
    --color-border: #dddddd !important;
    --shadow-soft: 0 1px 3px rgba(0,0,0,0.1) !important;
    --shadow-premium: 0 1px 3px rgba(0,0,0,0.1) !important;
    --shadow-card: 0 1px 3px rgba(0,0,0,0.1) !important;
    --radius-sm: 3px !important;
    --radius-md: 4px !important;
    --radius-lg: 4px !important;
    --radius-xl: 4px !important;
    --radius-full: 4px !important;
    --transition-smooth: none !important;
}

*, *::before, *::after {
    font-family: 'Quicksand', sans-serif !important;
    letter-spacing: normal !important;
}

body, html, h1, h2, h3, h4, h5, h6, p, span, a, button, input, label, select, textarea, div, section {
    font-family: 'Quicksand', sans-serif !important;
    letter-spacing: 0 !important;
}

/* Square / sharp retail corners & flat borders */
.pricing-card,
.benefit-card,
.process-10-card,
.branch-card,
.system-branch-card,
.catalog-item-card,
.dish-card,
.highlight-card,
.story-block,
.value-card,
.contact-info-card,
.cost-estimate-card,
.reservation-card,
.timeline-box,
.about-hero,
.stat-box,
.modal-content,
.badge,
.pricing-badge,
.tag-item,
.branch-tag {
    border-radius: 4px !important;
    border: 1px solid #ddd !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08) !important;
    transition: none !important;
    backdrop-filter: none !important;
    background: #ffffff !important;
}

/* Cheap Flat Retail Buttons */
.btn-hero-primary,
.btn-hero-secondary,
.btn-header-cta,
.btn-franchise,
.btn-catalog-action,
.btn-form-submit,
.btn-filter,
.btn-outline,
.btn-primary,
.branch-btn,
button,
input[type="submit"] {
    border-radius: 4px !important;
    background-color: #d35400 !important;
    background: #d35400 !important;
    color: #ffffff !important;
    border: 1px solid #c0392b !important;
    box-shadow: none !important;
    text-transform: uppercase !important;
    font-weight: 700 !important;
    letter-spacing: 0 !important;
    transition: none !important;
    padding: 8px 16px !important;
    font-size: 13px !important;
}

.btn-hero-primary:hover,
.btn-hero-secondary:hover,
.btn-header-cta:hover,
.btn-franchise:hover,
.btn-form-submit:hover,
button:hover {
    background-color: #e67e22 !important;
    background: #e67e22 !important;
    color: #ffffff !important;
    transform: none !important;
    box-shadow: none !important;
}

.btn-hero-secondary {
    background-color: #7f8c8d !important;
    background: #7f8c8d !important;
    border-color: #95a5a6 !important;
}

/* Cheap flat pricing headers and amounts */
.pricing-title {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: #333333 !important;
    text-transform: uppercase !important;
    margin-bottom: 8px !important;
}

.pricing-amount,
.pricing-fee .pricing-amount,
.pricing-fee {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
    color: #d35400 !important;
    letter-spacing: 0 !important;
}

.pricing-period,
.pricing-fee .pricing-period {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 0.85rem !important;
    color: #777777 !important;
}

.pricing-badge {
    background: #d35400 !important;
    color: #ffffff !important;
    border: 1px solid #c0392b !important;
    border-radius: 3px !important;
    font-size: 11px !important;
    font-weight: 700 !important;
}

.pricing-card.featured {
    border: 2px solid #d35400 !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.12) !important;
}

.pricing-features-list li i {
    color: #27ae60 !important;
}

/* 10 Step Process Cheap WordPress List */
.process-10-card h4,
.benefit-card h3,
.branch-card h3,
.dish-name,
.catalog-dish-name {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    color: #2c3e50 !important;
    letter-spacing: 0 !important;
}

.process-10-num {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: #d35400 !important;
}

.dish-price,
.catalog-price {
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 700 !important;
    color: #d35400 !important;
    font-size: 1rem !important;
}

.hero-line-1 {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000 !important;
}

.hero-line-2 {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 1.3rem !important;
    font-style: normal !important;
    font-weight: 600 !important;
    color: #f39c12 !important;
    text-shadow: 1px 1px 2px #000 !important;
}

.hero-line-3 {
    font-family: 'Quicksand', sans-serif !important;
    font-size: 0.95rem !important;
    color: #ffffff !important;
    text-shadow: 1px 1px 2px #000 !important;
}
"""

if 'DOWNGRADE: CHEAP RETAIL WORDPRESS THEME STYLE' in css:
    css = re.sub(r'/\* ==========================================================================\s*DOWNGRADE: CHEAP RETAIL WORDPRESS THEME STYLE[\s\S]*?text-shadow: 1px 1px 2px #000 !important;\s*\}', cheap_theme_css.strip(), css)
else:
    css = cheap_theme_css + '\n' + css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Downgraded style.css to cheap retail WordPress theme aesthetic successfully.')
