import re
import subprocess
import time
import os

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

bg_urls = re.findall(r"url\('([^']+)'\)", html)
src_urls = re.findall(r"src='([^']+)'", html)
all_urls = list(set(bg_urls + src_urls))

for url in all_urls:
    if "images.unsplash.com" in url:
        filename = url.split('/')[-1].split('?')[0] + ".jpg"
    else:
        # Pulizia URL decode
        filename = url.split('/')[-1]
        filename = filename.replace('%', '_')
        
    local_path = os.path.join(img_dir, filename)
    
    if not os.path.exists(local_path) or os.path.getsize(local_path) < 1000:
        print(f"Downloading {filename} via curl...")
        cmd = ["curl", "-s", "-L", "-o", local_path, "-A", "Mozilla/5.0", url]
        subprocess.run(cmd)
        time.sleep(2)
        
    html = html.replace(url, f"images/{filename}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Immagini scaricate e file HTML aggiornato.")
