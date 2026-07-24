import re

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Eseguo le sostituzioni ma con un pattern meno aggressivo (non greedy e che non cattura righe extra usando [^<]+ invece di .*)

# Giorno 2: Melon Pan
html = re.sub(r"(<h4>Cosa mangiare:</h4>\s*<img src=')[^']*(.*?alt=')Sukiyaki(')", 
    r"\g<1>https://upload.wikimedia.org/wikipedia/commons/a/a0/Melonpan_on_the_plastic_bag.jpg\g<2>Melon Pan\g<3>", html)

# Giorno 3: Katsu Curry
html = re.sub(r"(<h4>Cosa mangiare:</h4>\s*<img src=')[^']*(.*?alt=')Curry(')", 
    r"\g<1>https://upload.wikimedia.org/wikipedia/commons/c/cc/%E3%81%A8%E3%82%93%E3%81%8B%E3%82%89%E4%BA%AD_%E6%AD%A6%E8%94%B5%E9%87%8E%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%81%8B%E3%81%A4%E3%82%AB%E3%83%AC%E3%83%BC_-_1.jpg\g<2>Katsu Curry\g<3>", html)

# Giorno 8: Matcha
html = re.sub(r"(<h4>Cosa mangiare:</h4>\s*<img src=')[^']*(.*?alt=')Wagyu(')", 
    r"\g<1>https://upload.wikimedia.org/wikipedia/commons/f/ff/Maccha_parfait.jpg\g<2>Matcha Parfait\g<3>", html)

# Giorno 10: Tako tamago
html = re.sub(r"(<h4>Cosa mangiare:</h4>\s*<img src=')[^']*(.*?alt=')Takoyaki(')", 
    r"\g<1>https://upload.wikimedia.org/wikipedia/commons/4/4b/Tako_tamago.jpg\g<2>Tako Tamago\g<3>", html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
