# scratch/fix_pricing_cards_typography.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

pricing_css = """
.pricing-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
    color: #1E3932 !important;
    margin-bottom: 14px !important;
    letter-spacing: 0.2px !important;
}

.pricing-fee {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 2.25rem !important;
    font-weight: 800 !important;
    color: #C0904D !important;
    font-variant-numeric: normal !important;
    letter-spacing: -0.025em !important;
    margin-bottom: 20px !important;
    line-height: 1 !important;
    display: flex !important;
    align-items: baseline !important;
    gap: 8px !important;
}

.pricing-fee span {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    color: #6B7280 !important;
}
"""

css = re.sub(r'\.pricing-title\s*\{[^}]*\}', '', css)
css = re.sub(r'\.pricing-fee\s*\{[^}]*\}', '', css)
css = re.sub(r'\.pricing-fee span\s*\{[^}]*\}', '', css)
css += '\n' + pricing_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update franchise.html
with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

card1_title = '<h3 class="pricing-title" style="font-family: \'Cormorant Garamond\', serif !important; font-weight: 700 !important; color: #1E3932 !important; font-size: 1.4rem !important; letter-spacing: 0.2px !important;">Thành Phố Trực Thuộc Trung Ương</h3>'
card1_fee = '<div class="pricing-fee" style="font-family: \'Plus Jakarta Sans\', sans-serif !important; font-size: 2.25rem !important; font-weight: 800 !important; color: #C0904D !important; font-variant-numeric: normal !important; letter-spacing: -0.025em !important; display: flex !important; align-items: baseline !important; gap: 8px !important;">350.000.000đ <span style="font-family: \'Plus Jakarta Sans\', sans-serif !important; font-weight: 500 !important; font-size: 14px !important; color: #6B7280 !important;">/ 5 năm</span></div>'

card2_title = '<h3 class="pricing-title" style="font-family: \'Cormorant Garamond\', serif !important; font-weight: 700 !important; color: #1E3932 !important; font-size: 1.4rem !important; letter-spacing: 0.2px !important;">KĐT Vùng Ven & Các Tỉnh</h3>'
card2_fee = '<div class="pricing-fee" style="font-family: \'Plus Jakarta Sans\', sans-serif !important; font-size: 2.25rem !important; font-weight: 800 !important; color: #C0904D !important; font-variant-numeric: normal !important; letter-spacing: -0.025em !important; display: flex !important; align-items: baseline !important; gap: 8px !important;">300.000.000đ <span style="font-family: \'Plus Jakarta Sans\', sans-serif !important; font-weight: 500 !important; font-size: 14px !important; color: #6B7280 !important;">/ 5 năm</span></div>'

fran = re.sub(r'<h3 class="pricing-title"[^>]*>Thành Phố Trực Thuộc Trung Ương</h3>', card1_title, fran)
fran = re.sub(r'<div class="pricing-fee"[^>]*>350\.000\.000đ[\s\S]*?</div>', card1_fee, fran)

fran = re.sub(r'<h3 class="pricing-title"[^>]*>KĐT Vùng Ven & Các Tỉnh</h3>', card2_title, fran)
fran = re.sub(r'<div class="pricing-fee"[^>]*>300\.000\.000đ[\s\S]*?</div>', card2_fee, fran)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

print('Updated Pricing Cards typography in style.css and franchise.html successfully.')
