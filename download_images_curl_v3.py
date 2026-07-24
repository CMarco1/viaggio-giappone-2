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
        filename = url.split('/')[-1].replace('%', '_')
        
    local_path = os.path.join(img_dir, filename)
    
    print(f"Downloading {filename}...")
    cmd = ["curl", "-s", "-L", "-o", local_path, "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", url]
    subprocess.run(cmd)
    time.sleep(3)
        
    html = html.replace(url, f"images/{filename}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
