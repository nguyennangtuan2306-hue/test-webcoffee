# scratch/restore_both_pricing_cards.py
import re

pricing_grid_block = '''            <div class="pricing-grid">
                <!-- Gói 1: Thành phố Trung ương -->
                <div class="pricing-card featured">
                    <span class="pricing-badge">ƯU TIÊN HÀ NỘI & TP.HCM</span>
                    <div class="pricing-header-block" style="text-align: center; border-bottom: 1px solid #EAEFE9; padding-bottom: 24px; margin-bottom: 24px;">
                        <h3 class="pricing-title" style="font-family: 'Cormorant Garamond', serif !important; font-weight: 700 !important; font-size: 1.35rem !important; text-transform: none !important; color: #1B382B !important; letter-spacing: 0.2px !important; line-height: 1.3 !important; margin-bottom: 12px !important; text-align: center !important;">Thành Phố Trực Thuộc Trung Ương</h3>
                        <div class="pricing-fee" style="margin: 10px 0 4px 0 !important; text-align: center !important; display: block !important;">
                            <span class="pricing-amount" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #C59B27 !important; line-height: 1.2 !important; display: block !important; text-align: center !important; font-variant-numeric: normal !important; letter-spacing: -0.02em !important;">350.000.000đ</span>
                            <span class="pricing-period" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 0.85rem !important; font-weight: 500 !important; color: #8C9A8E !important; display: block !important; text-align: center !important; margin-top: 2px !important;">/ 5 năm</span>
                        </div>
                    </div>
                    <ul class="pricing-features-list">
                        <li><i class="fa-solid fa-check"></i> <strong>Khoảng cách bảo hộ độc quyền:</strong> Bán kính 3 km</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Phí duy trì thương hiệu:</strong> Năm đầu 8 tr/tháng, các năm sau 10 tr/tháng</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Đào tạo:</strong> 18 buổi tại văn phòng + 10 buổi tại điểm bán</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Hỗ trợ Marketing:</strong> Xây kênh truyền thông 1 tháng đầu</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Setup bàn giao:</strong> Bàn giao toàn bộ vận hành đạt chuẩn</li>
                    </ul>
                    <a href="#dang-ky" class="btn-hero-primary" style="display: block; text-align: center;">ĐĂNG KÝ GÓI TRUNG ƯƠNG</a>
                </div>

                <!-- Gói 2: KĐT Vùng Ven & Các Tỉnh -->
                <div class="pricing-card">
                    <div class="pricing-header-block" style="text-align: center; border-bottom: 1px solid #EAEFE9; padding-bottom: 24px; margin-bottom: 24px;">
                        <h3 class="pricing-title" style="font-family: 'Cormorant Garamond', serif !important; font-weight: 700 !important; font-size: 1.35rem !important; text-transform: none !important; color: #1B382B !important; letter-spacing: 0.2px !important; line-height: 1.3 !important; margin-bottom: 12px !important; text-align: center !important;">KĐT Vùng Ven &amp; Các Tỉnh</h3>
                        <div class="pricing-fee" style="margin: 10px 0 4px 0 !important; text-align: center !important; display: block !important;">
                            <span class="pricing-amount" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #C59B27 !important; line-height: 1.2 !important; display: block !important; text-align: center !important; font-variant-numeric: normal !important; letter-spacing: -0.02em !important;">300.000.000đ</span>
                            <span class="pricing-period" style="font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 0.85rem !important; font-weight: 500 !important; color: #8C9A8E !important; display: block !important; text-align: center !important; margin-top: 2px !important;">/ 5 năm</span>
                        </div>
                    </div>
                    <ul class="pricing-features-list">
                        <li><i class="fa-solid fa-check"></i> <strong>Khoảng cách bảo hộ độc quyền:</strong> Bán kính 5 – 8 km</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Phí duy trì thương hiệu:</strong> Năm đầu 8 tr/tháng, các năm sau 10 tr/tháng</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Đào tạo:</strong> 18 buổi tại văn phòng + 10 buổi tại điểm bán</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Hỗ trợ Marketing:</strong> Kế hoạch quảng cáo định kỳ hàng tháng</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Setup bàn giao:</strong> Bàn giao toàn bộ vận hành đạt chuẩn</li>
                    </ul>
                    <a href="#dang-ky" class="btn-hero-secondary" style="display: block; text-align: center; color: var(--color-primary-green); border-color: var(--color-primary-green);">ĐĂNG KÝ GÓI VÙNG VEN</a>
                </div>
            </div>'''

with open('franchise.html', 'r', encoding='utf-8') as f:
    fran = f.read()

fran = re.sub(
    r'<div class="pricing-grid">[\s\S]*?<!-- Bảng dự toán chi phí đầu tư -->',
    pricing_grid_block + '\n\n            <!-- Bảng dự toán chi phí đầu tư -->',
    fran
)

with open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(fran)

print('Both pricing cards restored and updated successfully.')
