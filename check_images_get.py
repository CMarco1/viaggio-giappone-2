import re
import urllib.request
import time

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Trova i background
bg_urls = re.findall(r"background-image:\s*url\('([^']+)'\)", html)
# Trova i tag img
img_urls1 = re.findall(r"<img[^>]+src='([^']+)'", html)
img_urls2 = re.findall(r'<img[^>]+src="([^"]+)"', html)

all_urls = list(set(bg_urls + img_urls1 + img_urls2))

print(f"Ho trovato {len(all_urls)} URL unici.")
broken = []

for url in all_urls:
    try:
        # Usa GET invece di HEAD e rallenta per evitare i rate limit di Wikipedia (Errore 429)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
        res = urllib.request.urlopen(req, timeout=5)
        time.sleep(0.5) 
    except Exception as e:
        if "429" not in str(e): # Ignoro i rate limit veri e propri causati dal mio check massivo
            broken.append(f"{url} - {e}")

if not broken:
    print("Nessuna immagine rotta (esclusi gli errori 429 temporanei di Wikipedia).")
else:
    for b in broken: print(b)
