# scratch/restore_index_hero_quicksand.py
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slide1_content = """                    <div class="hero-content">
                        <h1 class="hero-line-1" style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem !important; font-weight: 700 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; text-transform: uppercase !important; margin-bottom: 12px !important; text-align: center !important;">HEAVEN COFFEE &amp; TEA</h1>
                        <p class="hero-line-2" style="font-family: 'Quicksand', sans-serif !important; font-size: 1.5rem !important; font-weight: 600 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; margin-bottom: 12px !important; text-align: center !important;">Trà ngon biết nói - Bản sắc hương vị Việt</p>
                        <p class="hero-line-3" style="font-family: 'Quicksand', sans-serif !important; font-size: 1rem !important; font-weight: 500 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; max-width: 800px !important; margin: 0 auto 24px !important; text-align: center !important;">Từ đỉnh núi Shan Tuyết Hà Giang đến dừa non Bến Tre và cà phê mộc nắng gió Lâm Đồng.</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">"""

slide2_content = """                    <div class="hero-content">
                        <h1 class="hero-line-1" style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem !important; font-weight: 700 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; text-transform: uppercase !important; margin-bottom: 12px !important; text-align: center !important;">KHÔNG GIAN ZEN &amp; MỘC</h1>
                        <p class="hero-line-2" style="font-family: 'Quicksand', sans-serif !important; font-size: 1.5rem !important; font-weight: 600 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; margin-bottom: 12px !important; text-align: center !important;">Mặt bằng căn góc 150m² thoáng đãng</p>
                        <p class="hero-line-3" style="font-family: 'Quicksand', sans-serif !important; font-size: 1rem !important; font-weight: 500 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; max-width: 800px !important; margin: 0 auto 24px !important; text-align: center !important;">Thư thái bên hồ cá Koi, vườn cây xanh mát và kiến trúc mộc mạc ấm áp.</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">"""

slide3_content = """                    <div class="hero-content">
                        <h1 class="hero-line-1" style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem !important; font-weight: 700 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; text-transform: uppercase !important; margin-bottom: 12px !important; text-align: center !important;">CHUYÊN NGHIỆP &amp; TẬN TÂM</h1>
                        <p class="hero-line-2" style="font-family: 'Quicksand', sans-serif !important; font-size: 1.5rem !important; font-weight: 600 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; margin-bottom: 12px !important; text-align: center !important;">Công nghệ hiện đại &amp; bí quyết độc quyền</p>
                        <p class="hero-line-3" style="font-family: 'Quicksand', sans-serif !important; font-size: 1rem !important; font-weight: 500 !important; color: #FFFFFF !important; text-shadow: 0 2px 8px rgba(0,0,0,0.6) !important; max-width: 800px !important; margin: 0 auto 24px !important; text-align: center !important;">Chuẩn hóa vận hành, quản trị chất lượng cùng chuỗi 6 chi nhánh KĐT hàng đầu.</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">"""

html = re.sub(
    r'<div class="hero-content">\s*<h1 class="hero-line-1">[\s\S]*?TRÀ NGON BIẾT NÓI[\s\S]*?<div class="hero-actions"[^>]*>',
    slide1_content,
    html
)

html = re.sub(
    r'<div class="hero-content">\s*<h1 class="hero-line-1">[\s\S]*?KHÔNG GIAN ZEN & MỘC[\s\S]*?<div class="hero-actions"[^>]*>',
    slide2_content,
    html
)

html = re.sub(
    r'<div class="hero-content">\s*<h1 class="hero-line-1">[\s\S]*?CHUYÊN NGHIỆP & TẬN TÂM[\s\S]*?<div class="hero-actions"[^>]*>',
    slide3_content,
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

hero_quicksand_css = """
/* Hero Banner Quicksand Styles */
.hero-line-1 {
    font-family: 'Quicksand', sans-serif !important;
    font-size: clamp(1.8rem, 4vw, 3rem) !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
    text-transform: uppercase !important;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6) !important;
    margin-bottom: 12px !important;
    text-align: center !important;
    opacity: 1 !important;
    transform: none !important;
    display: block !important;
}

.hero-line-2 {
    font-family: 'Quicksand', sans-serif !important;
    font-size: clamp(1.2rem, 2.5vw, 1.6rem) !important;
    font-weight: 600 !important;
    color: #FFFFFF !important;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6) !important;
    margin-bottom: 12px !important;
    text-align: center !important;
    opacity: 1 !important;
    transform: none !important;
    display: block !important;
}

.hero-line-3 {
    font-family: 'Quicksand', sans-serif !important;
    font-size: clamp(0.9rem, 1.6vw, 1.05rem) !important;
    font-weight: 500 !important;
    color: #FFFFFF !important;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6) !important;
    max-width: 800px !important;
    margin: 0 auto 24px !important;
    text-align: center !important;
    opacity: 1 !important;
    transform: none !important;
    display: block !important;
}
"""

css = re.sub(r'/\* Hero Banner Quicksand Styles[\s\S]*?display: block !important;\s*\}', '', css)
css += '\n' + hero_quicksand_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated index.html hero banner titles with Quicksand and text shadow.')
