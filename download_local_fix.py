import re
import urllib.request
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# I 404 su Unsplash avvengono perché gli ID non esistono più.
# Cerchiamo su Pexels o link alternativi Unsplash sicuri (le API di Unsplash nascondono molti ID)

# Giorno 1: Shinjuku 
html = html.replace("images/photo-1542051812871-757500933fa8_3.jpg", "https://images.unsplash.com/photo-1536294711317-0a44dc72719c?w=800&q=80")
# Taiyaki
html = html.replace("images/photo-1516054817457-3f3099908cf6_6.jpg", "https://images.unsplash.com/photo-1620063223049-550a2569ba88?w=500&q=80")
# Okonomiyaki
html = html.replace("images/photo-1504669882200-a15d050d4f3b_8.jpg", "https://images.unsplash.com/photo-1551221763-718e8a6411d7?w=500&q=80")
# Nishiki
html = html.replace("images/photo-1563261623-f38b0bd58f00_22.jpg", "https://images.unsplash.com/photo-1558231269-e315579d4692?w=800&q=80")
# Shinsekai
html = html.replace("images/photo-1512401662916-25f0e137ca25_27.jpg", "https://images.unsplash.com/photo-1583091910237-77fb2559ccac?w=800&q=80")
# Kushikatsu
html = html.replace("images/photo-1544681280-d2dc1e6fb3cd_30.jpg", "https://images.unsplash.com/photo-1562919427-d0d1e39bbf87?w=500&q=80")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
