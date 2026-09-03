# scratch/fix_playfair.py
import re

html_files = ['index.html', 'about.html', 'menu.html', 'franchise.html', 'contact.html']

google_font_block = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Montserrat:wght@400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,600;0,700;1,500;1,600&display=swap" rel="stylesheet">'''

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(
        r'<link rel="preconnect" href="https://fonts.googleapis.com">[\s\S]*?<link href="https://fonts.googleapis.com/css2\?[^"]+" rel="stylesheet">',
        google_font_block.strip(),
        content
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Updated font link in {fname}')

print('All HTML files updated with Playfair Display.')
