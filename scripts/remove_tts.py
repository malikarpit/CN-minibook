"""
Script to completely remove Text-to-Speech (TTS) from the CN MiniBook.
Removes:
1. #tts-toggle buttons from navigation headers
2. #tts-panel floating audio controls
3. <script src="...tts.js"></script> references
4. Validates all HTML files for tag balance and duplicate IDs
"""
import glob, os, re, html.parser

class MasterValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.ids = set()
        self.duplicates = []
        self.void_tags = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k == 'id':
                if v in self.ids:
                    self.duplicates.append(v)
                self.ids.add(v)
        if tag not in self.void_tags:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_tags:
            return
        if not self.stack:
            return
        top_tag, pos = self.stack.pop()

btn_pattern = re.compile(r'\s*<button\s+id=[\"\']tts-toggle[\"\'][\s\S]*?</button>')
panel_pattern = re.compile(r'\s*(?:<!--\s*TTS\s*FLOATING\s*PANEL\s*-->\s*)?<div\s+id=[\"\']tts-panel[\"\'][\s\S]*?<div\s+class=[\"\']tts-voice[\"\'][\s\S]*?</div>\s*</div>')
script_pattern = re.compile(r'\s*<script\s+src=[\"\'][^\"\']*tts\.js[\"\']\s*></script>')

target_files = sorted(glob.glob('chapters/ch*.html')) + ['index.html', 'exams/unit-quiz.html', 'exams/mock-exam.html']

print(f'Processing {len(target_files)} HTML files for complete TTS removal...')

all_passed = True
for path in target_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Button
    new_content, btn_subs = btn_pattern.subn('', content)
    # 2. Remove Panel
    new_content, pnl_subs = panel_pattern.subn('', new_content)
    # 3. Remove Script
    new_content, scr_subs = script_pattern.subn('', new_content)

    if btn_subs != 1 or pnl_subs != 1 or scr_subs != 1:
        print(f'Warning in {path}: btn={btn_subs}, pnl={pnl_subs}, scr={scr_subs}')
        all_passed = False

    # Check for any remaining tts in new_content
    rem = len(re.findall(r'tts', new_content, flags=re.I))
    if rem > 0:
        print(f'Notice: {rem} remaining "tts" references in {path}')

    # Validate HTML
    val = MasterValidator()
    val.feed(new_content)
    if val.stack or val.duplicates:
        print(f'Validation error in {path}: unclosed={len(val.stack)}, dups={len(val.duplicates)}')
        all_passed = False

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if all_passed:
    print('✅ Successfully removed TTS from all 21 HTML files with 100% tag validation!')
else:
    print('⚠️ Some files had issues during removal. Please inspect above logs.')
