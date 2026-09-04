# scratch/replace_all_fonts_with_quicksand.py
import re

html_files = ['index.html', 'about.html', 'menu.html', 'franchise.html', 'contact.html']

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all font-family declarations in inline styles
    content = re.sub(
        r"font-family\s*:\s*[^;\"]+;?",
        "font-family: 'Quicksand', sans-serif !important;",
        content
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

# Process style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace any font-family declaration in style.css except FontAwesome
fonts_to_replace = [
    'Montserrat', 'Playfair Display', 'Cormorant Garamond', 
    'Plus Jakarta Sans', 'Be Vietnam Pro', 'sans-serif', 'serif'
]

css = re.sub(r"--font-heading:\s*[^;]+;", "--font-heading: 'Quicksand', sans-serif !important;", css)
css = re.sub(r"--font-body:\s*[^;]+;", "--font-body: 'Quicksand', sans-serif !important;", css)
css = re.sub(r"--font-display:\s*[^;]+;", "--font-display: 'Quicksand', sans-serif !important;", css)
css = re.sub(r"--font-soft:\s*[^;]+;", "--font-soft: 'Quicksand', sans-serif !important;", css)

# Make sure global Quicksand rule is at top and bottom
quicksand_enforcement = """
/* ==========================================================================
   FORCE 100% QUICKSAND FONT EVERYWHERE
   ========================================================================== */
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i:not([class*="fa"]), center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video, button, input, textarea, select {
    font-family: 'Quicksand', sans-serif !important;
}

/* Keep FontAwesome icons */
.fa, .fa-solid, .fa-regular, .fa-brands, .fa-duotone, .fa-thin, .fa-light, 
i[class*="fa-"], span[class*="fa-"] {
    font-family: "Font Awesome 6 Free", "Font Awesome 6 Brands", "FontAwesome" !important;
    font-weight: 900 !important;
    font-style: normal !important;
}

.fa-brands, i.fa-brands {
    font-family: "Font Awesome 6 Brands" !important;
    font-weight: 400 !important;
}
"""

if 'FORCE 100% QUICKSAND FONT EVERYWHERE' in css:
    css = re.sub(r'/\* ==========================================================================\s*FORCE 100% QUICKSAND FONT EVERYWHERE[\s\S]*?font-weight: 400 !important;\s*\}', quicksand_enforcement.strip(), css)
else:
    css = quicksand_enforcement + '\n' + css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Replaced all font occurrences with Quicksand successfully.')
