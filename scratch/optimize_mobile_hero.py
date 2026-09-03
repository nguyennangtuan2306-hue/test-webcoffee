# scratch/optimize_mobile_hero.py
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_hero_css = """
/* ==========================================================================
   Mobile Responsive Optimizations for Hero & Header (< 768px)
   ========================================================================== */
@media (max-width: 768px) {
    /* Header layout */
    .site-header {
        padding: 10px 0;
    }

    .header-container {
        padding: 0 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
    }

    .logo-brand {
        flex-shrink: 0;
    }

    .logo-main {
        font-size: 1.35rem !important;
    }

    .logo-sub {
        font-size: 0.62rem !important;
    }

    .header-cta {
        margin: 0;
        margin-left: auto;
        display: flex;
        align-items: center;
    }

    .header-cta a {
        padding: 6px 12px !important;
        font-size: 11px !important;
        gap: 4px !important;
        letter-spacing: 0.03em !important;
    }

    .mobile-toggle {
        display: flex !important;
        flex-shrink: 0;
        margin-left: 8px;
        z-index: 1001;
    }

    /* Ẩn hoàn toàn 2 nút mũi tên slider trên mobile */
    .hero-nav-btn,
    .swiper-button-prev.hero-nav-btn,
    .swiper-button-next.hero-nav-btn {
        display: none !important;
    }

    /* Hero Section Content */
    .hero-slider-section {
        min-height: 100vh;
        height: 100vh;
    }

    .hero-slide-content {
        padding: 85px 16px 50px;
        max-width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    .hero-line-1 {
        font-size: clamp(1.5rem, 6.5vw, 2.1rem) !important;
        letter-spacing: 1.5px !important;
        margin-bottom: 6px !important;
        line-height: 1.25 !important;
    }

    .hero-line-2 {
        font-size: clamp(1.1rem, 4.8vw, 1.45rem) !important;
        margin-bottom: 10px !important;
        line-height: 1.3 !important;
    }

    .hero-line-3 {
        font-size: 0.8rem !important;
        line-height: 1.55 !important;
        padding: 0 8px !important;
        margin: 0 auto 20px !important;
        max-width: 310px !important;
        color: #EDE4D8 !important;
        text-wrap: balance !important;
    }

    .hero-actions {
        display: flex !important;
        flex-direction: row !important;
        gap: 10px !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        max-width: 340px !important;
        margin: 0 auto !important;
    }

    .btn-hero-primary,
    .btn-hero-secondary {
        flex: 1 1 0 !important;
        padding: 10px 10px !important;
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        border-radius: 50px !important;
        letter-spacing: 0.5px !important;
        text-align: center !important;
        white-space: nowrap !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    }
}
"""

if 'Mobile Responsive Optimizations for Hero & Header' in css:
    import re
    css = re.sub(r'/\* ==========================================================================\s*Mobile Responsive Optimizations for Hero & Header[\s\S]*?/\* ==========================================================================', '/* ==========================================================================', css)

css += '\n' + mobile_hero_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated mobile hero optimizations in style.css')
