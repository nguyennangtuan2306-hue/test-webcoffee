# scratch/update_benefits.py
import unicodedata

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_h3 = """.benefit-card h3 {
    font-family: var(--font-serif);
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--color-text-dark);
    margin-bottom: 10px;
}"""

new_h3 = """.benefit-card h3 {
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1.12rem;
    font-weight: 700 !important;
    color: #1E3932 !important;
    letter-spacing: 0.02em !important;
    margin-bottom: 10px;
}"""

if old_h3 in css:
    css = css.replace(old_h3, new_h3)
else:
    import re
    css = re.sub(r'\.benefit-card h3\s*\{[^}]*\}', new_h3, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Normalize Unicode in franchise.html
with open('franchise.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = unicodedata.normalize('NFC', html)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated benefit card titles in style.css and normalized franchise.html')
