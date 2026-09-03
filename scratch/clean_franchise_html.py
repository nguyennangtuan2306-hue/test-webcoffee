# scratch/clean_franchise_html.py
import re

with open('franchise.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Clean inline styles on h3 and h4 inside benefit-card and process-10-card
c = re.sub(r'<h3 style="[^"]*">', '<h3>', c)
c = re.sub(r'<h4 style="[^"]*">', '<h4>', c)
c = re.sub(r'<span class="process-10-num"[^>]*>', '<span class="process-10-num">', c)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Cleaned inline styles on franchise.html successfully.')
