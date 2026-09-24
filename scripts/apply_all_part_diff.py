#!/usr/bin/env python3
"""
Systematically apply Part I, II, III differentiation and unified sidebar across:
1. All 10 Chapters:
   - Sidebar Part section labels and active part-themed chapter link
   - My Notes section preserved in all 10 chapters
   - Top bar header-chapter-title
   - Hero section prominent .chapter-part-banner
   - TOC card .toc-part-tag
2. Exams (mock-exam.html, unit-quiz.html):
   - Sidebar Part section labels
3. Root pages (index.html, progress.html):
   - Sidebar Part section labels and index.html part-divider badges
"""

import os
import re

BASE_DIR = '/Users/arpit/minibook/cn'
CHAPTERS_DIR = os.path.join(BASE_DIR, 'chapters')
EXAMS_DIR = os.path.join(BASE_DIR, 'exams')

CHAPTERS_INFO = [
    {
        'file': 'ch01-fundamentals.html',
        'num': 1,
        'header_title': 'Ch 1 — Network Fundamentals',
        'link_name': 'Ch 1 — Fundamentals',
        'icon': '📡',
        'part_id': 'part-i',
        'part_badge': 'Part I',
        'part_name': 'Part I — Introduction',
        'part_full': 'Introduction to Computer Networks',
    },
    {
        'file': 'ch02-types-topologies.html',
        'num': 2,
        'header_title': 'Ch 2 — Types of Networks & Topologies',
        'link_name': 'Ch 2 — Types &amp; Topologies',
        'icon': '🔗',
        'part_id': 'part-i',
        'part_badge': 'Part I',
        'part_name': 'Part I — Introduction',
        'part_full': 'Introduction to Computer Networks',
    },
    {
        'file': 'ch03-models-addressing.html',
        'num': 3,
        'header_title': 'Ch 3 — Network Models & Addressing',
        'link_name': 'Ch 3 — Models &amp; Addressing',
        'icon': '📦',
        'part_id': 'part-i',
        'part_badge': 'Part I',
        'part_name': 'Part I — Introduction',
        'part_full': 'Introduction to Computer Networks',
    },
    {
        'file': 'ch04-devices-sdn.html',
        'num': 4,
        'header_title': 'Ch 4 — Network Devices & SDN',
        'link_name': 'Ch 4 — Devices &amp; SDN',
        'icon': '🔌',
        'part_id': 'part-i',
        'part_badge': 'Part I',
        'part_name': 'Part I — Introduction',
        'part_full': 'Introduction to Computer Networks',
    },
    {
        'file': 'ch05-physical-fundamentals.html',
        'num': 5,
        'header_title': 'Ch 5 — Physical Fundamentals',
        'link_name': 'Ch 5 — Physical Fundamentals',
        'icon': '📶',
        'part_id': 'part-ii',
        'part_badge': 'Part II',
        'part_name': 'Part II — Physical Layer',
        'part_full': 'Physical Layer',
    },
    {
        'file': 'ch06-media-signaling.html',
        'num': 6,
        'header_title': 'Ch 6 — Media & Line Coding',
        'link_name': 'Ch 6 — Media &amp; Line Coding',
        'icon': '🔌',
        'part_id': 'part-ii',
        'part_badge': 'Part II',
        'part_name': 'Part II — Physical Layer',
        'part_full': 'Physical Layer',
    },
    {
        'file': 'ch07-modulation-switching.html',
        'num': 7,
        'header_title': 'Ch 7 — Modulation & Switching',
        'link_name': 'Ch 7 — Modulation &amp; Switching',
        'icon': '📻',
        'part_id': 'part-ii',
        'part_badge': 'Part II',
        'part_name': 'Part II — Physical Layer',
        'part_full': 'Physical Layer',
    },
    {
        'file': 'ch08-dll-fundamentals.html',
        'num': 8,
        'header_title': 'Ch 8 — DLL Fundamentals & Errors',
        'link_name': 'Ch 8 — DLL Fundamentals',
        'icon': '🔧',
        'part_id': 'part-iii',
        'part_badge': 'Part III',
        'part_name': 'Part III — Data Link Layer',
        'part_full': 'Data Link Layer',
    },
    {
        'file': 'ch09-protocols-sliding.html',
        'num': 9,
        'header_title': 'Ch 9 — Protocols & Sliding Window',
        'link_name': 'Ch 9 — Protocols &amp; Sliding Window',
        'icon': '🔄',
        'part_id': 'part-iii',
        'part_badge': 'Part III',
        'part_name': 'Part III — Data Link Layer',
        'part_full': 'Data Link Layer',
    },
    {
        'file': 'ch10-mac-ethernet.html',
        'num': 10,
        'header_title': 'Ch 10 — MAC & Ethernet',
        'link_name': 'Ch 10 — MAC &amp; Ethernet',
        'icon': '🌐',
        'part_id': 'part-iii',
        'part_badge': 'Part III',
        'part_name': 'Part III — Data Link Layer',
        'part_full': 'Data Link Layer',
    },
]

