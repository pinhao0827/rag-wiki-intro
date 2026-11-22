"""Download fixed arXiv PDFs and verify source hashes. Python standard library only."""
from pathlib import Path
import json, urllib.request, hashlib
root=Path(__file__).resolve().parents[1]
dest=root/'raw/downloads';dest.mkdir(exist_ok=True)
for item in json.loads((root/'raw/manifest.json').read_text(encoding='utf-8')):
    path=dest/(item['id']+'.pdf')
    if not path.exists():
        with urllib.request.urlopen(item['url'],timeout=60) as r:path.write_bytes(r.read())
    good=hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256']
    print(item['id'],'PASS' if good else 'HASH MISMATCH')
    if not good:raise SystemExit(1)
