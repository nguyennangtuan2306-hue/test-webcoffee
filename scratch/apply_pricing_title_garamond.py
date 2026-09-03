# scratch/apply_pricing_title_garamond.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

pricing_title_css = """
.pricing-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.35rem !important;
    font-weight: 700 !important;
    text-transform: none !important;
    color: #1B382B !important;
    letter-spacing: 0.2px !important;
    line-height: 1.3 !important;
    margin-bottom: 12px !important;
    text-align: center !important;
}
"""

css = re.sub(r'\.pricing-title\s*\{[^}]*\}', '', css)
css += '\n' + pricing_title_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update franchise.html
with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

card1_title = '<h3 class="pricing-title" style="font-family: \'Cormorant Garamond\', serif !important; font-weight: 700 !important; font-size: 1.35rem !important; text-transform: none !important; color: #1B382B !important; letter-spacing: 0.2px !important; line-height: 1.3 !important; margin-bottom: 12px !important; text-align: center !important;">Thành Phố Trực Thuộc Trung Ương</h3>'

card2_title = '<h3 class="pricing-title" style="font-family: \'Cormorant Garamond\', serif !important; font-weight: 700 !important; font-size: 1.35rem !important; text-transform: none !important; color: #1B382B !important; letter-spacing: 0.2px !important; line-height: 1.3 !important; margin-bottom: 12px !important; text-align: center !important;">KĐT Vùng Ven &amp; Các Tỉnh</h3>'

fran = re.sub(r'<h3 class="pricing-title"[^>]*>[\s\S]*?TRUNG ƯƠNG</h3>', card1_title, fran)
fran = re.sub(r'<h3 class="pricing-title"[^>]*>[\s\S]*?CÁC TỈNH</h3>', card2_title, fran)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

print('Updated pricing package titles to Cormorant Garamond titlecase.')
