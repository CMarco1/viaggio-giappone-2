import re
import urllib.request
import time
import os

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
img_dir = "/home/jupyter/giappone/viaggio-giappone-2/images"

# Ripristino i link originari per sicurezza rileggendo da git se si è incasinato, ma non lo faccio qua, 
# faccio checkout e rileggo
