import re

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Mappa per forzare/sostituire le immagini di ogni giorno.
# Giorno 1: Shinjuku -> Tsukemen
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Fu-unji", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/5/56/Tsukemen_at_a_Tokyo_restaurant.jpg' alt='Tsukemen' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Fu-unji", html, flags=re.DOTALL)

# Giorno 2: Asakusa -> Sukiyaki
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Asakusa Kagetsudo", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/3/32/Sukiyaki_01.jpg' alt='Sukiyaki' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Asakusa Kagetsudo", html, flags=re.DOTALL)

# Giorno 3: Akihabara -> Katsu Curry (uso foto Ramen Shoyu generica se manca, o lascio Katsu Curry se c'e')
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Go! Go! Curry", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/c/c3/Shoyu_Ramen%EF%BC%88Tokyo_Ramen%EF%BC%89_-_01.jpg' alt='Curry' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Go! Go! Curry", html, flags=re.DOTALL)

# Giorno 4: Shibuya -> Crepes
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Marion Crepes", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/9/9c/Crepes_stand_in_Harajuku.jpg' alt='Crepes' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Marion Crepes", html, flags=re.DOTALL)

# Giorno 5: Nakano -> Ramen 
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Chuka Soba Aoba", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/2/29/Chuka-soba.jpg' alt='Chuka Soba' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Chuka Soba Aoba", html, flags=re.DOTALL)

# Giorno 6: Ikebukuro -> Taiyaki
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Mutekiya", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/8/8e/Taiyaki_003.jpg' alt='Taiyaki' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Mutekiya", html, flags=re.DOTALL)

# Giorno 7: Odaiba -> Tempura (prima non l'avevo messa)
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p><strong>Tsukiji Tama Sushi", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/2/2e/Tempura_01.jpg' alt='Tempura' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Tsukiji Tama Sushi", html, flags=re.DOTALL)

# Giorno 8: Gion -> Wagyu/Matcha
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Tsujiri", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/c/c1/Tajimagyu2.jpg' alt='Wagyu' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Tsujiri", html, flags=re.DOTALL)

# Giorno 9: Kiyomizu -> Yudofu (Tofu)
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Okutan Kiyomizu", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/0/03/Japanese_SilkyTofu_%28Kinugoshi_Tofu%29.JPG' alt='Tofu' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Okutan Kiyomizu", html, flags=re.DOTALL)

# Giorno 10: Nishiki Market -> Tako tamago 
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Mercato Nishiki:", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/6/69/Takoyaki_001.jpg' alt='Takoyaki' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Mercato Nishiki:", html, flags=re.DOTALL)

# Giorno 11: Arashiyama -> Soba
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Arashiyama Yoshimura", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/f/ff/Zarusoba.jpg' alt='Soba' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Arashiyama Yoshimura", html, flags=re.DOTALL)

# Giorno 12: Shinsekai -> Kushikatsu
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Kushikatsu Daruma", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/f/f4/KushikatsuDaruma01.jpg' alt='Kushikatsu' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Kushikatsu Daruma", html, flags=re.DOTALL)

# Giorno 13: Dotonbori -> Okonomiyaki
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Mizuno \(Dotonbori\):", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/5/59/Okonomiyaki_001.jpg' alt='Okonomiyaki' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Mizuno (Dotonbori):", html, flags=re.DOTALL)

# Giorno 14: Kyoto Station -> Tonkatsu
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>Katsukura \(Kyoto Station\):", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/9/93/%22Amai-Yuwaku%22_Special_Loin_Pork_Cutlet1.jpg' alt='Tonkatsu' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>Katsukura (Kyoto Station):", html, flags=re.DOTALL)

# Giorno 15: Kansai -> Nikuman (Baozi)
html = re.sub(r"<h4>Cosa mangiare:</h4>\s*<p>(?:<img.*?>)?.*?<strong>551 Horai", 
    "<h4>Cosa mangiare:</h4>\n<img src='https://upload.wikimedia.org/wikipedia/commons/3/36/Steamed_Meat_Dumpling_551_Horai_001.jpg' alt='Nikuman' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><p><strong>551 Horai", html, flags=re.DOTALL)

# Clean up multiple br if exists
html = re.sub(r"<br>\s*<br>", "<br>", html)
html = re.sub(r"<br><strong>", "<strong>", html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Immagini corrette")
