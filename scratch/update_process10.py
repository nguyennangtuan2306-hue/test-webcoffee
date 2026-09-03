# scratch/update_process10.py
import re
import unicodedata

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

p_num_css = """.process-10-num {
    display: inline-block;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1.25rem;
    font-weight: 700 !important;
    color: #C89D66 !important;
    font-variant-numeric: normal !important;
    margin-bottom: 8px;
}"""

p_h4_css = """.process-10-card h4 {
    font-family: 'Montserrat', sans-serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    color: #1E3932 !important;
    letter-spacing: -0.01em !important;
    margin-bottom: 6px;
    line-height: 1.4;
}"""

css = re.sub(r'\.process-10-num\s*\{[^}]*\}', p_num_css, css)
css = re.sub(r'\.process-10-card h4\s*\{[^}]*\}', p_h4_css, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update franchise.html
with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

fran = unicodedata.normalize('NFC', fran)

step_titles = [
    'Thẩm định mặt bằng',
    'Thẩm định năng lực',
    'Đặt cọc hợp đồng',
    'Ký kết hợp đồng',
    'Thiết kế & Thi công',
    'Đào tạo chuyên sâu',
    'Kế hoạch Marketing',
    'Chạy thử nghiệm',
    'Khai trương hồng phát',
    'Đồng hành sau khai trương'
]

for title in step_titles:
    norm_t = unicodedata.normalize('NFC', title)
    pattern = rf'<h4[^>]*>\s*{re.escape(norm_t)}\s*</h4>'
    replacement = f'<h4 style="font-family: \'Montserrat\', sans-serif !important; font-weight: 700 !important; color: #1E3932 !important; font-size: 16px !important; letter-spacing: -0.01em !important;">{norm_t}</h4>'
    fran = re.sub(pattern, replacement, fran)

# Update step numbers inline
for num in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']:
    pattern = rf'<span class="process-10-num"[^>]*>{num}</span>'
    replacement = f'<span class="process-10-num" style="font-family: \'Montserrat\', sans-serif !important; font-weight: 700 !important; color: #C89D66 !important; font-variant-numeric: normal !important;">{num}</span>'
    fran = re.sub(pattern, replacement, fran)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

print('Updated 10-step process typography in style.css and franchise.html')
