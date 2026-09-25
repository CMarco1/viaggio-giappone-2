# Ricomprime le foto del sito e crea le miniature per le card della home.
# Uso (da PowerShell, nella cartella del sito):  powershell -File assets/optimize-images.ps1
# Le foto originali stanno nella storia di git: rilanciarlo su file gia' compressi
# peggiora la qualita', quindi va usato solo su foto nuove.
param([string[]]$Only)

Add-Type -AssemblyName System.Drawing

$heroes = 'airport','akihabara','cover','dotonbori','himeji','ikebukuro','kiyomizu','kyoto_station',
          'nakano','nishiki','odaiba','shibuya','shinjuku','shinsekai','toji','yanaka'

$codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }

function Save-Jpeg($src, $dst, [int]$maxW, [int]$quality, [bool]$cropWide = $false) {
    $img = [System.Drawing.Image]::FromFile($src)
    # Le copertine si vedono come fascia orizzontale centrata: le foto verticali
    # si ritagliano al centro in 3:2, che e' quello che la pagina mostra comunque.
    $sx = 0; $sy = 0; $sw = $img.Width; $sh = $img.Height
    if ($cropWide -and $sh -gt [int]($sw * 2 / 3)) { $sh = [int]($sw * 2 / 3); $sy = [int](($img.Height - $sh) / 2) }
    $w = [Math]::Min($maxW, $sw)
    $h = [int]([Math]::Round($sh * $w / $sw))
    $bmp = New-Object System.Drawing.Bitmap $w, $h
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.DrawImage($img, (New-Object System.Drawing.Rectangle 0, 0, $w, $h), (New-Object System.Drawing.Rectangle $sx, $sy, $sw, $sh), [System.Drawing.GraphicsUnit]::Pixel)
    $img.Dispose()
    $p = New-Object System.Drawing.Imaging.EncoderParameters 1
    $p.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), ([long]$quality)
    $tmp = "$dst.tmp"
    $bmp.Save($tmp, $codec, $p)
    $g.Dispose(); $bmp.Dispose()
    Move-Item -Force $tmp $dst
}

$root = Join-Path $PSScriptRoot '..\images'
New-Item -ItemType Directory -Force (Join-Path $root 'thumbs') | Out-Null

foreach ($n in $heroes) {
    if ($Only -and ($Only -notcontains $n)) { continue }
    $f = Join-Path $root "$n.jpg"
    Save-Jpeg $f (Join-Path $root "thumbs\$n.jpg") 640 66 $true
    Save-Jpeg $f $f 1200 72 $true
}
