import re
from pathlib import Path
path = Path('docs/fiskalna-analiza/Trenutni-Fiskalni-Prihodi-Podaci.md')
text = path.read_text(encoding='utf-8')
pattern = r"1\. \*\*Nova Ekonomija \(12\. maj 2025\) - Drzava zaradjuje stotine miliona evra\.\.\.\*\*[\s\S]*?Kontekstualizacija i javni podaci"
replacement = """1. **Nova Ekonomija (12. maj 2025) - \"Država zaradjuje stotine miliona evra...\"**
   - Prenosi izjave Ministarstva finansija o 177M € direktnih naknada i ~320M € ukupnog prihoda
   - Koristi se kao baseline dok se ne dobiju primarni podaci

2. **Serbian Monitor**
   - Industrijski izveštaji o tržištu igara na sreću
   - Statistički podaci i trendovi

3. **EGBA Report 2023** (European Gaming and Betting Association)
   - Napomena: download ograničen; služi samo kao okvirni benchmark dok se ne pribavi lokalna kopija

4. **Medijski izvori**
   - Euronews Serbia
   - Vesti.rs
   - Kontekstualizacija i javni podaci"""
new_text, count = re.subn(pattern, replacement, text, count=1)
if count != 1:
    raise SystemExit('pattern not found')
path.write_text(new_text, encoding='utf-8')
