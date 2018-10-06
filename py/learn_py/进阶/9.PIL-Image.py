# -*- coding:utf-8 -*-

import random
from PIL import Image,ImageFont,ImageDraw,ImageFilter

def randFont():
     return chr(random.randint(65,90))

def randColor():
     return (random.randint(99,255),random.randint(99,255),random.randint(99,255))

def randFontColor():
     return (random.randint(45,123),random.randint(45,123),random.randint(45,123))

width = 4 * 60
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype(font=r'D:\python\a\Library\lib\fonts\VeraSe.ttf',size=36)
draw = ImageDraw.Draw(image)

for x in range(width):
     for y in range(height):
          draw.point((x,y),fill=randColor())

for t in range(4):
     code = randFont()
     print(code)
     draw.text((10+t*60,10),text=code,fill=randFontColor(),font=font)

image = image.filter(ImageFilter.BLUR)
image.save(r'c:/users/administrator/desktop/y.jpg')
