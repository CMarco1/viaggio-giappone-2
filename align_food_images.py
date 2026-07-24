import re

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Giorno 2: Il testo parlava di Melon Pan, ma avevo messo la foto del Sukiyaki
html = re.sub(r"(<h4>Cosa mangiare:</h4>\s*<img src=')(.*?)(' alt=')Sukiyaki(' style='.*?<p><strong>Asakusa Kagetsudo)", 
    r"\g<1>https://upload.wikimedia.org/wikipedia/commons/a/a0/Melonpan_on_the_plastic_bag.jpg\g<3>Melon Pan\g<4>", html, flags=re.DOTALL)

# Giorno 3: Il testo parlava di Katsu Curry (Go! Go! Curry), ma c'era la foto del Ramen Shoyu
html = re.sub(r"(<h4>Cosa mangiare:</h4>\s*<img src=')(.*?)(' alt=')Curry(' style='.*?<p><strong>Go! Go! Curry)", 
    r"\g<1>https://upload.wikimedia.org/wikipedia/commons/c/cc/%E3%81%A8%E3%82%93%E3%81%8B%E3%82%89%E4%BA%AD_%E6%AD%A6%E8%94%B5%E9%87%8E%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%81%8B%E3%81%A4%E3%82%AB%E3%83%AC%E3%83%BC_-_1.jpg\g<3>Katsu Curry\g<4>", html, flags=re.DOTALL)

# Giorno 8: Il testo parlava di Matcha/Wagyu (Tsujiri), metto il Parfait di Matcha
html = re.sub(r"(<h4>Cosa mangiare:</h4>\s*<img src=')(.*?)(' alt=')Wagyu(' style='.*?<p><strong>Tsujiri)", 
    r"\g<1>https://upload.wikimedia.org/wikipedia/commons/f/ff/Maccha_parfait.jpg\g<3>Matcha Parfait\g<4>", html, flags=re.DOTALL)

# Giorno 10: Il testo parlava di Tako Tamago al Mercato Nishiki, ma la foto era dei Takoyaki classici
html = re.sub(r"(<h4>Cosa mangiare:</h4>\s*<img src=')(.*?)(' alt=')Takoyaki(' style='.*?<p><strong>Mercato Nishiki:)", 
    r"\g<1>https://upload.wikimedia.org/wikipedia/commons/4/4b/Tako_tamago.jpg\g<3>Tako Tamago\g<4>", html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Allineamento completato.")
