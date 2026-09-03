/* ==========================================================================
   HEAVEN - "trà ngon biết nói"
   Official Interactive Script
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. Sticky Transparent Header Transition ---
    const siteHeader = document.getElementById('siteHeader');
    
    const handleScroll = () => {
        if (window.scrollY > 50) {
            siteHeader.classList.add('scrolled');
        } else {
            siteHeader.classList.remove('scrolled');
        }
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check

    // --- 2. Mobile Menu Toggle ---
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.querySelector('.nav-menu');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            mobileToggle.classList.toggle('open');
        });

        // Close mobile menu when clicking nav link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                mobileToggle.classList.remove('open');
            });
        });
    }

    // --- 3. Initialize Swiper.js for Hero Slider ---
    if (typeof Swiper !== 'undefined' && document.querySelector('.heroSwiper')) {
        const heroSwiper = new Swiper('.heroSwiper', {
            loop: true,
            speed: 1200,
            effect: 'fade',
            fadeEffect: {
                crossFade: true
            },
            autoplay: {
                delay: 6000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
    }

    // --- 4. Featured Menu Tabs Filter (Homepage) ---
    const homeMenuTabs = document.querySelectorAll('.menu-tab-btn');
    const homeMenuCards = document.querySelectorAll('.menu-card');

    if (homeMenuTabs.length > 0 && homeMenuCards.length > 0) {
        homeMenuTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Update active tab
                homeMenuTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                const filterValue = tab.getAttribute('data-filter');

                // Filter cards with smooth fade
                homeMenuCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    if (filterValue === 'all' || category === filterValue) {
                        card.style.display = 'flex';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'scale(1)';
                        }, 20);
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.95)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 250);
                    }
                });
            });
        });
    }

    // --- 5. Menu Catalog Filter Bar (Menu Page) ---
    const catFilterBtns = document.querySelectorAll('.cat-filter-btn');
    const catalogCards = document.querySelectorAll('.catalog-item-card');

    if (catFilterBtns.length > 0 && catalogCards.length > 0) {
        catFilterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                catFilterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const selectedCategory = btn.getAttribute('data-category');

                catalogCards.forEach(card => {
                    const itemCat = card.getAttribute('data-cat');
                    if (selectedCategory === 'all' || itemCat === selectedCategory) {
                        card.style.display = 'flex';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'scale(1)';
                        }, 20);
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.95)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 250);
                    }
                });
            });
        });
    }

    // --- 6. Form Submission Handler Helper ---
    const handleFormSubmit = (formId, btnId, feedbackId, successMsg) => {
        const form = document.getElementById(formId);
        const btn = document.getElementById(btnId);
        const feedback = document.getElementById(feedbackId);

        if (form && btn && feedback) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();

                btn.classList.add('loading');
                btn.disabled = true;

                setTimeout(() => {
                    btn.classList.remove('loading');
                    btn.disabled = false;

                    feedback.className = 'form-feedback success';
                    feedback.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${successMsg}`;
                    form.reset();

                    setTimeout(() => {
                        feedback.style.display = 'none';
                        feedback.className = 'form-feedback';
                    }, 7000);
                }, 1200);
            });
        }
    };

    // Initialize all forms
    handleFormSubmit('reservationForm', 'btnSubmitRes', 'formFeedback', 'Đăng ký thành công! Chuyên viên nhượng quyền HEAVEN sẽ gửi trọn bộ hồ sơ tài chính chi tiết và liên hệ tư vấn trực tiếp cho bạn.');
    handleFormSubmit('franchiseForm', 'btnSubmitFran', 'franchiseFeedback', 'Đăng ký thành công! Chuyên viên nhượng quyền HEAVEN sẽ gửi trọn bộ tài liệu chi tiết và liên hệ hỗ trợ bạn.');
    handleFormSubmit('contactForm', 'btnSubmitContact', 'contactFeedback', 'Cảm ơn ý kiến đóng góp của bạn! Đội ngũ HEAVEN sẽ phản hồi sớm nhất.');

    // --- 7. Quick Toast for Add-to-Order buttons ---
    const addButtons = document.querySelectorAll('.btn-add-item, .btn-catalog-action');
    addButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const originalIcon = btn.innerHTML;
            btn.innerHTML = '<i class="fa-solid fa-check"></i>';
            btn.style.backgroundColor = '#2D6A4F';
            btn.style.color = '#FFFFFF';
            btn.style.borderColor = '#FFFFFF';

            setTimeout(() => {
                btn.innerHTML = originalIcon;
                btn.style.backgroundColor = '';
                btn.style.color = '';
                btn.style.borderColor = '';
            }, 1500);
        });
    });

});
