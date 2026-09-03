# scratch/apply_branch_styles.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add @import at top of style.css if not present
import_rule = "@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');\n"
if '@import url' not in css:
    css = import_rule + css
else:
    css = re.sub(r"@import url\([^)]+\);\n?", import_rule, css)

branch_css_block = """
/* ==========================================================================
   Branch Card Typography & Styling
   ========================================================================== */

/* 2. Tiêu đề các thẻ cơ sở (Cơ sở I, Cơ sở II, ...) */
.branch-card h3,
.branch-card .branch-title,
.branch-card h4,
.system-branch-card h3 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.35rem !important;
    font-weight: 700 !important;
    color: #1b382b !important;
    letter-spacing: 0.3px !important;
}

/* 3. Địa chỉ và số điện thoại chi tiết */
.branch-card p,
.branch-card .branch-address,
.branch-card .branch-phone,
.branch-card .branch-hotline,
.branch-card span:not(.branch-tag) {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.88rem !important;
    color: #4a5568 !important;
    line-height: 1.5;
}

/* 4. Các thẻ tag tiện ích (Hồ cá Koi, Đỗ ô tô, Căn góc...) */
.branch-card .branch-tag,
.branch-card .tag-item,
.branch-card .badge {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    background-color: #f2f5ed !important;
    color: #2d4a3e !important;
    border-radius: 6px !important;
    padding: 4px 10px !important;
}
"""

if 'Branch Card Typography & Styling' in css:
    css = re.sub(r'/\* ==========================================================================\s*Branch Card Typography & Styling[\s\S]*?border-radius: 6px !important;\s*padding: 4px 10px !important;\s*\}', branch_css_block.strip(), css)
else:
    css += '\n' + branch_css_block

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html and contact.html
for fname in ['index.html', 'contact.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean inline font styles on branch-title
    html = re.sub(r'<h3 class="branch-title"[^>]*>([^<]+)</h3>', r'<h3 class="branch-title">\1</h3>', html)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

print('Updated branch card typography in style.css, index.html, and contact.html')
