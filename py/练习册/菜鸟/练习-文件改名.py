# codeing=utf-8
import os

import shutil

d =  'C:\\Users\\Administrator\\Desktop\\python\\py\\'

for i in os.listdir(d):
    new_file = i.replace('test','0')
    old_full_file = d + '\\' + i
    new_full_file = d + '\\' + new_file
    shutil.move(old_full_file,new_full_file)
print("done!")
