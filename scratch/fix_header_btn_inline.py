# scratch/fix_header_btn_inline.py
import re

html_files = ['index.html', 'about.html', 'menu.html', 'franchise.html', 'contact.html']

target_btn_html = '''<div class="header-cta">
                <a href="franchise.html" style="display: inline-flex !important; align-items: center !important; gap: 6px !important; background-color: #C89D66 !important; color: #FFFFFF !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; text-transform: uppercase !important; letter-spacing: 0.05em !important; padding: 8px 18px !important; border-radius: 9999px !important; text-decoration: none !important; box-shadow: 0 2px 6px rgba(0,0,0,0.15) !important;">
                    <span>🤝</span>
                    <span>NHƯỢNG QUYỀN</span>
                </a>
            </div>'''

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<div class="header-cta">[\s\S]*?NHƯỢNG QUYỀN[\s\S]*?</div>'
    content = re.sub(pattern, target_btn_html, content)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Updated {fname}')

print('All 5 HTML files updated with inline fixed gold button.')
