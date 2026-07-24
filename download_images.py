import re
import urllib.request
import time
import os

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Trova tutti i link
bg_urls = re.findall(r"url\('([^']+)'\)", html)
src_urls = re.findall(r"src='([^']+)'", html)
all_urls = list(set(bg_urls + src_urls))

# Ignoro i link di Google Maps e Unsplash (che reggono il traffico senza 429) e scarico solo Wikipedia
# Oppure meglio scaricare TUTTO per avere zero dipendenze esterne.
for url in all_urls:
    if "images.unsplash.com" in url:
        # Se è unsplash teniamo un nome file pulito
        filename = url.split('/')[-1].split('?')[0] + ".jpg"
    else:
        # Pulisci il nome del file (da url encode a nome normale se possibile)
        filename = urllib.parse.unquote(url.split('/')[-1])
        filename = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', filename)
        
    local_path = os.path.join(img_dir, filename)
    
    # Se il file non esiste già, scaricalo
    if not os.path.exists(local_path):
        print(f"Downloading {filename}...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
            with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
                out_file.write(response.read())
            time.sleep(1) # Pausa per non far arrabbiare Wikipedia
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            
    # Aggiorna l'HTML per puntare alla cartella locale
    html = html.replace(url, f"images/{filename}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Tutte le immagini scaricate e HTML aggiornato!")
