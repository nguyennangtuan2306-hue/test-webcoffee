# scratch/restore_typography.py
import re
import os

html_files = ['index.html', 'about.html', 'menu.html', 'franchise.html', 'contact.html']

google_font_block = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Cormorant+Garamond:ital,wght@0,600;0,700;1,500;1,600&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'''

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Google Fonts link
    content = re.sub(
        r'<link rel="preconnect" href="https://fonts.googleapis.com">[\s\S]*?<link href="https://fonts.googleapis.com/css2\?[^"]+" rel="stylesheet">',
        google_font_block.strip(),
        content
    )

    # 2. Clean inline font-family
    def clean_style(match):
        style_content = match.group(1)
        cleaned = re.sub(r'font-family\s*:\s*[^;"]+;?', '', style_content)
        cleaned = re.sub(r';\s*;', ';', cleaned).strip(' ;')
        if not cleaned:
            return ''
        return f'style="{cleaned}"'

    content = re.sub(r'style="([^"]*font-family[^"]*)"', clean_style, content)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Processed {fname}')

print('All HTML files updated.')
