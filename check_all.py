import re
import urllib.request
import urllib.error

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

bg_urls = re.findall(r"url\('([^']+)'\)", html)
src_urls = re.findall(r"src='([^']+)'", html)
all_urls = bg_urls + src_urls

for url in all_urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        res = urllib.request.urlopen(req)
        status = res.getcode()
        if status != 200:
            print(f"BROKEN [{status}]: {url}")
    except urllib.error.HTTPError as e:
        print(f"BROKEN [{e.code}]: {url}")
    except Exception as e:
        print(f"BROKEN [Error]: {url} ({e})")
