# scratch/fix_fontawesome_and_quicksand_sync.py
import re

html_files = ['index.html', 'about.html', 'menu.html', 'franchise.html', 'contact.html']

fa_cdn = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'
quicksand_link = '<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">'

head_style = """    <!-- FontAwesome & Quicksand Font -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
      *, html, body, h1, h2, h3, h4, h5, h6, p, a, button, input, select, textarea, label {
        font-family: 'Quicksand', sans-serif !important;
      }
      .fa, .fa-solid, .fa-regular, .fa-brands, .fa-duotone, i[class*="fa-"], span[class*="fa-"] {
        font-family: "Font Awesome 6 Free", "Font Awesome 6 Brands", "FontAwesome" !important;
      }
      .fa-brands, i.fa-brands {
        font-family: "Font Awesome 6 Brands" !important;
      }
    </style>"""

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean old inline serif fonts
    content = re.sub(r"font-family:\s*'?(Cormorant Garamond|Playfair Display|Times New Roman)'?[^;\"']*;", "font-family: 'Quicksand', sans-serif !important;", content, flags=re.IGNORECASE)

    # Ensure FontAwesome is in head
    if 'font-awesome/6.5.1/css/all.min.css' not in content:
        content = content.replace('</head>', f'    {fa_cdn}\n</head>')

    # Replace head font tags with clean sync
    if '<style>' in content and 'Quicksand' in content:
        content = re.sub(r'<!-- Quicksand Google Font -->[\s\S]*?</style>', head_style.strip(), content)
    else:
        content = content.replace('</head>', f'{head_style}\n</head>')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

# Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace all serif fonts in style.css
css = re.sub(r"'Cormorant Garamond',\s*serif", "'Quicksand', sans-serif", css)
css = re.sub(r"'Playfair Display',\s*serif", "'Quicksand', sans-serif", css)
css = re.sub(r"'Times New Roman',\s*serif", "'Quicksand', sans-serif", css)

# Top of style.css rule
top_css_rule = """/* ==========================================================================
   GLOBAL QUICKSAND & FONTAWESOME ICON PRESERVATION
   ========================================================================== */
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');

*, html, body, h1, h2, h3, h4, h5, h6, p, a, button, input, select, textarea, label {
    font-family: 'Quicksand', sans-serif !important;
}

/* Explicitly preserve FontAwesome icons from being overridden by Quicksand */
.fa, .fa-solid, .fa-regular, .fa-brands, .fa-duotone, .fa-thin, .fa-light, 
i[class*="fa-"], span[class*="fa-"], i.fa-solid, i.fa-brands, i.fa-regular {
    font-family: "Font Awesome 6 Free", "Font Awesome 6 Brands", "FontAwesome" !important;
    font-weight: 900 !important;
    font-style: normal !important;
}

.fa-brands, i.fa-brands {
    font-family: "Font Awesome 6 Brands" !important;
    font-weight: 400 !important;
}
"""

if 'GLOBAL QUICKSAND & FONTAWESOME ICON PRESERVATION' in css:
    css = re.sub(r'/\* ==========================================================================\s*GLOBAL QUICKSAND & FONTAWESOME ICON PRESERVATION[\s\S]*?font-weight: 400 !important;\s*\}', top_css_rule.strip(), css)
else:
    css = top_css_rule + '\n' + css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Synchronized FontAwesome and Quicksand typography across all pages and style.css')
