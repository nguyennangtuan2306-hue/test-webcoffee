# scratch/replace_roman_branches.py
import re

files = ['index.html', 'about.html', 'menu.html', 'franchise.html', 'contact.html']

replacements = [
    (r'Cơ\s*[sS]ở\s*VI\b', 'Cơ sở 6'),
    (r'Cơ\s*[sS]ở\s*IV\b', 'Cơ sở 4'),
    (r'Cơ\s*[sS]ở\s*V\b', 'Cơ sở 5'),
    (r'Cơ\s*[sS]ở\s*III\b', 'Cơ sở 3'),
    (r'Cơ\s*[sS]ở\s*II\b', 'Cơ sở 2'),
    (r'Cơ\s*[sS]ở\s*I\b', 'Cơ sở 1'),
    (r'CƠ\s*SỞ\s*VI\b', 'CƠ SỞ 6'),
    (r'CƠ\s*SỞ\s*IV\b', 'CƠ SỞ 4'),
    (r'CƠ\s*SỞ\s*V\b', 'CƠ SỞ 5'),
    (r'CƠ\s*SỞ\s*III\b', 'CƠ SỞ 3'),
    (r'CƠ\s*SỞ\s*II\b', 'CƠ SỞ 2'),
    (r'CƠ\s*SỞ\s*I\b', 'CƠ SỞ 1'),
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    for pattern, repl in replacements:
        if re.search(pattern, content):
            content = re.sub(pattern, repl, content)
            modified = True

    if modified:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {fname}')
    else:
        print(f'No changes in {fname}')

print('All branch numbers converted to Arabic numerals (1, 2, 3, 4, 5, 6).')
