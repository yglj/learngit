import os
import pyecharts
from pyecharts import WordCloud
from pyecharts import Bar,Pie,Line

def gen_cloud(x, y, label):
     cloud = WordCloud(width=1000, height=600)
     cloud.add(label, x, y, word_size_range=[20, 60], shape="triangle-forward")
     cloud.render()
     os.system(r"render.html")

x = ["黄瓜", "一行白鹭", "嘤嘤嘤",
     "", "e", "f",
     "h", "j", "kc"
     ]
y = [1, 10, 100, 1000, 5, 45, 245, 555, 909]
label = "english"
gen_cloud(x, y, label)


def get_charts(x, y, label, type):
     if type == 1:
          tu = Bar("条形图")
     elif type == 2:
          tu = Line("折线图")
     elif type == 3:
          tu = Pie("饼状图")

     tu.add(label, x, y, is_more_utils=True)
     tu.render()
     os.system(r"render.html")


x = ['白丝', '黑丝', '蕾丝', '花边', '豆芽菜', '老黄瓜']
y = [5, 20, 36, 10, 75, 90]
label = "xxx"
get_charts(x, y, label, 1)
get_charts(x, y, label, 2)
get_charts(x, y, label, 3)
