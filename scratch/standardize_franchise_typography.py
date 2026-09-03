# scratch/standardize_franchise_typography.py
import re
import unicodedata

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

franchise_typo_css = """
/* ==========================================================================
   Standardized Franchise Page Typography
   ========================================================================== */

/* 1. Tiêu đề chính h1, h2, section main title */
.franchise-benefits-section h2,
.franchise-pricing-section h2,
.franchise-process-section h2,
.page-header-title,
.section-main-title,
.reservation-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
}

/* 2. Tiêu đề 8 thẻ đặc quyền & Tiêu đề các bước triển khai */
.benefit-card h3 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 700 !important;
    font-size: 1.25rem !important;
    color: #1E3932 !important;
    letter-spacing: 0.2px !important;
    margin-bottom: 10px !important;
}

.process-10-card h4 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 700 !important;
    font-size: 1.12rem !important;
    color: #1E3932 !important;
    letter-spacing: 0.2px !important;
    margin-bottom: 6px !important;
    line-height: 1.35 !important;
}

.pricing-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 700 !important;
    font-size: 1.4rem !important;
    color: #1E3932 !important;
}

/* 3. Toàn bộ mô tả, gói chi phí, bảng dự toán và con số: Plus Jakarta Sans */
.benefit-card p,
.process-10-card p,
.section-sub-desc,
.section-tag,
.cost-estimate-card,
.cost-table,
.cost-table th,
.cost-table td,
.pricing-features-list,
.pricing-features-list li,
.pricing-badge,
.franchise-benefits-section p,
.franchise-pricing-section p,
.franchise-process-section p,
.reservation-card p,
.reservation-card label,
.reservation-card input,
.reservation-card select,
.reservation-card textarea,
.reservation-card button {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

.pricing-fee {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    color: #C89D66 !important;
    font-variant-numeric: normal !important;
    letter-spacing: -0.02em !important;
    display: flex !important;
    align-items: baseline !important;
    gap: 6px !important;
}

.pricing-fee span {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    color: #6B7280 !important;
}

.process-10-num {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    color: #C89D66 !important;
    font-variant-numeric: normal !important;
}
"""

if 'Standardized Franchise Page Typography' in css:
    css = re.sub(r'/\* ==========================================================================\s*Standardized Franchise Page Typography[\s\S]*?font-variant-numeric: normal !important;\s*\}', franchise_typo_css.strip(), css)
else:
    css += '\n' + franchise_typo_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update franchise.html: clean inline font styles and keep clean semantic markup
with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

fran = unicodedata.normalize('NFC', fran)

# Clean inline font-family in franchise.html
def clean_style(m):
    s = m.group(1)
    s = re.sub(r'font-family\s*:\s*[^;"]+;?', '', s)
    s = re.sub(r';\s*;', ';', s).strip(' ;')
    if not s:
        return ''
    return f'style="{s}"'

fran = re.sub(r'style="([^"]*font-family[^"]*)"', clean_style, fran)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

print('Updated Franchise typography in style.css and franchise.html successfully.')
