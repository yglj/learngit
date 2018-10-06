# -*- coding: utf-8 -*-
#PIL Python Imaging Library 图像处理标准库 兼容版本Pillow
from PIL import Image


#缩放图像
##img = Image.open(r'C:/users/administrator/desktop/1.png')
##w,h = img.size
##print(f'width:{w},height:{h}')
##img.thumbnail((w//2,h//2)) #长，宽缩小一半
##img.save(r'C:/users/administrator/desktop/3.png')

##from PIL import ImageFilter
##img = Image.open(r'C:/users/administrator/desktop/4.jpg')
##img.filter(ImageFilter.BLUR)  #使用模糊滤镜
##img.save(r'C:/users/administrator/desktop/4blur.jpg','jpeg')

#字母验证图片(生成验证码)


from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

def rndChar():
     return chr(random.randint(65,90))

def rndColor():  #填充色 rgb
     return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2(): #字体色
     return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 4*60  #4个字符
height = 60
image = Image.new('RGB',(width,height),(255,255,255))  #白色底图
draw = ImageDraw.Draw(image)
for x in range(width):
     for y in range(height):
          draw.point((x,y),fill=rndColor()) #每一点随机填充颜色
font = ImageFont.truetype(r'D:\python\a\Library\lib\fonts\Vera.ttf',36) #无法定位，提供系统绝对资源
for i in range(4):
     draw.text(( 60*i+10 , 10),rndChar(),font=font,fill=rndColor2())

#模糊
image = image.filter(ImageFilter.BLUR)
image.save(r'C:/users/administrator/desktop/code2.jpg','jpeg')
#PIL提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理。

