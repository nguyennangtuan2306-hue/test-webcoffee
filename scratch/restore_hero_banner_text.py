# scratch/restore_hero_banner_text.py
import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

hero_text_css = """
/* ==========================================================================
   Hero Banner Content & Typography (Restored & Guaranteed Visibility)
   ========================================================================== */
.hero-content {
    position: relative;
    z-index: 2;
    max-width: 1080px;
    width: 100%;
    padding: 0 24px;
    margin-top: 40px;
    text-align: center;
    user-select: none;
}

.hero-line-1 {
    font-family: 'Playfair Display', serif !important;
    font-size: clamp(1.8rem, 4vw, 3.4rem) !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
    text-transform: uppercase !important;
    letter-spacing: clamp(1.5px, 0.3vw, 3px) !important;
    margin-bottom: 12px !important;
    text-shadow: 0 4px 20px rgba(0, 0, 0, 0.9), 0 2px 8px rgba(0, 0, 0, 0.95) !important;
    text-wrap: balance !important;
    max-width: 100% !important;
    opacity: 1 !important;
    transform: none !important;
    display: block !important;
}

.hero-line-2 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.5rem, 3.2vw, 2.6rem) !important;
    font-style: italic !important;
    font-weight: 500 !important;
    color: #D4A373 !important;
    margin-bottom: 14px !important;
    letter-spacing: 0.5px !important;
    text-shadow: 0 3px 15px rgba(0, 0, 0, 0.9) !important;
    text-wrap: balance !important;
    max-width: 100% !important;
    opacity: 1 !important;
    transform: none !important;
    display: block !important;
}

.hero-line-3 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: clamp(0.92rem, 1.8vw, 1.15rem) !important;
    font-weight: 500 !important;
    color: #EDE4D8 !important;
    max-width: 820px !important;
    margin: 0 auto 28px !important;
    letter-spacing: 0.3px !important;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95) !important;
    text-wrap: balance !important;
    opacity: 1 !important;
    transform: none !important;
    display: block !important;
}

.swiper-slide-active .hero-line-1,
.swiper-slide-active .hero-line-2,
.swiper-slide-active .hero-line-3,
.swiper-slide-active .hero-actions {
    opacity: 1 !important;
    transform: none !important;
}
"""

css = re.sub(r'\.hero-content\s*\{[\s\S]*?\.hero-line-3\s*\{[^}]*\}', '', css)
css = re.sub(r'/\* ==========================================================================\s*Hero Banner Content & Typography[\s\S]*?transform: none !important;\s*\}', '', css)

css += '\n' + hero_text_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Restored hero banner text styles in style.css')
