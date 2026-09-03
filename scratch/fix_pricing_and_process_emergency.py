# scratch/fix_pricing_and_process_emergency.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

emergency_css = """
/* Emergency Fix for Pricing & Process Cards */
.pricing-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    color: #1B382B !important;
    letter-spacing: 0.5px !important;
    line-height: 1.35 !important;
    margin-bottom: 12px !important;
    text-align: center !important;
}

.pricing-fee {
    margin: 10px 0 4px 0 !important;
    text-align: center !important;
    display: block !important;
}

.pricing-amount,
.pricing-fee .pricing-amount {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    color: #C59B27 !important;
    line-height: 1.2 !important;
    display: block !important;
    text-align: center !important;
    font-variant-numeric: normal !important;
    letter-spacing: -0.02em !important;
}

.pricing-period,
.pricing-fee .pricing-period {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    color: #8C9A8E !important;
    display: block !important;
    text-align: center !important;
    margin-top: 2px !important;
}

.process-10-card h4 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    color: #1B382B !important;
    margin-bottom: 8px !important;
    line-height: 1.25 !important;
    text-wrap: balance !important;
    letter-spacing: 0.1px !important;
}
"""

css = re.sub(r'/\* Emergency Fix for Pricing & Process Cards[\s\S]*?letter-spacing: 0\.1px !important;\s*\}', '', css)
css += '\n' + emergency_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update franchise.html
with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

card1_new = """                    <span class="pricing-badge">ƯU TIÊN HÀ NỘI & TP.HCM</span>
                    <div class="pricing-header-block" style="text-align: center; border-bottom: 1px solid #EAEFE9; padding-bottom: 24px; margin-bottom: 24px;">
                        <h3 class="pricing-title" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 700 !important; font-size: 0.95rem !important; text-transform: uppercase !important; color: #1B382B !important; letter-spacing: 0.5px !important; line-height: 1.35 !important; margin-bottom: 12px !important; text-align: center !important;">THÀNH PHỐ TRỰC THUỘC<br>TRUNG ƯƠNG</h3>
                        <div class="pricing-fee" style="margin: 10px 0 4px 0 !important; text-align: center !important; display: block !important;">
                            <span class="pricing-amount" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #C59B27 !important; line-height: 1.2 !important; display: block !important; text-align: center !important; font-variant-numeric: normal !important; letter-spacing: -0.02em !important;">350.000.000đ</span>
                            <span class="pricing-period" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 0.85rem !important; font-weight: 500 !important; color: #8C9A8E !important; display: block !important; text-align: center !important; margin-top: 2px !important;">/ 5 năm</span>
                        </div>
                    </div>"""

card2_new = """                    <div class="pricing-header-block" style="text-align: center; border-bottom: 1px solid #EAEFE9; padding-bottom: 24px; margin-bottom: 24px;">
                        <h3 class="pricing-title" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 700 !important; font-size: 0.95rem !important; text-transform: uppercase !important; color: #1B382B !important; letter-spacing: 0.5px !important; line-height: 1.35 !important; margin-bottom: 12px !important; text-align: center !important;">KĐT VÙNG VEN &amp;<br>CÁC TỈNH</h3>
                        <div class="pricing-fee" style="margin: 10px 0 4px 0 !important; text-align: center !important; display: block !important;">
                            <span class="pricing-amount" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #C59B27 !important; line-height: 1.2 !important; display: block !important; text-align: center !important; font-variant-numeric: normal !important; letter-spacing: -0.02em !important;">300.000.000đ</span>
                            <span class="pricing-period" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 0.85rem !important; font-weight: 500 !important; color: #8C9A8E !important; display: block !important; text-align: center !important; margin-top: 2px !important;">/ 5 năm</span>
                        </div>
                    </div>"""

fran = re.sub(
    r'<span class="pricing-badge">ƯU TIÊN HÀ NỘI & TP\.HCM</span>[\s\S]*?<div class="pricing-header-block"[^>]*>[\s\S]*?</div>\s*</div>',
    card1_new,
    fran
)

fran = re.sub(
    r'<div class="pricing-card">\s*<div class="pricing-header-block"[^>]*>[\s\S]*?</div>\s*</div>',
    '<div class="pricing-card">\n' + card2_new,
    fran
)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

print('Applied emergency fix for pricing fee size and title wrapping successfully.')
