# scratch/restore_all_3_slides.py
import re

slides_wrapper_html = """            <div class="swiper-wrapper">
                <!-- Slide 1: Khung cảnh góc phố 150m2 K-Town -->
                <div class="swiper-slide">
                    <div class="slide-bg" style="background-image: url('assets/image20.png');"></div>
                    <div class="hero-overlay"></div>
                    <div class="hero-content" style="position: relative; z-index: 20; text-align: center; max-width: 1080px; width: 100%; padding: 0 24px; margin-top: 40px;">
                        <h1 style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem; font-weight: 700; color: #ffffff; text-shadow: 0 2px 10px rgba(0,0,0,0.7); margin-bottom: 12px; text-align: center;">HEAVEN COFFEE &amp; TEA</h1>
                        <p style="font-family: 'Quicksand', sans-serif !important; font-size: 1.1rem; color: #f0f0f0; text-shadow: 0 1px 6px rgba(0,0,0,0.7); margin-bottom: 24px; text-align: center;">Trà ngon biết nói - Bản sắc hương vị Việt</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">
                            <a href="menu.html" class="btn-hero-primary" style="display: inline-flex !important; align-items: center !important; justify-content: center !important; white-space: nowrap !important; padding: 12px 24px !important; border-radius: 9999px !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.05em !important; text-transform: uppercase !important; background-color: #C89D66 !important; color: #FFFFFF !important; border: 1.5px solid #D4A373 !important; text-decoration: none !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;">KHÁM PHÁ THỰC ĐƠN</a>
                            <a href="franchise.html" class="btn-hero-secondary" style="display: inline-flex !important; align-items: center !important; justify-content: center !important; white-space: nowrap !important; padding: 12px 24px !important; border-radius: 9999px !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.05em !important; text-transform: uppercase !important; background: rgba(24, 61, 43, 0.75) !important; color: #FFFFFF !important; border: 1.5px solid rgba(212, 163, 115, 0.7) !important; backdrop-filter: blur(6px) !important; text-decoration: none !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;">HỢP TÁC NHƯỢNG QUYỀN</a>
                        </div>
                    </div>
                </div>

                <!-- Slide 2: Không gian sân vườn & hồ cá Koi -->
                <div class="swiper-slide">
                    <div class="slide-bg" style="background-image: url('assets/image1.png');"></div>
                    <div class="hero-overlay"></div>
                    <div class="hero-content" style="position: relative; z-index: 20; text-align: center; max-width: 1080px; width: 100%; padding: 0 24px; margin-top: 40px;">
                        <h1 style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem; font-weight: 700; color: #ffffff; text-shadow: 0 2px 10px rgba(0,0,0,0.7); margin-bottom: 12px; text-align: center;">KHÔNG GIAN ZEN &amp; MỘC</h1>
                        <p style="font-family: 'Quicksand', sans-serif !important; font-size: 1.1rem; color: #f0f0f0; text-shadow: 0 1px 6px rgba(0,0,0,0.7); margin-bottom: 24px; text-align: center;">Mặt bằng căn góc 150m² thoáng đãng bên hồ cá Koi</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">
                            <a href="about.html" class="btn-hero-primary" style="display: inline-flex !important; align-items: center !important; justify-content: center !important; white-space: nowrap !important; padding: 12px 24px !important; border-radius: 9999px !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.05em !important; text-transform: uppercase !important; background-color: #C89D66 !important; color: #FFFFFF !important; border: 1.5px solid #D4A373 !important; text-decoration: none !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;">VỀ HEAVEN</a>
                            <a href="franchise.html" class="btn-hero-secondary" style="display: inline-flex !important; align-items: center !important; justify-content: center !important; white-space: nowrap !important; padding: 12px 24px !important; border-radius: 9999px !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.05em !important; text-transform: uppercase !important; background: rgba(24, 61, 43, 0.75) !important; color: #FFFFFF !important; border: 1.5px solid rgba(212, 163, 115, 0.7) !important; backdrop-filter: blur(6px) !important; text-decoration: none !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;">TƯ VẤN ĐẦU TƯ</a>
                        </div>
                    </div>
                </div>

                <!-- Slide 3: Quầy Bar & Nội thất gỗ sang trọng -->
                <div class="swiper-slide">
                    <div class="slide-bg" style="background-image: url('assets/image12.png');"></div>
                    <div class="hero-overlay"></div>
                    <div class="hero-content" style="position: relative; z-index: 20; text-align: center; max-width: 1080px; width: 100%; padding: 0 24px; margin-top: 40px;">
                        <h1 style="font-family: 'Quicksand', sans-serif !important; font-size: 2.8rem; font-weight: 700; color: #ffffff; text-shadow: 0 2px 10px rgba(0,0,0,0.7); margin-bottom: 12px; text-align: center;">CHUYÊN NGHIỆP &amp; TẬN TÂM</h1>
                        <p style="font-family: 'Quicksand', sans-serif !important; font-size: 1.1rem; color: #f0f0f0; text-shadow: 0 1px 6px rgba(0,0,0,0.7); margin-bottom: 24px; text-align: center;">Công nghệ hiện đại &amp; bí quyết độc quyền cùng chuỗi 6 chi nhánh</p>
                        <div class="hero-actions" style="display: flex !important; gap: 16px !important; justify-content: center !important; align-items: center !important; flex-wrap: wrap !important; margin-top: 24px !important; width: 100% !important;">
                            <a href="franchise.html" class="btn-hero-primary" style="display: inline-flex !important; align-items: center !important; justify-content: center !important; white-space: nowrap !important; padding: 12px 24px !important; border-radius: 9999px !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.05em !important; text-transform: uppercase !important; background-color: #C89D66 !important; color: #FFFFFF !important; border: 1.5px solid #D4A373 !important; text-decoration: none !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;">TƯ VẤN ĐẦU TƯ</a>
                            <a href="contact.html" class="btn-hero-secondary" style="display: inline-flex !important; align-items: center !important; justify-content: center !important; white-space: nowrap !important; padding: 12px 24px !important; border-radius: 9999px !important; font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.05em !important; text-transform: uppercase !important; background: rgba(24, 61, 43, 0.75) !important; color: #FFFFFF !important; border: 1.5px solid rgba(212, 163, 115, 0.7) !important; backdrop-filter: blur(6px) !important; text-decoration: none !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25) !important;">HỆ THỐNG CƠ SỞ</a>
                        </div>
                    </div>
                </div>
            </div>"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'<div class="swiper-wrapper">[\s\S]*?</div>\s*<!-- Navigation Buttons -->',
    slides_wrapper_html + '\n\n            <!-- Navigation Buttons -->',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('All 3 hero slides restored accurately.')
