# scratch/apply_exact_user_hero_quicksand.py
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add font and style to <head>
head_tag = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HEAVEN - Trà Ngon Biết Nói | Thức Uống Bản Sắc Vùng Miền</title>
    <!-- Quicksand Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
      * { font-family: 'Quicksand', sans-serif !important; }
    </style>"""

html = re.sub(r'<head>[\s\S]*?<title>[^<]*</title>', head_tag, html)

# 2. Update slide 1, 2, 3 in index.html
slide1 = """                    <div class="hero-content" style="position: relative; z-index: 20; text-align: center; max-width: 1080px; width: 100%; padding: 0 24px; margin-top: 40px;">
                        <h1 style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem; font-weight: 700; color: #ffffff; text-shadow: 0 2px 10px rgba(0,0,0,0.7); margin-bottom: 12px; text-align: center;">HEAVEN COFFEE &amp; TEA</h1>
                        <p style="font-family: 'Quicksand', sans-serif !important; font-size: 1.1rem; color: #f0f0f0; text-shadow: 0 1px 6px rgba(0,0,0,0.7); margin-bottom: 24px; text-align: center;">Trà ngon biết nói - Bản sắc hương vị Việt</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">"""

slide2 = """                    <div class="hero-content" style="position: relative; z-index: 20; text-align: center; max-width: 1080px; width: 100%; padding: 0 24px; margin-top: 40px;">
                        <h1 style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem; font-weight: 700; color: #ffffff; text-shadow: 0 2px 10px rgba(0,0,0,0.7); margin-bottom: 12px; text-align: center;">KHÔNG GIAN ZEN &amp; MỘC</h1>
                        <p style="font-family: 'Quicksand', sans-serif !important; font-size: 1.1rem; color: #f0f0f0; text-shadow: 0 1px 6px rgba(0,0,0,0.7); margin-bottom: 24px; text-align: center;">Mặt bằng căn góc 150m² thoáng đãng bên hồ cá Koi</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">"""

slide3 = """                    <div class="hero-content" style="position: relative; z-index: 20; text-align: center; max-width: 1080px; width: 100%; padding: 0 24px; margin-top: 40px;">
                        <h1 style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem; font-weight: 700; color: #ffffff; text-shadow: 0 2px 10px rgba(0,0,0,0.7); margin-bottom: 12px; text-align: center;">CHUYÊN NGHIỆP &amp; TẬN TÂM</h1>
                        <p style="font-family: 'Quicksand', sans-serif !important; font-size: 1.1rem; color: #f0f0f0; text-shadow: 0 1px 6px rgba(0,0,0,0.7); margin-bottom: 24px; text-align: center;">Công nghệ hiện đại &amp; bí quyết độc quyền cùng chuỗi 6 chi nhánh</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">"""

html = re.sub(
    r'<div class="hero-content"[\s\S]*?<div class="hero-actions"[^>]*>',
    slide1,
    html,
    count=1
)

html = re.sub(
    r'<div class="hero-content"[\s\S]*?KHÔNG GIAN ZEN &amp; MỘC[\s\S]*?<div class="hero-actions"[^>]*>',
    slide2,
    html
)

html = re.sub(
    r'<div class="hero-content"[\s\S]*?CHUYÊN NGHIỆP &amp; TẬN TÂM[\s\S]*?<div class="hero-actions"[^>]*>',
    slide3,
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html with exact requested markup and Quicksand head style.')
