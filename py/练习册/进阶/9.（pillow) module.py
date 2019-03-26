'''
pyc文件介绍

pyc文件，是python编译后的字节码（bytecode）文件。
只要你运行了py文件，python编译器就会自动生成一个对应的pyc字节码文件。
这个pyc字节码文件，经过python解释器，会生成机器码运行（这也是为什么pyc文件可以跨平台部署，类似于java的跨平台，java中JVM运行的字节码文件）。
下次调用直接调用pyc，而不调用py文件。直到你这个py文件有改变。python解释器会检查pyc文件中的生成时间，对比py文件的修改时间，如果py更新，那么就生成新的pyc。
'''

#PIL Python Imaging Library 图像处理标准库 兼容版本Pillow
from PIL import Image


#缩放图像
img = Image.open(r'C:/users/administrator/desktop/1.png')
w,h = img.size
print(f'width:{w},height:{h}')
img.thumbnail((w//2,h//2))
img.save(r'C:/users/administrator/desktop/1.png')

