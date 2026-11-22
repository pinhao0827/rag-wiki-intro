"""Re-render the HTML without modifying its original execution record."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'content.json').read_text(encoding='utf-8'))
data['run']=json.loads((root/'records/run.json').read_text(encoding='utf-8'))
payload=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
template=(root/'scripts/template.html').read_text(encoding='utf-8')
(root/'index.html').write_text(template.replace('/*__CONTENT__*/',payload),encoding='utf-8')
print('Rebuilt index.html. Run scripts/check.py next. Existing run.json preserved.')
