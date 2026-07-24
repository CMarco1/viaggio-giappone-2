import re
import urllib.request

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Trova tutti i link di background-image e src
bg_urls = re.findall(r"url\('([^']+)'\)", html)
src_urls = re.findall(r"src='([^']+)'", html)
all_urls = list(set(bg_urls + src_urls))

broken = []
for url in all_urls:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        res = urllib.request.urlopen(req, timeout=5)
        if res.getcode() != 200:
            broken.append(url)
    except Exception as e:
        broken.append(f"{url} - Errore: {e}")

if not broken:
    print(f"SUCCESSO! Tutte le {len(all_urls)} immagini funzionano (Stato 200).")
else:
    for b in broken: print(b)
