# Crea le versioni leggere di una foto nuova per il sito.
# Uso:  powershell -NoProfile -ExecutionPolicy Bypass -File assets/make-images.ps1 -Src <foto> -Name <nome> -Kind stop|food|shop
#   stop -> images/stops/<nome>.jpg (800x533, per la galleria) + images/stops/t/<nome>.jpg (160x160, miniatura della tappa)
#   food -> images/food/<nome>.jpg  (360x270, miniatura del piatto)
#   shop -> images/shop/<nome>.jpg  (640x427, esempio nello Shopping)
# Tutte ritagliate al centro nella proporzione giusta. -CropY sposta il ritaglio in verticale (0 = alto, 0.5 = centro, 1 = basso).
param(
    [Parameter(Mandatory = $true)][string]$Src,
    [Parameter(Mandatory = $true)][string]$Name,
    [Parameter(Mandatory = $true)][ValidateSet('stop', 'food', 'shop')][string]$Kind,
    [double]$CropY = 0.5
)
Add-Type -AssemblyName System.Drawing
$codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$root = Join-Path $PSScriptRoot '..\images'

function Save-Crop([string]$src, [string]$dst, [int]$w, [int]$h, [int]$quality, [double]$cropY) {
    $img = [System.Drawing.Image]::FromFile((Resolve-Path $src))
    $target = $w / $h
    $sw = $img.Width; $sh = $img.Height; $sx = 0; $sy = 0
    if ($sw / $sh -gt $target) { $nw = [int]($sh * $target); $sx = [int](($sw - $nw) / 2); $sw = $nw }
    else { $nh = [int]($sw / $target); $sy = [int](($sh - $nh) * $cropY); $sh = $nh }
    $bmp = New-Object System.Drawing.Bitmap $w, $h
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.DrawImage($img, (New-Object System.Drawing.Rectangle 0, 0, $w, $h), (New-Object System.Drawing.Rectangle $sx, $sy, $sw, $sh), [System.Drawing.GraphicsUnit]::Pixel)
    $img.Dispose()
    $p = New-Object System.Drawing.Imaging.EncoderParameters 1
    $p.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter ([System.Drawing.Imaging.Encoder]::Quality), ([long]$quality)
    New-Item -ItemType Directory -Force (Split-Path $dst) | Out-Null
    $bmp.Save("$dst.tmp", $codec, $p)
    $g.Dispose(); $bmp.Dispose()
    Move-Item -Force "$dst.tmp" $dst
}

switch ($Kind) {
    'stop' {
        Save-Crop $Src (Join-Path $root "stops\$Name.jpg") 800 533 60 $CropY
        Save-Crop $Src (Join-Path $root "stops\t\$Name.jpg") 160 160 70 $CropY
    }
    'food' { Save-Crop $Src (Join-Path $root "food\$Name.jpg") 360 270 70 $CropY }
    'shop' { Save-Crop $Src (Join-Path $root "shop\$Name.jpg") 640 427 70 $CropY }
}
Write-Output "ok $Kind $Name"
