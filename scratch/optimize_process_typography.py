# scratch/optimize_process_typography.py
import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

process_css_block = """
/* 10 Steps Process */
.process-10-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 16px;
    margin-top: 40px;
}

.process-10-card {
    background: #FFFFFF;
    border: 1px solid rgba(212, 163, 115, 0.3);
    border-radius: 14px;
    padding: 24px 10px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(24, 61, 43, 0.04);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    transition: var(--transition-smooth);
}

.process-10-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(24, 61, 43, 0.08);
    border-color: var(--color-sand-gold);
}

.process-10-num {
    display: inline-block;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1.25rem !important;
    font-weight: 700 !important;
    color: #C89D66 !important;
    font-variant-numeric: normal !important;
    margin-bottom: 8px !important;
}

.process-10-card h4 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    color: #1B382B !important;
    margin-bottom: 8px !important;
    line-height: 1.25 !important;
    text-wrap: balance !important;
    letter-spacing: 0.1px !important;
}

.process-10-card p {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.82rem !important;
    color: #5C6961 !important;
    line-height: 1.5 !important;
}
"""

css = re.sub(r'/\* 10 Steps Process[\s\S]*?\.process-10-card p\s*\{[^}]*\}', '', css)
css = re.sub(r'\.process-10-grid\s*\{[^}]*\}', '', css)
css = re.sub(r'\.process-10-card\s*\{[^}]*\}', '', css)
css = re.sub(r'\.process-10-card:hover\s*\{[^}]*\}', '', css)
css = re.sub(r'\.process-10-num\s*\{[^}]*\}', '', css)
css = re.sub(r'\.process-10-card h4\s*\{[^}]*\}', '', css)
css = re.sub(r'\.process-10-card p\s*\{[^}]*\}', '', css)

css += '\n' + process_css_block

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated 10-step process styles in style.css')
