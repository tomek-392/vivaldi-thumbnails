import requests
import favicon
from colorthief import ColorThief

icons = favicon.get('https://www.wykop.pl/')

icon = icons[0]

response = requests.get(icon.url, stream=True)
with open('tmp/favicon.{}'.format(icon.format), 'wb') as image:
    for chunk in response.iter_content(1024):
        image.write(chunk)



color_thief = ColorThief('tmp/favicon.png')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
print(dominant_color)
# build a color palette
palette = color_thief.get_palette(color_count=6)
print(palette)