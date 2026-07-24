import re
import urllib.request
import os

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

bg_urls = re.findall(r"url\('([^']+)'\)", html)
src_urls = re.findall(r"src='([^']+)'", html)
all_urls = list(set(bg_urls + src_urls))

opener = urllib.request.build_opener()
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, come Gecko) Chrome/120.0.0.0 Safari/537.36'),
    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'),
    ('Accept-Language', 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7'),
    ('Referer', 'https://en.wikipedia.org/')
]
urllib.request.install_opener(opener)

for url in all_urls:
    if "images.unsplash.com" in url:
        filename = url.split('/')[-1].split('?')[0] + ".jpg"
    else:
        filename = url.split('/')[-1]
        filename = filename.replace('%', '_')
        
    local_path = os.path.join(img_dir, filename)
    
    print(f"Scaricando {filename}...")
    try:
        urllib.request.urlretrieve(url, local_path)
    except Exception as e:
        print(f"FALLITO: {url} -> {e}")

