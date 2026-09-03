# scratch/apply_menu_fonts.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

menu_typography_css = """
/* ==========================================================================
   Menu Cards Typography (Dish Title, Description, Price)
   ========================================================================== */

/* Tiêu đề tên món nước: Cormorant Garamond đậm */
.dish-name,
.catalog-dish-name,
.menu-card h4,
.menu-card h3,
.catalog-item-card h3,
.catalog-item-card h4 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 700 !important;
    font-size: 1.18rem !important;
    color: #1E2822 !important;
    letter-spacing: 0.2px !important;
}

/* Phần mô tả món: Plus Jakarta Sans */
.dish-desc,
.catalog-dish-desc,
.menu-card p,
.catalog-item-card p {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.82rem !important;
    color: #5C6961 !important;
    font-weight: 400 !important;
    line-height: 1.55 !important;
}

/* Phần giá tiền: Plus Jakarta Sans */
.dish-price,
.catalog-price,
.price,
[class*="price"],
.text-price {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    color: #C89D66 !important;
    font-variant-numeric: normal !important;
    letter-spacing: -0.02em !important;
    display: inline-flex !important;
    align-items: baseline !important;
}
"""

if 'Menu Cards Typography (Dish Title, Description, Price)' in css:
    css = re.sub(
        r'/\* ==========================================================================\s*Menu Cards Typography[\s\S]*?align-items: baseline !important;\s*\}',
        menu_typography_css.strip(),
        css
    )
else:
    css += '\n' + menu_typography_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html and menu.html to standardize price inline styles to Plus Jakarta Sans
for fname in ['index.html', 'menu.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update inline styles for dish-price and catalog-price
    html = re.sub(
        r'class="dish-price"[^>]*>',
        'class="dish-price" style="font-family: \'Plus Jakarta Sans\', sans-serif !important; font-weight: 700 !important; color: #C89D66 !important; font-variant-numeric: normal !important;">',
        html
    )
    html = re.sub(
        r'class="catalog-price"[^>]*>',
        'class="catalog-price" style="font-family: \'Plus Jakarta Sans\', sans-serif !important; font-weight: 700 !important; color: #C89D66 !important; font-variant-numeric: normal !important;">',
        html
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

print('Updated menu card typography in style.css, index.html, and menu.html')
