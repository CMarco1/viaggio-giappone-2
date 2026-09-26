#!/usr/bin/env bash
# Rigenera la parte automatica di images/CREDITS.md dai file images/credits/*.tsv.
# Uso (dalla root del repo):  bash assets/build-credits.sh
# I TSV hanno le colonne: slug, file_commons, autore, licenza, url, note.
# Le righe senza licenza (foto già presenti nel sito, tappe senza foto) non vengono elencate.
set -e
cd "$(dirname "$0")/.."
OUT=images/CREDITS.md
MARK='<!-- CREDITI-TSV: da qui in giù il testo è generato da assets/build-credits.sh -->'
head_part=$(awk -v m="$MARK" '$0 == m { exit } { print }' "$OUT")
{
  printf '%s\n%s\n' "$head_part" "$MARK"
  section() { # $1 titolo, $2 cartella delle immagini, $3... file TSV (righe tenute solo se la foto esiste in quella cartella)
    local title="$1" dir="$2"; shift 2
    printf '\n## %s\n\n| File | Autore | Licenza | Originale |\n|---|---|---|---|\n' "$title"
    for f in "$@"; do
      [ -f "$f" ] || continue
      awk -F'\t' -v d="$dir" 'NR > 1 && $4 != "" && system("test -f images/" d "/" $1 ".jpg") == 0 {
        a = $3; gsub(/\|/, "/", a)
        src = ($5 ~ /wikimedia\.org/) ? "Commons" : "Originale"
        printf "| `%s/%s.jpg` | %s | %s | [%s](%s) |\n", d, $1, a, $4, src, $5
      }' "$f"
    done
  }
  section "Tappe: miniature e gallerie (images/stops, images/stops/t)" "stops" images/credits/stops-*.tsv images/credits/extra-*.tsv
  section "Piatti (images/food)" "food" images/credits/food.tsv images/credits/extra-*.tsv
  section "Shopping (images/shop)" "shop" images/credits/shop.tsv
  printf '\nTutte ritagliate e ridimensionate con `assets/make-images.ps1`. Le miniature in `images/stops/t` hanno gli stessi crediti della foto in `images/stops`.\n'
} > "$OUT.tmp"
mv "$OUT.tmp" "$OUT"
echo "CREDITS.md: $(grep -c '^| `' "$OUT") righe generate"
