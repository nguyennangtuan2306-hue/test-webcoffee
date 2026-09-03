# scratch/apply_all_fixes.py
import re
import unicodedata

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .benefit-card h3 in style.css
benefit_css = """.benefit-card h3 {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    color: #1E3932 !important;
    font-size: 17px !important;
    letter-spacing: -0.01em !important;
    margin-bottom: 10px;
}"""

css = re.sub(r'\.benefit-card h3\s*\{[^}]*\}', benefit_css, css)

# Update .branch-title in style.css
branch_css = """.branch-title {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 700 !important;
    color: #1E3932 !important;
    letter-spacing: 0.02em !important;
}"""

css = re.sub(r'\.branch-title\s*\{[^}]*\}', branch_css, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update franchise.html
with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

# Normalize NFC
fran = unicodedata.normalize('NFC', fran)

# Update the 8 benefit headings with inline style as requested
benefit_titles = [
    'Khai Thác Thương Hiệu',
    'Setup Chuẩn Vận Hành',
    'Giảm Thiểu Rủi Ro',
    'Món Mới Định Kỳ',
    'Marketing Thương Hiệu',
    'Nguồn Cung Ổn Định',
    'Quản Trị Chất Lượng',
    'Đồng Hành Phát Triển'
]

for title in benefit_titles:
    norm_title = unicodedata.normalize('NFC', title)
    pattern = rf'<h3[^>]*>\s*{re.escape(norm_title)}\s*</h3>'
    replacement = f'<h3 style="font-family: \'Montserrat\', sans-serif !important; font-weight: 700 !important; color: #1E3932 !important; font-size: 17px !important; letter-spacing: -0.01em !important;">{norm_title}</h3>'
    fran = re.sub(pattern, replacement, fran)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

# 3. Update contact.html & index.html for Roman numerals and subtitles
def update_branches(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = unicodedata.normalize('NFC', content)
    
    roman_map = [
        ('Cơ sở 1 (Trụ sở chính)', 'Cơ sở I (Trụ sở chính)'),
        ('Cơ sở 1', 'Cơ sở I (Trụ sở chính)'),
        ('Cơ sở 2', 'Cơ sở II'),
        ('Cơ sở 3', 'Cơ sở III'),
        ('Cơ sở 4', 'Cơ sở IV'),
        ('Cơ sở 5', 'Cơ sở V'),
        ('Cơ sở 6', 'Cơ sở VI'),
    ]
    
    for old_t, new_t in roman_map:
        norm_old = unicodedata.normalize('NFC', old_t)
        norm_new = unicodedata.normalize('NFC', new_t)
        pattern = rf'<h3 class="branch-title"[^>]*>\s*{re.escape(norm_old)}\s*</h3>'
        replacement = f'<h3 class="branch-title" style="font-family: \'Montserrat\', sans-serif !important; font-weight: 700 !important; color: #1E3932 !important; letter-spacing: 0.02em !important;">{norm_new}</h3>'
        content = re.sub(pattern, replacement, content)
        # Also try matching without class attribute or with other inline styles
        pattern2 = rf'<h3[^>]*>\s*{re.escape(norm_old)}\s*</h3>'
        content = re.sub(pattern2, replacement, content)
    
    # Subtitle for headquarters
    sub_old = r'<span[^>]*>TRUNG TÂM VẬN HÀNH & ĐÀO TẠO</span>'
    sub_new = '<span style="font-family: \'Montserrat\', sans-serif !important; font-weight: 600 !important; font-size: 11px !important; letter-spacing: 0.05em !important; color: var(--color-sand-gold); display: block;">TRUNG TÂM VẬN HÀNH & ĐÀO TẠO</span>'
    content = re.sub(sub_old, sub_new, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_branches('contact.html')
update_branches('index.html')

print('Applied all requested typography changes successfully.')
