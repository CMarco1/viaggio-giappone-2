import re

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Rimuovere la sezione "Cibo Tipico" generica
food_section_pattern = r'<section>\s*<h2>🍱 Cibo Tipico da Assaggiare</h2>\s*<div class="food-grid">.*?</div>\s*</section>'
html = re.sub(food_section_pattern, '', html, flags=re.DOTALL)

# Definiamo i dati da aggiornare per ogni giorno: mappa + immagine cibo
updates = {
    # Giorno 1: Shinjuku -> Fu-unji
    "Shinjuku,+Tokyo&t=&z=14": "Shinjuku,+Tokyo&daddr=Fu-unji,+Shinjuku,+Tokyo&dirflg=w&t=&z=15",
    "<strong>Fu-unji": "<img src='https://upload.wikimedia.org/wikipedia/commons/c/c3/Shoyu_Ramen%EF%BC%88Tokyo_Ramen%EF%BC%89_-_01.jpg' alt='Ramen' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Fu-unji",
    
    # Giorno 2: Senso-ji -> Asakusa Kagetsudo -> Tokyo Skytree
    "saddr=Senso-ji,+Tokyo&daddr=Tokyo+Skytree,+Tokyo": "saddr=Senso-ji,+Tokyo&daddr=Asakusa+Kagetsudo,+Tokyo+to:Tokyo+Skytree,+Tokyo",
    "<strong>Asakusa Kagetsudo": "<img src='https://upload.wikimedia.org/wikipedia/commons/e/ea/Melonpan_by_oimax_in_Tokyo.jpg' alt='Melon Pan' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Asakusa Kagetsudo",

    # Giorno 3: Akihabara -> Go! Go! Curry
    "Akihabara,+Tokyo&t=&z=15": "Akihabara,+Tokyo&daddr=Go+Go+Curry,+Akihabara,+Tokyo&dirflg=w&t=&z=16",
    "<strong>Go! Go! Curry": "<img src='https://upload.wikimedia.org/wikipedia/commons/3/36/Katsu-curry_by_basyot_in_Sapporo.jpg' alt='Katsu Curry' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Go! Go! Curry",

    # Giorno 4: Meiji -> Takeshita -> Shibuya -> Uobei
    "saddr=Meiji-jingu,+Tokyo&daddr=Takeshita+Street,+Tokyo+to:Shibuya+Crossing,+Tokyo": "saddr=Meiji-jingu,+Tokyo&daddr=Takeshita+Street,+Tokyo+to:Shibuya+Crossing,+Tokyo+to:Uobei+Shibuya+Dogenzaka,+Tokyo",
    "<strong>Marion Crepes": "<img src='https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=500&q=80' alt='Sushi' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Marion Crepes",

    # Giorno 5: Nakano Broadway -> Chuka Soba Aoba
    "Nakano+Broadway,+Tokyo&t=&z=15": "Nakano+Broadway,+Tokyo&daddr=Chuka+Soba+Aoba,+Nakano,+Tokyo&dirflg=w&t=&z=16",
    "<strong>Chuka Soba Aoba": "<img src='https://upload.wikimedia.org/wikipedia/commons/7/75/Chukasoba_by_t-mizo_in_Nakano%2C_Tokyo.jpg' alt='Chuka Soba' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Chuka Soba Aoba",

    # Giorno 6: Ikebukuro -> Mutekiya
    "Sunshine+City,+Ikebukuro,+Tokyo&t=&z=15": "Sunshine+City,+Ikebukuro,+Tokyo&daddr=Mutekiya,+Ikebukuro,+Tokyo&dirflg=w&t=&z=15",
    "<strong>Mutekiya": "<img src='https://upload.wikimedia.org/wikipedia/commons/0/05/Taiyaki_001.jpg' alt='Taiyaki' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Mutekiya",

    # Giorno 8: Gion -> Tsujiri / Mikaku
    "Gion,+Kyoto&t=&z=15": "Gion,+Kyoto&daddr=Tsujiri,+Gion,+Kyoto+to:Pontocho,+Kyoto&dirflg=w&t=&z=15",
    "<strong>Tsujiri": "<img src='https://upload.wikimedia.org/wikipedia/commons/f/ff/Maccha_parfait.jpg' alt='Matcha Parfait' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Tsujiri",

    # Giorno 9: Kiyomizu -> Sannenzaka -> Okutan
    "saddr=Kiyomizu-dera,+Kyoto&daddr=Sannenzaka,+Kyoto+to:Ninenzaka,+Kyoto": "saddr=Kiyomizu-dera,+Kyoto&daddr=Sannenzaka,+Kyoto+to:Okutan,+Kiyomizu,+Kyoto+to:Ninenzaka,+Kyoto",
    "<strong>Okutan Kiyomizu": "<img src='https://upload.wikimedia.org/wikipedia/commons/1/14/Yudofu_by_t-mizo_in_Kyoto.jpg' alt='Yudofu' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Okutan Kiyomizu",

    # Giorno 10: Nishiki Market -> Manga Museum -> Gogyo
    "saddr=Nishiki+Market,+Kyoto&daddr=Kyoto+International+Manga+Museum": "saddr=Nishiki+Market,+Kyoto&daddr=Kyoto+International+Manga+Museum+to:Gogyo+Kyoto",
    "<strong>Mercato Nishiki:": "<img src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Tako_tamago.jpg' alt='Tako Tamago' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Mercato Nishiki:",

    # Giorno 11: Arashiyama -> Yoshimura -> Kinkakuji
    "saddr=Arashiyama+Bamboo+Grove,+Kyoto&daddr=Kinkaku-ji,+Kyoto": "saddr=Arashiyama+Bamboo+Grove,+Kyoto&daddr=Arashiyama+Yoshimura,+Kyoto+to:Kinkaku-ji,+Kyoto",
    "<strong>Arashiyama Yoshimura": "<img src='https://upload.wikimedia.org/wikipedia/commons/9/91/Soba_by_t-mizo.jpg' alt='Soba' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Arashiyama Yoshimura",

    # Giorno 12: Den Den Town -> Daruma -> Shinsekai
    "saddr=Nippombashi+Den+Den+Town,+Osaka&daddr=Shinsekai,+Osaka": "saddr=Nippombashi+Den+Den+Town,+Osaka&daddr=Kushikatsu+Daruma,+Shinsekai,+Osaka",
    "<strong>Kushikatsu Daruma": "<img src='https://upload.wikimedia.org/wikipedia/commons/8/87/Kushikatsu_by_t-mizo_in_Osaka.jpg' alt='Kushikatsu' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Kushikatsu Daruma",

    # Giorno 13: Dotonbori -> Mizuno
    "Dotonbori,+Osaka&t=&z=15": "Dotonbori,+Osaka&daddr=Mizuno,+Dotonbori,+Osaka&dirflg=w&t=&z=16",
    "<strong>Mizuno (Dotonbori):": "<img src='https://upload.wikimedia.org/wikipedia/commons/5/59/Okonomiyaki_001.jpg' alt='Okonomiyaki' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Mizuno (Dotonbori):",

    # Giorno 14: Kyoto Station -> Katsukura
    "Kyoto+Station,+Kyoto&t=&z=15": "Kyoto+Station,+Kyoto&daddr=Katsukura,+Kyoto+Station&dirflg=w&t=&z=16",
    "<strong>Katsukura (Kyoto Station):": "<img src='https://upload.wikimedia.org/wikipedia/commons/8/86/Tonkatsu_by_t-mizo.jpg' alt='Tonkatsu' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>Katsukura (Kyoto Station):",

    # Giorno 15: Kansai Airport -> 551 Horai
    "Kansai+International+Airport&t=&z=13": "Kansai+International+Airport&daddr=551+Horai,+Kansai+Airport&dirflg=w&t=&z=14",
    "<strong>551 Horai": "<img src='https://upload.wikimedia.org/wikipedia/commons/5/5c/%E3%82%BD%E3%83%BC%E3%82%B9%E3%81%A8%E3%83%9D%E3%83%B3%E9%85%A2%E3%81%AE%E3%81%9F%E3%81%93%E7%84%BC%E3%81%8D.jpg' alt='Takoyaki' style='width:100%; border-radius:8px; margin-bottom:10px; height:150px; object-fit:cover;'><br><strong>551 Horai"
}

for old, new in updates.items():
    if old in html:
        html = html.replace(old, new)
    else:
        print(f"Non trovato per la sostituzione: {old[:50]}")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Aggiornamento completato.")
