import re
import urllib.request
import os
import time
import ssl

# Ignora errori SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Estraggo URL
bg_urls = re.findall(r"url\('([^']+)'\)", html)
src_urls = re.findall(r"src='([^']+)'", html)
all_urls = list(set(bg_urls + src_urls))

print(f"Inizio download di {len(all_urls)} immagini...")

for i, url in enumerate(all_urls):
    if "images.unsplash.com" in url:
        filename = url.split('/')[-1].split('?')[0] + f"_{i}.jpg"
    else:
        filename = f"img_{i}.jpg"
        
    local_path = os.path.join(img_dir, filename)
    
    # Download
    print(f"Scaricando: {filename}")
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8"
    })
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        time.sleep(1) # pausa per sicurezza
    except Exception as e:
        print(f"Errore su {url}: {e}")

    # Sostituisco nell'HTML il path relativo
    html = html.replace(url, f"images/{filename}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Download concluso e HTML aggiornato!")