def generate_chapter_sidebar_block(current_file=None):
    """
    Builds the clean, unified 3-part sidebar section + My Notes for chapters.
    """
    lines = []
    # Part I
    lines.append('    <div class="sidebar-section">')
    lines.append('      <div class="sidebar-section-label part-label part-i">Part I — Introduction</div>')
    for ch in CHAPTERS_INFO[:4]:
        cls = 'sidebar-link active part-i' if ch['file'] == current_file else 'sidebar-link'
        lines.append(f'      <a href="{ch["file"]}" class="{cls}"><span class="link-icon">{ch["icon"]}</span>{ch["link_name"]}</a>')
    lines.append('    </div>')

    # Part II
    lines.append('    <div class="sidebar-section">')
    lines.append('      <div class="sidebar-section-label part-label part-ii">Part II — Physical Layer</div>')
    for ch in CHAPTERS_INFO[4:7]:
        cls = 'sidebar-link active part-ii' if ch['file'] == current_file else 'sidebar-link'
        lines.append(f'      <a href="{ch["file"]}" class="{cls}"><span class="link-icon">{ch["icon"]}</span>{ch["link_name"]}</a>')
    lines.append('    </div>')

    # Part III
    lines.append('    <div class="sidebar-section">')
    lines.append('      <div class="sidebar-section-label part-label part-iii">Part III — Data Link Layer</div>')
    for ch in CHAPTERS_INFO[7:]:
        cls = 'sidebar-link active part-iii' if ch['file'] == current_file else 'sidebar-link'
        lines.append(f'      <a href="{ch["file"]}" class="{cls}"><span class="link-icon">{ch["icon"]}</span>{ch["link_name"]}</a>')
    lines.append('    </div>')

    # My Notes Section
    lines.append('    <div class="sidebar-section">')
    lines.append('      <div class="sidebar-section-label">My Notes</div>')
    lines.append('      <div id="notes-sidebar-list"></div>')
    lines.append('    </div>')

    return '\n'.join(lines)

