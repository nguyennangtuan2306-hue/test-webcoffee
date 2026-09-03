# scratch/optimize_pricing_cards_layout.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

pricing_css_block = """
/* Pricing Cards Header & Layout */
.pricing-header-block {
    text-align: center;
    border-bottom: 1px solid #EAEFE9;
    padding-bottom: 22px;
    margin-bottom: 22px;
}

.pricing-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    color: #1B382B !important;
    letter-spacing: 1.5px !important;
    margin-bottom: 12px !important;
    text-align: center !important;
}

.pricing-fee {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    color: #C59B27 !important;
    font-variant-numeric: normal !important;
    letter-spacing: -0.025em !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    line-height: 1.1 !important;
    gap: 4px !important;
    text-align: center !important;
}

.pricing-fee .pricing-period {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    color: #8C9A8E !important;
    margin-top: 4px !important;
    letter-spacing: 0.5px !important;
}
"""

css = re.sub(r'/\* Pricing Cards Header & Layout[\s\S]*?\.pricing-fee \.pricing-period\s*\{[^}]*\}', '', css)
css += '\n' + pricing_css_block

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update franchise.html
with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

card1_block = """                    <span class="pricing-badge">ƯU TIÊN HÀ NỘI & TP.HCM</span>
                    <div class="pricing-header-block" style="text-align: center; border-bottom: 1px solid #EAEFE9; padding-bottom: 22px; margin-bottom: 22px;">
                        <h3 class="pricing-title" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 700 !important; font-size: 1rem !important; text-transform: uppercase !important; color: #1B382B !important; letter-spacing: 1.5px !important; margin-bottom: 12px !important; text-align: center !important;">Thành Phố Trực Thuộc Trung Ương</h3>
                        <div class="pricing-fee" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #C59B27 !important; font-variant-numeric: normal !important; letter-spacing: -0.025em !important; display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; line-height: 1.1 !important; gap: 4px !important; text-align: center !important;">
                            <span>350.000.000đ</span>
                            <span class="pricing-period" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 500 !important; font-size: 0.85rem !important; color: #8C9A8E !important; margin-top: 4px !important; letter-spacing: 0.5px !important;">/ 5 năm</span>
                        </div>
                    </div>"""

card2_block = """                    <div class="pricing-header-block" style="text-align: center; border-bottom: 1px solid #EAEFE9; padding-bottom: 22px; margin-bottom: 22px;">
                        <h3 class="pricing-title" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 700 !important; font-size: 1rem !important; text-transform: uppercase !important; color: #1B382B !important; letter-spacing: 1.5px !important; margin-bottom: 12px !important; text-align: center !important;">KĐT Vùng Ven & Các Tỉnh</h3>
                        <div class="pricing-fee" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #C59B27 !important; font-variant-numeric: normal !important; letter-spacing: -0.025em !important; display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; line-height: 1.1 !important; gap: 4px !important; text-align: center !important;">
                            <span>300.000.000đ</span>
                            <span class="pricing-period" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 500 !important; font-size: 0.85rem !important; color: #8C9A8E !important; margin-top: 4px !important; letter-spacing: 0.5px !important;">/ 5 năm</span>
                        </div>
                    </div>"""

fran = re.sub(
    r'<span class="pricing-badge">ƯU TIÊN HÀ NỘI & TP\.HCM</span>[\s\S]*?<div class="pricing-fee"[^>]*>350\.000\.000đ[\s\S]*?</div>',
    card1_block,
    fran
)

fran = re.sub(
    r'<h3 class="pricing-title"[^>]*>KĐT Vùng Ven & Các Tỉnh</h3>[\s\S]*?<div class="pricing-fee"[^>]*>300\.000\.000đ[\s\S]*?</div>',
    card2_block,
    fran
)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

print('Optimized pricing cards layout and typography successfully.')
