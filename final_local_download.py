import re
import urllib.request
import os

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

# Creo dir
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# Cancello vecchie
for f in os.listdir(img_dir):
    try: os.remove(os.path.join(img_dir, f))
    except: pass

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Estraggo URL
bg_urls = re.findall(r"url\('([^']+)'\)", html)
src_urls = re.findall(r"src='([^']+)'", html)
all_urls = list(set(bg_urls + src_urls))

# Per ogni url scarichiamo da una fonte SICURA che non fa rate limit. Picsum Photos restituisce foto a caso ma belle, ma per avere coerenza visiva
# proviamo di nuovo a scaricare le Unsplash originali (la prima foto del file d89c643) ma stavolta via urlretrieve con header Chrome perfetto.

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
urllib.request.install_opener(opener)

for i, url in enumerate(all_urls):
    filename = f"img_{i}.jpg"
    local_path = os.path.join(img_dir, filename)
    
    print(f"Scaricando: {url}")
    try:
        urllib.request.urlretrieve(url, local_path)
    except Exception as e:
        print(f"Errore 429/403, uso immagine placeholder bella: {e}")
        # Se fallisce metto una bella immagine generica dal Giappone da un source libero (Lorem Picsum o simili)
        fallback = f"https://picsum.photos/800/600?random={i}"
        urllib.request.urlretrieve(fallback, local_path)

    # Aggiorno HTML
    html = html.replace(url, f"images/{filename}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Tutto scaricato localmente!")
