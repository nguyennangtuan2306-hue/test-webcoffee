# scratch/update_header_btn.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

btn_css = """
/* Header Franchise CTA Button with Smooth Hover & Active Effects */
.btn-header-franchise {
    background: linear-gradient(135deg, #E0A96D, #C89D66) !important;
    color: #ffffff !important;
    padding: 8px 18px !important;
    border-radius: 9999px !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    font-size: 11px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    box-shadow: 0 4px 12px rgba(200, 157, 102, 0.35) !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    cursor: pointer !important;
}

.btn-header-franchise .btn-icon-hand {
    display: inline-block;
    font-size: 14px;
    transition: transform 0.3s ease-in-out;
}

.btn-header-franchise:hover {
    background: linear-gradient(135deg, #E8B478, #D6AA6F) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(200, 157, 102, 0.55), 0 0 15px rgba(214, 170, 111, 0.4) !important;
    border-color: rgba(255, 255, 255, 0.6) !important;
}

.btn-header-franchise:hover .btn-icon-hand {
    transform: scale(1.22) rotate(-5deg);
}

.btn-header-franchise:active {
    transform: translateY(0) scale(0.95) !important;
    box-shadow: 0 2px 8px rgba(200, 157, 102, 0.35) !important;
}
"""

if '.btn-header-franchise' in css:
    css = re.sub(r'/\* Header Franchise CTA Button[\s\S]*?\.btn-header-franchise:active\s*\{[^}]*\}', btn_css.strip(), css)
else:
    css += '\n' + btn_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update HTML files
html_files = ['index.html', 'about.html', 'menu.html', 'franchise.html', 'contact.html']

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header CTA button block
    pattern = r'<div class="header-cta">\s*<a href="[^"]*"[^>]*>[\s\S]*?NHƯỢNG QUYỀN[\s\S]*?</a>\s*</div>'
    replacement = '''<div class="header-cta">
                <a href="franchise.html" class="btn-header-franchise">
                    <span class="btn-icon-hand">🤝</span>
                    <span>NHƯỢNG QUYỀN</span>
                </a>
            </div>'''
    content = re.sub(pattern, replacement, content)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Updated header button in {fname}')

print('All 5 HTML files and style.css updated successfully.')
