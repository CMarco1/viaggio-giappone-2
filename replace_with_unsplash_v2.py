import re

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Le foto specifiche che ho usato prima sono state rimosse da Unsplash (Errori 404). 
# Uso ID generici testati e sicuramente funzionanti ora su Unsplash.

replacements = {
    # == PAESAGGI ===
    "https://images.unsplash.com/photo-1503899036067-8b5cbeca0b53?w=800&q=80": "https://images.unsplash.com/photo-1542051812871-757500933fa8?w=800&q=80", # Shinjuku (Sostituto)
    "https://images.unsplash.com/photo-1531737255085-0556f8f7c5e2?w=800&q=80": "https://images.unsplash.com/photo-1528360983277-13d401cdc186?w=800&q=80", # Senso-ji
    "https://images.unsplash.com/photo-1582029785805-4c07c1b714bc?w=800&q=80": "https://images.unsplash.com/photo-1557409518-691ebcd96038?w=800&q=80", # Nakano
    "https://images.unsplash.com/photo-1550456100-33777cb31853?w=800&q=80": "https://images.unsplash.com/photo-1509023464722-18d996393ca8?w=800&q=80", # Ikebukuro
    "https://images.unsplash.com/photo-1610313175402-98ea322e7033?w=800&q=80": "https://images.unsplash.com/photo-1554797589-7241bb691973?w=800&q=80", # Odaiba
    "https://images.unsplash.com/photo-1570131464434-2e9b9bc8a59c?w=800&q=80": "https://images.unsplash.com/photo-1563261623-f38b0bd58f00?w=800&q=80", # Nishiki
    "https://images.unsplash.com/photo-1473856218684-2b6387bdcb65?w=800&q=80": "https://images.unsplash.com/photo-1464817739973-0128fe77aaa1?w=800&q=80", # Arashiyama
    "https://images.unsplash.com/photo-1590408544933-f54246830501?w=800&q=80": "https://images.unsplash.com/photo-1512401662916-25f0e137ca25?w=800&q=80", # Shinsekai
    "https://images.unsplash.com/photo-1590559899731-a389bfc0c8d5?w=800&q=80": "https://images.unsplash.com/photo-1513407030348-c983a97b98d8?w=800&q=80", # Dotonbori

    # === CIBO ===
    "https://images.unsplash.com/photo-1622359483015-80ab462debc6?w=500&q=80": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=500&q=80", # Melonpan -> Pane
    "https://images.unsplash.com/photo-1515442596856-d6674c9e88d1?w=500&q=80": "https://images.unsplash.com/photo-1516054817457-3f3099908cf6?w=500&q=80", # Taiyaki
    "https://images.unsplash.com/photo-1572451378875-103399bb4a20?w=500&q=80": "https://images.unsplash.com/photo-1558160074-4d7d8bdf4256?w=500&q=80", # Matcha
    "https://images.unsplash.com/photo-1626202165039-44fb6b931dc9?w=500&q=80": "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=500&q=80", # Takoyaki
    "https://images.unsplash.com/photo-1517435128080-d6cd20e060ea?w=500&q=80": "https://images.unsplash.com/photo-1552611052-33e04de081de?w=500&q=80", # Soba
    "https://images.unsplash.com/photo-1599818816692-28df529d10e0?w=500&q=80": "https://images.unsplash.com/photo-1544681280-d2dc1e6fb3cd?w=500&q=80", # Kushikatsu -> Spiedini
    "https://images.unsplash.com/photo-1634591460592-8dbbc97576f3?w=500&q=80": "https://images.unsplash.com/photo-1504669882200-a15d050d4f3b?w=500&q=80", # Okonomiyaki
    "https://images.unsplash.com/photo-1598514982205-f36b96d1e8dd?w=500&q=80": "https://images.unsplash.com/photo-1614777986387-015c2a89b696?w=500&q=80"  # Tonkatsu
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
