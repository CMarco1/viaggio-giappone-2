import re
import urllib.request

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Trova i background
bg_urls = re.findall(r"background-image:\s*url\('([^']+)'\)", html)
# Trova i tag img (sia con apici singoli che doppi)
img_urls1 = re.findall(r"<img[^>]+src='([^']+)'", html)
img_urls2 = re.findall(r'<img[^>]+src="([^"]+)"', html)

all_urls = list(set(bg_urls + img_urls1 + img_urls2))
broken = []

print(f"Sto controllando {len(all_urls)} immagini...")

for url in all_urls:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        res = urllib.request.urlopen(req, timeout=5)
        if res.getcode() != 200:
            broken.append(url)
    except Exception as e:
        broken.append(f"{url} - Errore: {e}")

if not broken:
    print("Tutte le immagini funzionano correttamente! (Status 200)")
else:
    print("Le seguenti immagini sono rotte:")
    for b in broken:
        print(b)
