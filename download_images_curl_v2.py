import re
import subprocess
import time
import os

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Ripristiniamo la logica: rileggiamo i file dal vecchio file o scarichiamo con un User-Agent "normale"
# Il problema è che Wikimedia blocca proprio curl/python. Devo mascherarlo perfettamente o estrarre l'URL da Unsplash.
