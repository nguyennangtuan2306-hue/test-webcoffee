# scratch/apply_pricing_premium_ui.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

pricing_premium_css = """
/* ==========================================================================
   Premium Pricing Cards Styling
   ========================================================================== */
.pricing-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
    max-width: 950px;
    margin: 0 auto;
    align-items: stretch;
}

.pricing-card {
    background: #FFFFFF;
    border: 1px solid rgba(212, 163, 115, 0.35);
    border-radius: 20px;
    padding: 40px 32px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
    transition: var(--transition-smooth);
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.pricing-card.featured {
    border: 2px solid #1B382B !important;
    border-radius: 20px;
    background: linear-gradient(180deg, #FFFFFF 0%, #F5F9F6 100%);
    box-shadow: 0 16px 45px rgba(27, 56, 43, 0.14) !important;
}

.pricing-badge {
    position: absolute;
    top: -14px;
    right: 30px;
    background: #1B382B;
    color: var(--color-gold);
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    padding: 5px 16px;
    border-radius: 20px;
    border: 1px solid var(--color-gold);
    box-shadow: 0 4px 12px rgba(27, 56, 43, 0.2);
}

.pricing-header-block {
    text-align: center;
    border-bottom: 1px solid #EAEFE9;
    padding-bottom: 24px;
    margin-bottom: 24px;
}

.pricing-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    color: #1B382B !important;
    letter-spacing: 1.5px !important;
    margin-bottom: 14px !important;
    text-align: center !important;
}

.pricing-fee {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    color: #C0904D !important;
    font-variant-numeric: normal !important;
    letter-spacing: -0.025em !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    line-height: 1.1 !important;
    gap: 6px !important;
    text-align: center !important;
}

.pricing-fee .pricing-period {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    color: #8C9A8E !important;
    letter-spacing: 0.5px !important;
}

.pricing-features-list {
    list-style: none;
    margin-bottom: 30px;
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.pricing-features-list li {
    font-size: 0.92rem;
    color: var(--color-text-dark);
    display: flex;
    align-items: flex-start;
    gap: 12px;
    line-height: 1.5;
}

.pricing-features-list li i {
    color: #1B382B !important;
    font-size: 1rem;
    margin-top: 3px;
    flex-shrink: 0;
}
"""

if 'Premium Pricing Cards Styling' in css:
    css = re.sub(r'/\* ==========================================================================\s*Premium Pricing Cards Styling[\s\S]*?flex-shrink: 0;\s*\}', pricing_premium_css.strip(), css)
else:
    css += '\n' + pricing_premium_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update franchise.html
with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

card1_html = """                    <span class="pricing-badge">ƯU TIÊN HÀ NỘI & TP.HCM</span>
                    <div class="pricing-header-block" style="text-align: center; border-bottom: 1px solid #EAEFE9; padding-bottom: 24px; margin-bottom: 24px;">
                        <h3 class="pricing-title" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 700 !important; font-size: 1.05rem !important; text-transform: uppercase !important; color: #1B382B !important; letter-spacing: 1.5px !important; margin-bottom: 14px !important; text-align: center !important;">Thành Phố Trực Thuộc Trung Ương</h3>
                        <div class="pricing-fee" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #C0904D !important; font-variant-numeric: normal !important; letter-spacing: -0.025em !important; display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; line-height: 1.1 !important; gap: 6px !important; text-align: center !important;">
                            <span>350.000.000đ</span>
                            <span class="pricing-period" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 500 !important; font-size: 0.85rem !important; color: #8C9A8E !important; letter-spacing: 0.5px !important;">/ 5 năm</span>
                        </div>
                    </div>"""

card2_html = """                    <div class="pricing-header-block" style="text-align: center; border-bottom: 1px solid #EAEFE9; padding-bottom: 24px; margin-bottom: 24px;">
                        <h3 class="pricing-title" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 700 !important; font-size: 1.05rem !important; text-transform: uppercase !important; color: #1B382B !important; letter-spacing: 1.5px !important; margin-bottom: 14px !important; text-align: center !important;">KĐT Vùng Ven & Các Tỉnh</h3>
                        <div class="pricing-fee" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #C0904D !important; font-variant-numeric: normal !important; letter-spacing: -0.025em !important; display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; line-height: 1.1 !important; gap: 6px !important; text-align: center !important;">
                            <span>300.000.000đ</span>
                            <span class="pricing-period" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 500 !important; font-size: 0.85rem !important; color: #8C9A8E !important; letter-spacing: 0.5px !important;">/ 5 năm</span>
                        </div>
                    </div>"""

fran = re.sub(
    r'<span class="pricing-badge">ƯU TIÊN HÀ NỘI & TP\.HCM</span>[\s\S]*?<div class="pricing-header-block"[^>]*>[\s\S]*?</div>\s*</div>',
    card1_html,
    fran
)

fran = re.sub(
    r'<div class="pricing-card">\s*<div class="pricing-header-block"[^>]*>[\s\S]*?</div>\s*</div>',
    '<div class="pricing-card">\n' + card2_html,
    fran
)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

print('Applied premium pricing cards styling successfully.')
