import os
import glob
import imghdr

img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"
images = glob.glob(os.path.join(img_dir, "*.*"))

broken = []
for img in images:
    if "checkpoint" in img: continue
    
    # Controlla la grandezza
    size = os.path.getsize(img)
    if size < 1000:
        broken.append(f"{os.path.basename(img)}: Troppo piccola ({size} bytes)")
        continue
        
    # Controlla se è davvero un'immagine
    img_type = imghdr.what(img)
    if img_type is None:
        broken.append(f"{os.path.basename(img)}: Non sembra essere un file immagine valido")

if not broken:
    print(f"Tutte le {len(images)} immagini locali sono state verificate e sono valide!")
else:
    print("ATTENZIONE, trovati file corrotti o non validi:")
    for b in broken:
        print(b)