def process_chapters():
    # Matches from Part I — Introduction down to </nav>
    sidebar_pattern = re.compile(
        r'<div class="sidebar-section">\s*<div class="sidebar-section-label[^"]*">\s*Part I — Introduction\s*</div>.*?(?=\s*</nav>)',
        re.DOTALL
    )

    for ch in CHAPTERS_INFO:
        fpath = os.path.join(CHAPTERS_DIR, ch['file'])
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update Header Chapter Title
        content = re.sub(
            r'<span class="header-chapter-title">.*?</span>',
            f'<span class="header-chapter-title">{ch["header_title"]}</span>',
            content
        )

        # 2. Clean any trailing My Notes outside </nav>
        content = re.sub(
            r'</nav>\s*<div class="sidebar-section">\s*<div class="sidebar-section-label">My Notes</div>\s*<div id="notes-sidebar-list"></div>\s*</div>',
            r'</nav>',
            content
        )

        # 3. Update Sidebar Part Block (including My Notes)
        new_sidebar_block = generate_chapter_sidebar_block(current_file=ch['file'])
        if sidebar_pattern.search(content):
            content = sidebar_pattern.sub(new_sidebar_block, content)
        else:
            print(f"Warning: Sidebar part block pattern not matched in {ch['file']}")

        # 4. Chapter Hero Part Banner
        banner_html = f'''    <div class="chapter-part-banner {ch["part_id"]}">
      <span class="part-banner-badge">{ch["part_badge"]}</span>
      <span>{ch["part_full"]}</span>
    </div>'''

        if '<div class="chapter-part-banner' in content:
            content = re.sub(
                r'<div class="chapter-part-banner[^>]*>.*?</div>',
                banner_html.strip(),
                content,
                flags=re.DOTALL
            )
        else:
            # Place right before <h1 class="chapter-title">
            if '<h1 class="chapter-title">' in content:
                content = content.replace(
                    '<h1 class="chapter-title">',
                    f'{banner_html}\n    <h1 class="chapter-title">'
                )
            else:
                print(f"Warning: <h1 class=\"chapter-title\"> not found in {ch['file']}")

        # 5. TOC Part Tag
        toc_tag_html = f'<div class="toc-part-tag {ch["part_id"]}">{ch["part_badge"]} · {ch["part_full"]}</div>'
        if '<div class="toc-part-tag' in content:
            content = re.sub(
                r'<div class="toc-part-tag[^>]*>.*?</div>',
                toc_tag_html,
                content
            )
        else:
            m = re.search(r'(<div class="toc-card[^"]*"[^>]*>)', content)
            if m:
                open_tag = m.group(1)
                content = content.replace(
                    open_tag,
                    f'{open_tag}\n    {toc_tag_html}'
                )
            else:
                print(f"Warning: .toc-card not found in {ch['file']}")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Processed {ch['file']} -> {ch['part_badge']}")

def process_other_pages():
    def update_sidebar_labels(text):
        text = re.sub(
            r'<div class="sidebar-section-label[^"]*">\s*Part I — Introduction\s*</div>',
            r'<div class="sidebar-section-label part-label part-i">Part I — Introduction</div>',
            text
        )
        text = re.sub(
            r'<div class="sidebar-section-label[^"]*">\s*Part II — Physical Layer\s*</div>',
            r'<div class="sidebar-section-label part-label part-ii">Part II — Physical Layer</div>',
            text
        )
        text = re.sub(
            r'<div class="sidebar-section-label[^"]*">\s*Part III — Data Link Layer\s*</div>',
            r'<div class="sidebar-section-label part-label part-iii">Part III — Data Link Layer</div>',
            text
        )
        return text

    pages = [
        os.path.join(EXAMS_DIR, 'mock-exam.html'),
        os.path.join(EXAMS_DIR, 'unit-quiz.html'),
        os.path.join(BASE_DIR, 'index.html'),
        os.path.join(BASE_DIR, 'progress.html'),
    ]

    for p in pages:
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        content = update_sidebar_labels(content)

        # For index.html specifically
        if 'index.html' in p:
            content = re.sub(
                r'<div class="part-divider[^"]*">\s*<span class="part-label[^"]*">\s*Part I — Introduction to Computer Networks\s*</span>\s*</div>',
                r'<div class="part-divider"><span class="part-label part-i">Part I — Introduction to Computer Networks</span></div>',
                content
            )
            content = re.sub(
                r'<div class="part-divider[^"]*">\s*<span class="part-label[^"]*">\s*Part II — Physical Layer\s*</span>\s*</div>',
                r'<div class="part-divider"><span class="part-label part-ii">Part II — Physical Layer</span></div>',
                content
            )
            content = re.sub(
                r'<div class="part-divider[^"]*">\s*<span class="part-label[^"]*">\s*Part III — Data Link Layer ⭐\s*</span>\s*</div>',
                r'<div class="part-divider"><span class="part-label part-iii">Part III — Data Link Layer ⭐</span></div>',
                content
            )

            if '.part-label.part-i' not in content:
                content = content.replace(
                    '.part-label { font-size:.8rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--accent-light);white-space:nowrap; }',
                    '''.part-label { font-size:.8rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;white-space:nowrap; }
.part-label.part-i { color: #38bdf8; }
.part-label.part-ii { color: #fbbf24; }
.part-label.part-iii { color: #f87171; }'''
                )

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Processed {os.path.basename(p)}")

def main():
    process_chapters()
    process_other_pages()
    print("✨ Successfully updated all chapters and pages!")

if __name__ == '__main__':
    main()
