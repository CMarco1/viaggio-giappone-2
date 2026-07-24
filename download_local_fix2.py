import re
import urllib.request
import os
import time
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Riscansiono solo gli url esterni rimasti
urls = re.findall(r"(https://images.unsplash.com[^\'\"]*)", html)
urls = list(set(urls))

for i, url in enumerate(urls):
    filename = f"fixed_img_{i}.jpg"
    local_path = os.path.join(img_dir, filename)
    
    print(f"Scaricando: {filename}")
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    })
    
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        time.sleep(1)
    except Exception as e:
        print(f"Errore: {e}")

    html = html.replace(url, f"images/{filename}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
