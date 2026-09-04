# scratch/restore_slider_arrows.py
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'<div class="swiper-button-prev hero-nav-btn"[^>]*>',
    '<div class="swiper-button-prev hero-nav-btn">',
    html
)
html = re.sub(
    r'<div class="swiper-button-next hero-nav-btn"[^>]*>',
    '<div class="swiper-button-next hero-nav-btn">',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

arrow_css = """
/* ==========================================================================
   Hero Navigation Arrows (Enhanced & Visible)
   ========================================================================== */
.hero-nav-btn {
    width: 48px !important;
    height: 48px !important;
    background: rgba(24, 61, 43, 0.65) !important;
    border: 1.5px solid rgba(212, 163, 115, 0.7) !important;
    border-radius: 50% !important;
    color: #FFFFFF !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    backdrop-filter: blur(6px) !important;
    -webkit-backdrop-filter: blur(6px) !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    z-index: 20 !important;
}

.hero-nav-btn::after {
    display: none !important;
}

.hero-nav-btn i {
    font-size: 1.25rem !important;
    color: #FFFFFF !important;
    transition: transform 0.2s ease !important;
}

.swiper-button-prev.hero-nav-btn {
    left: 28px !important;
}

.swiper-button-next.hero-nav-btn {
    right: 28px !important;
}

.hero-nav-btn:hover {
    background: #C89D66 !important;
    border-color: #D4A373 !important;
    color: #FFFFFF !important;
    transform: scale(1.1) !important;
    box-shadow: 0 6px 20px rgba(200, 157, 102, 0.5) !important;
}

@media (max-width: 768px) {
    .hero-nav-btn {
        width: 38px !important;
        height: 38px !important;
        opacity: 0.85 !important;
    }
    .swiper-button-prev.hero-nav-btn {
        left: 10px !important;
    }
    .swiper-button-next.hero-nav-btn {
        right: 10px !important;
    }
}
"""

css = re.sub(r'/\* ==========================================================================\s*Hero Navigation Arrows[\s\S]*?right: 10px !important;\s*\}\s*\}', '', css)
css += '\n' + arrow_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Restored hero slider navigation arrows in index.html and style.css')
