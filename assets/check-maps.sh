#!/usr/bin/env bash
# check-maps.sh [giorni...] (da lanciare con: bash assets/check-maps.sh 08 10): per ogni giornata scarica l'embed di Google Maps (col cookie di consenso)
# e dice quali tappe Google trova (con le coordinate) e quali no.
cd "$(dirname "$0")/.."
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
CK="SOCS=CAESHAgBEhJnd3NfMjAyNDA1MDEtMF9SQzEaAml0IAEaBgiA_LyxBg; CONSENT=YES+cb"
days="${@:-01 02 03 04 05 06 07 08 09 10 11 12 13 14 15}"
for n in $days; do
  f=giorno-$n.html
  u=$(grep -o 'data-embed="[^"]*"' $f | head -1 | sed 's/data-embed="//;s/"$//;s/&amp;/\&/g')
  [ -z "$u" ] && { echo "G$n: nessuna mappa"; continue; }
  # elenco dei punti come scritti: saddr + daddr separati da +to:
  pts=$(echo "$u" | sed 's/.*saddr=//;s/&daddr=/+to:/;s/&.*//' | sed 's/+to:/\n/g')
  html=$(curl -s -L -A "$UA" -H "Accept-Language: it-IT,it;q=0.9" -b "$CK" "$u")
  # la lista delle coordinate: [[[],[lat,lng],...]] con 1 elemento per punto
  coords=$(echo "$html" | grep -o '\[\[\(\[\]\|\[[0-9.]*,[0-9.]*\]\)\(,\(\[\]\|\[[0-9.]*,[0-9.]*\]\)\)*\]' | grep '13[0-9]\.' | head -1)
  if [ -z "$coords" ]; then echo "G$n: nessuna lista coordinate (risposta anomala, ${#html} byte)"; continue; fi
  items=$(echo "$coords" | sed 's/^\[\[/[/;s/\]\]$/]/' | sed 's/\],\[/]\n[/g')
  ok=1; i=0
  echo "=== G$n ==="
  paste <(echo "$pts") <(echo "$items") | while IFS=$'\t' read -r p c; do
    i=$((i+1)); name=$(printf '%b' "$(echo "$p" | sed 's/+/ /g;s/%\([0-9A-F][0-9A-F]\)/\\x\1/g')")
    if [ "$c" = "[]" ]; then echo "  ✗ NON TROVATO: $name"; else echo "  ✓ $name  $c"; fi
  done
done
