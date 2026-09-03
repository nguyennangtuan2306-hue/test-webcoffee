# scratch/apply_branch_and_price_fonts.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .branch-title in style.css
branch_css = '''
.branch-title {
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1.15rem;
    font-weight: 700 !important;
    color: #1E3932 !important;
    font-variant-numeric: normal !important;
}'''

css = re.sub(r'\.branch-title\s*\{[^}]*\}', branch_css.strip(), css)

# Update price in style.css
price_css = '''
.dish-price,
.catalog-price,
.price,
[class*="price"],
.text-price {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    color: #C89D66 !important;
    font-variant-numeric: normal !important;
    letter-spacing: -0.02em;
    display: inline-flex;
    align-items: baseline;
}'''

css = re.sub(r'\.dish-price,\s*\.catalog-price\s*\{[^}]*\}', price_css.strip(), css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c_index = f.read()

# Inline styles for branch-title in index.html
c_index = re.sub(
    r'<h3 class="branch-title">([^<]+)</h3>',
    r'<h3 class="branch-title" style="font-family: \'Montserrat\', sans-serif !important; font-weight: 700 !important; color: #1E3932 !important;">\1</h3>',
    c_index
)

# Inline styles for dish-price in index.html
c_index = re.sub(
    r'<span class="dish-price"[^>]*>([^<]+)</span>',
    r'<span class="dish-price" style="font-family: \'Montserrat\', sans-serif !important; font-weight: 700 !important; color: #C89D66 !important; font-variant-numeric: normal !important;">\1</span>',
    c_index
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c_index)

# 3. Update menu.html
with open('menu.html', 'r', encoding='utf-8') as f:
    c_menu = f.read()

# Inline styles for catalog-price in menu.html
c_menu = re.sub(
    r'<span class="catalog-price"[^>]*>([^<]+)</span>',
    r'<span class="catalog-price" style="font-family: \'Montserrat\', sans-serif !important; font-weight: 700 !important; color: #C89D66 !important; font-variant-numeric: normal !important;">\1</span>',
    c_menu
)

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(c_menu)

# 4. Update contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    c_contact = f.read()

c_contact = re.sub(
    r'<h3 class="branch-title">([^<]+)</h3>',
    r'<h3 class="branch-title" style="font-family: \'Montserrat\', sans-serif !important; font-weight: 700 !important; color: #1E3932 !important;">\1</h3>',
    c_contact
)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(c_contact)

print('Updated style.css, index.html, menu.html, and contact.html successfully.')
