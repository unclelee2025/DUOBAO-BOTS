from pathlib import Path
text = Path('bots/guide_bot/handlers.py').read_text(encoding='utf-8')
start = text.index('     en: {')
print(start)
print(text[start:start+4000])
