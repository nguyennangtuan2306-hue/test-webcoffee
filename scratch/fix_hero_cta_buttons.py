# scratch/fix_hero_cta_buttons.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

hero_actions_css = """
.hero-actions {
    display: flex !important;
    gap: 16px !important;
    justify-content: center !important;
    align-items: center !important;
    flex-wrap: wrap !important;
    margin-top: 24px !important;
    width: 100% !important;
}

.btn-hero-primary {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    white-space: nowrap !important;
    padding: 12px 24px !important;
    border-radius: 9999px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    background-color: #C89D66 !important;
    color: #FFFFFF !important;
    border: 1.5px solid #D4A373 !important;
    text-decoration: none !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;
    transition: all 0.3s ease !important;
}

.btn-hero-primary:hover {
    background-color: #B58B55 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(200, 157, 102, 0.45) !important;
}

.btn-hero-secondary {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    white-space: nowrap !important;
    padding: 12px 24px !important;
    border-radius: 9999px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    background: rgba(24, 61, 43, 0.75) !important;
    color: #FFFFFF !important;
    border: 1.5px solid rgba(212, 163, 115, 0.7) !important;
    backdrop-filter: blur(6px) !important;
    text-decoration: none !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;
    transition: all 0.3s ease !important;
}

.btn-hero-secondary:hover {
    border-color: #E0A96D !important;
    color: #E0A96D !important;
    background: rgba(24, 61, 43, 0.95) !important;
    transform: translateY(-2px) !important;
}
"""

css = re.sub(r'\.hero-actions\s*\{[\s\S]*?\.btn-hero-secondary:hover\s*\{[^}]*\}', hero_actions_css.strip(), css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

btn_p_style = "display: inline-flex !important; align-items: center !important; justify-content: center !important; white-space: nowrap !important; padding: 12px 24px !important; border-radius: 9999px !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.05em !important; text-transform: uppercase !important; background-color: #C89D66 !important; color: #FFFFFF !important; border: 1.5px solid #D4A373 !important; text-decoration: none !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;"

btn_s_style = "display: inline-flex !important; align-items: center !important; justify-content: center !important; white-space: nowrap !important; padding: 12px 24px !important; border-radius: 9999px !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.05em !important; text-transform: uppercase !important; background: rgba(24, 61, 43, 0.75) !important; color: #FFFFFF !important; border: 1.5px solid rgba(212, 163, 115, 0.7) !important; backdrop-filter: blur(6px) !important; text-decoration: none !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;"

actions_wrap_style = "display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;"

slide1_actions = f'''<div class="hero-actions" style="{actions_wrap_style}">
                            <a href="menu.html" class="btn-hero-primary" style="{btn_p_style}">KHÁM PHÁ THỰC ĐƠN</a>
                            <a href="franchise.html" class="btn-hero-secondary" style="{btn_s_style}">HỢP TÁC NHƯỢNG QUYỀN</a>
                        </div>'''

slide2_actions = f'''<div class="hero-actions" style="{actions_wrap_style}">
                            <a href="about.html" class="btn-hero-primary" style="{btn_p_style}">VỀ HEAVEN</a>
                            <a href="franchise.html" class="btn-hero-secondary" style="{btn_s_style}">TƯ VẤN ĐẦU TƯ</a>
                        </div>'''

slide3_actions = f'''<div class="hero-actions" style="{actions_wrap_style}">
                            <a href="franchise.html" class="btn-hero-primary" style="{btn_p_style}">TƯ VẤN ĐẦU TƯ</a>
                            <a href="contact.html" class="btn-hero-secondary" style="{btn_s_style}">HỆ THỐNG CƠ SỞ</a>
                        </div>'''

idx = re.sub(r'<div class="hero-actions"[^>]*>[\s\S]*?KHÁM PHÁ THỰC ĐƠN[\s\S]*?HỢP TÁC NHƯỢNG QUYỀN[\s\S]*?</div>', slide1_actions, idx)
idx = re.sub(r'<div class="hero-actions"[^>]*>[\s\S]*?VỀ HEAVEN[\s\S]*?TƯ VẤN ĐẦU TƯ[\s\S]*?</div>', slide2_actions, idx)
idx = re.sub(r'<div class="hero-actions"[^>]*>[\s\S]*?TƯ VẤN ĐẦU TƯ[\s\S]*?HỆ THỐNG CƠ SỞ[\s\S]*?</div>', slide3_actions, idx)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print('Updated Hero CTA button separation in index.html and style.css')
