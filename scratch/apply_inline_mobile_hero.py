# scratch/apply_inline_mobile_hero.py
import re

html_files = ['index.html', 'about.html', 'menu.html', 'franchise.html', 'contact.html']

header_btn_html = '''<div class="header-cta">
                <a href="franchise.html" style="display: inline-flex !important; flex-direction: row !important; align-items: center !important; white-space: nowrap !important; padding: 6px 12px !important; font-size: 11px !important; font-weight: 700 !important; background-color: #C89D66 !important; color: #fff !important; border-radius: 9999px !important; gap: 4px !important; text-decoration: none !important;">
                    <span>🤝</span>
                    <span>NHƯỢNG QUYỀN</span>
                </a>
            </div>'''

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<div class="header-cta">[\s\S]*?NHƯỢNG QUYỀN[\s\S]*?</div>'
    content = re.sub(pattern, header_btn_html, content)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html hero banner specifically
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Hide slider arrows
idx = re.sub(
    r'<div class="swiper-button-prev hero-nav-btn"[^>]*>',
    r'<div class="swiper-button-prev hero-nav-btn" style="display: none !important;">',
    idx
)
idx = re.sub(
    r'<div class="swiper-button-next hero-nav-btn"[^>]*>',
    r'<div class="swiper-button-next hero-nav-btn" style="display: none !important;">',
    idx
)

# Replace slide 1 hero actions
slide1_actions = '''<div class="hero-actions" style="display: flex !important; flex-direction: row !important; justify-content: center !important; gap: 10px !important; width: 100% !important; padding: 0 16px !important;">
                            <a href="menu.html" class="btn-hero-primary" style="flex: 1 !important; max-width: 160px !important; padding: 10px 12px !important; border-radius: 8px !important; font-size: 12px !important; font-weight: 700 !important; text-align: center !important; text-transform: uppercase !important; background-color: #C89D66 !important; color: #FFFFFF !important; border: 1px solid #D4A373 !important; text-decoration: none !important; white-space: nowrap !important; display: inline-flex !important; align-items: center !important; justify-content: center !important;">KHÁM PHÁ THỰC ĐƠN</a>
                            <a href="franchise.html" class="btn-hero-secondary" style="flex: 1 !important; max-width: 160px !important; padding: 10px 12px !important; border-radius: 8px !important; font-size: 12px !important; font-weight: 700 !important; text-align: center !important; text-transform: uppercase !important; background: rgba(24, 61, 43, 0.7) !important; color: #FFFFFF !important; border: 1px solid rgba(212, 163, 115, 0.6) !important; text-decoration: none !important; white-space: nowrap !important; display: inline-flex !important; align-items: center !important; justify-content: center !important;">HỢP TÁC NHƯỢNG QUYỀN</a>
                        </div>'''

slide2_actions = '''<div class="hero-actions" style="display: flex !important; flex-direction: row !important; justify-content: center !important; gap: 10px !important; width: 100% !important; padding: 0 16px !important;">
                            <a href="about.html" class="btn-hero-primary" style="flex: 1 !important; max-width: 160px !important; padding: 10px 12px !important; border-radius: 8px !important; font-size: 12px !important; font-weight: 700 !important; text-align: center !important; text-transform: uppercase !important; background-color: #C89D66 !important; color: #FFFFFF !important; border: 1px solid #D4A373 !important; text-decoration: none !important; white-space: nowrap !important; display: inline-flex !important; align-items: center !important; justify-content: center !important;">VỀ HEAVEN</a>
                            <a href="franchise.html" class="btn-hero-secondary" style="flex: 1 !important; max-width: 160px !important; padding: 10px 12px !important; border-radius: 8px !important; font-size: 12px !important; font-weight: 700 !important; text-align: center !important; text-transform: uppercase !important; background: rgba(24, 61, 43, 0.7) !important; color: #FFFFFF !important; border: 1px solid rgba(212, 163, 115, 0.6) !important; text-decoration: none !important; white-space: nowrap !important; display: inline-flex !important; align-items: center !important; justify-content: center !important;">TƯ VẤN ĐẦU TƯ</a>
                        </div>'''

slide3_actions = '''<div class="hero-actions" style="display: flex !important; flex-direction: row !important; justify-content: center !important; gap: 10px !important; width: 100% !important; padding: 0 16px !important;">
                            <a href="franchise.html" class="btn-hero-primary" style="flex: 1 !important; max-width: 160px !important; padding: 10px 12px !important; border-radius: 8px !important; font-size: 12px !important; font-weight: 700 !important; text-align: center !important; text-transform: uppercase !important; background-color: #C89D66 !important; color: #FFFFFF !important; border: 1px solid #D4A373 !important; text-decoration: none !important; white-space: nowrap !important; display: inline-flex !important; align-items: center !important; justify-content: center !important;">TƯ VẤN ĐẦU TƯ</a>
                            <a href="contact.html" class="btn-hero-secondary" style="flex: 1 !important; max-width: 160px !important; padding: 10px 12px !important; border-radius: 8px !important; font-size: 12px !important; font-weight: 700 !important; text-align: center !important; text-transform: uppercase !important; background: rgba(24, 61, 43, 0.7) !important; color: #FFFFFF !important; border: 1px solid rgba(212, 163, 115, 0.6) !important; text-decoration: none !important; white-space: nowrap !important; display: inline-flex !important; align-items: center !important; justify-content: center !important;">HỆ THỐNG CƠ SỞ</a>
                        </div>'''

# Replace each slide's hero-actions in index.html
idx = re.sub(r'<div class="hero-actions">[\s\S]*?KHÁM PHÁ THỰC ĐƠN[\s\S]*?HỢP TÁC NHƯỢNG QUYỀN[\s\S]*?</div>', slide1_actions, idx)
idx = re.sub(r'<div class="hero-actions">[\s\S]*?VỀ HEAVEN[\s\S]*?TƯ VẤN ĐẦU TƯ[\s\S]*?</div>', slide2_actions, idx)
idx = re.sub(r'<div class="hero-actions">[\s\S]*?TƯ VẤN ĐẦU TƯ[\s\S]*?HỆ THỐNG CƠ SỞ[\s\S]*?</div>', slide3_actions, idx)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print('Applied all direct inline styles to Header and Hero Banner successfully.')
