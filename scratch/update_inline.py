# update_inline.py
with open('index.html', 'r', encoding='utf-8') as f:
    c_index = f.read()

c_index = c_index.replace(
    '<h2 class="menu-title">THỰC ĐƠN ĐẶC SẮC</h2>',
    '<h2 class="menu-title" style="font-family: Arial, Helvetica, sans-serif !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 2px !important; text-align: center !important; color: #2B1810 !important;">THỰC ĐƠN ĐẶC SẮC</h2>'
)

c_index = c_index.replace(
    '<span class="dish-price">',
    '<span class="dish-price" style="font-family: Arial, Helvetica, sans-serif !important; font-weight: 700 !important; color: #C89D66 !important; font-size: 16px !important; font-variant-numeric: normal !important;">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c_index)

with open('menu.html', 'r', encoding='utf-8') as f:
    c_menu = f.read()

c_menu = c_menu.replace(
    '<h1 class="page-header-title">THỰC ĐƠN ĐẶC SẮC</h1>',
    '<h1 class="page-header-title" style="font-family: Arial, Helvetica, sans-serif !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 2px !important; text-align: center !important; color: #ffffff !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important;">THỰC ĐƠN ĐẶC SẮC</h1>'
)

c_menu = c_menu.replace(
    '<span class="catalog-price">',
    '<span class="catalog-price" style="font-family: Arial, Helvetica, sans-serif !important; font-weight: 700 !important; color: #C89D66 !important; font-size: 16px !important; font-variant-numeric: normal !important;">'
)

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(c_menu)

print('Updated index.html and menu.html successfully.')
