import requests
import favicon
import tldextract
from colorthief import ColorThief
from PIL import Image, ImageDraw, ImageFont

from pathlib import Path
Path("tmp").mkdir(exist_ok=True)

# get/set some initial params
url = 'http://google.com'
domain = tldextract.extract(url).domain
caption = domain.capitalize()
width = 440
height = 360
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'}

# set font and fontsize
font = ImageFont.truetype("fonts/OpenSans-Bold.ttf", size=40)

# get favicons and select biggest one
icons = favicon.get(url, headers=headers)
icon = icons[0]

# download and save favicon
response = requests.get(icon.url, headers=headers, stream=True)
with open(f'tmp/{domain}.{icon.format}', 'wb') as image:
    for chunk in response.iter_content(1024):
        image.write(chunk)

# get the dominant color
color_thief = ColorThief(f'tmp/{domain}.{icon.format}')
dominant_color = color_thief.get_color(quality=1)

# build a color palette
palette = color_thief.get_palette(color_count=6)

# create image with dominant color
img = Image.new('RGB', (width, height), color=(dominant_color))
imgDraw = ImageDraw.Draw(img)

# get textbox size
textbox = imgDraw.textbbox((0, 0), text = caption, font = font)
textWidth = textbox[2] - textbox[0]
textHeight = textbox[3] - textbox[1]

# get image center (with offsets) for text placement
xText = (width - textWidth) / 2
yText = (height - textHeight) / 2

# create text and place it on image
imgDraw.text((xText, yText), caption, font=font, fill=(255, 255, 255))

# finally save
img.save(f'tmp/{domain}.png')