import re

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Definisco sostituzioni massicce: tolgo le Wikimedia problematiche e rimetto Unsplash stabili
# e cambio l'aeroporto con una foto più bella.

replacements = {
    # Shinjuku (Giorno 1)
    "https://upload.wikimedia.org/wikipedia/commons/b/b2/Skyscrapers_of_Shinjuku_2009_January.jpg": "https://images.unsplash.com/photo-1503899036067-8b5cbeca0b53?w=800&q=80",
    
    # Asakusa (Giorno 2)
    "https://upload.wikimedia.org/wikipedia/commons/4/43/Sensoji_2023.jpg": "https://images.unsplash.com/photo-1531737255085-0556f8f7c5e2?w=800&q=80",
    
    # Akihabara (Giorno 3)
    "https://upload.wikimedia.org/wikipedia/commons/6/60/Sotokanda%2C_Akihabara_Electric_Town_at_night_20231114.png": "https://images.unsplash.com/photo-1542931287-023b922fa89b?w=800&q=80",
    
    # Nakano (Giorno 5) - metto una foto generica di Tokyo retro/vintage
    "https://upload.wikimedia.org/wikipedia/commons/3/35/Nakano_broadway_entrance.JPG": "https://images.unsplash.com/photo-1582029785805-4c07c1b714bc?w=800&q=80",
    
    # Ikebukuro (Giorno 6) - metto una foto di strade di tokyo
    "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunshine_60_Observatory_%40_Sunshine_Building_%40_Ikebukuro_%2811547419543%29.jpg": "https://images.unsplash.com/photo-1550456100-33777cb31853?w=800&q=80",
    
    # Odaiba (Giorno 7) 
    "https://upload.wikimedia.org/wikipedia/commons/4/4a/Odaiba_close_up_-_2025_Jan_14_01-27PM.jpeg": "https://images.unsplash.com/photo-1610313175402-98ea322e7033?w=800&q=80",
    
    # Gion (Giorno 8)
    "https://upload.wikimedia.org/wikipedia/commons/2/23/150124_Gion_Kyoto_Japan01s3.jpg": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800&q=80",
    
    # Nishiki Market (Giorno 10)
    "https://upload.wikimedia.org/wikipedia/commons/c/ce/Nishiki_Ichiba_by_matsuyuki.jpg": "https://images.unsplash.com/photo-1570131464434-2e9b9bc8a59c?w=800&q=80",
    
    # Arashiyama (Giorno 11)
    "https://upload.wikimedia.org/wikipedia/commons/c/c2/Arashiyama%2C_Part_II_-_Arashiyama7534.jpg": "https://images.unsplash.com/photo-1473856218684-2b6387bdcb65?w=800&q=80",
    
    # Shinsekai/Tsutenkaku (Giorno 12)
    "https://upload.wikimedia.org/wikipedia/commons/d/d2/New_Tsutenkaku%2C_Osaka.jpg": "https://images.unsplash.com/photo-1590408544933-f54246830501?w=800&q=80",
    
    # Dotonbori (Giorno 13)
    "https://upload.wikimedia.org/wikipedia/commons/f/f4/Osaka_Dotonbori_Ebisu_Bridge.jpg": "https://images.unsplash.com/photo-1590559899731-a389bfc0c8d5?w=800&q=80",
    
    # Kansai Airport (Giorno 15) - Sostituisco con bella immagine di aeroporto/aereo
    "https://upload.wikimedia.org/wikipedia/commons/5/56/%E9%96%A2%E8%A5%BF%E5%9B%BD%E9%9A%9B%E7%A9%BA%E6%B8%AF%E5%85%A8%E4%BD%93%E5%86%99%E7%9C%9F20220811.jpg": "https://images.unsplash.com/photo-1542296332-2e4473faf563?w=800&q=80",
    
    
    # === CIBO ===
    # Tsukemen
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Tsukemen_at_a_Tokyo_restaurant.jpg": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=500&q=80",
    # Melonpan
    "https://upload.wikimedia.org/wikipedia/commons/a/a0/Melonpan_on_the_plastic_bag.jpg": "https://images.unsplash.com/photo-1622359483015-80ab462debc6?w=500&q=80",
    # Katsu Curry
    "https://upload.wikimedia.org/wikipedia/commons/c/cc/%E3%81%A8%E3%82%93%E3%81%8B%E3%82%89%E4%BA%AD_%E6%AD%A6%E8%94%B5%E9%87%8E%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%81%8B%E3%81%A4%E3%82%AB%E3%83%AC%E3%83%BC_-_1.jpg": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=500&q=80",
    # Crepe
    "https://upload.wikimedia.org/wikipedia/commons/9/9c/Crepes_stand_in_Harajuku.jpg": "https://images.unsplash.com/photo-1519676867240-f03562e64548?w=500&q=80",
    # Chuka Soba
    "https://upload.wikimedia.org/wikipedia/commons/2/29/Chuka-soba.jpg": "https://images.unsplash.com/photo-1558862107-d49ef2a04d72?w=500&q=80",
    # Taiyaki
    "https://upload.wikimedia.org/wikipedia/commons/8/8e/Taiyaki_003.jpg": "https://images.unsplash.com/photo-1515442596856-d6674c9e88d1?w=500&q=80",
    # Tempura
    "https://upload.wikimedia.org/wikipedia/commons/2/2e/Tempura_01.jpg": "https://images.unsplash.com/photo-1615361200141-f45040f367be?w=500&q=80",
    # Matcha Parfait
    "https://upload.wikimedia.org/wikipedia/commons/f/ff/Maccha_parfait.jpg": "https://images.unsplash.com/photo-1572451378875-103399bb4a20?w=500&q=80",
    # Silky Tofu
    "https://upload.wikimedia.org/wikipedia/commons/0/03/Japanese_SilkyTofu_%28Kinugoshi_Tofu%29.JPG": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500&q=80",
    # Tako tamago / Takoyaki
    "https://upload.wikimedia.org/wikipedia/commons/4/4b/Tako_tamago.jpg": "https://images.unsplash.com/photo-1626202165039-44fb6b931dc9?w=500&q=80",
    # Soba
    "https://upload.wikimedia.org/wikipedia/commons/f/ff/Zarusoba.jpg": "https://images.unsplash.com/photo-1517435128080-d6cd20e060ea?w=500&q=80",
    # Kushikatsu
    "https://upload.wikimedia.org/wikipedia/commons/f/f4/KushikatsuDaruma01.jpg": "https://images.unsplash.com/photo-1599818816692-28df529d10e0?w=500&q=80",
    # Okonomiyaki
    "https://upload.wikimedia.org/wikipedia/commons/5/59/Okonomiyaki_001.jpg": "https://images.unsplash.com/photo-1634591460592-8dbbc97576f3?w=500&q=80",
    # Tonkatsu
    "https://upload.wikimedia.org/wikipedia/commons/9/93/%22Amai-Yuwaku%22_Special_Loin_Pork_Cutlet1.jpg": "https://images.unsplash.com/photo-1598514982205-f36b96d1e8dd?w=500&q=80",
    # Nikuman
    "https://upload.wikimedia.org/wikipedia/commons/3/36/Steamed_Meat_Dumpling_551_Horai_001.jpg": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=500&q=80"
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
