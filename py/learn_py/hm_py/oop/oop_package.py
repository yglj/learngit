# 包是包含多个模块的特殊文件，目录下必须包含__init__.py文件
# 可一次性导入包中所有的模块
# 在__init__中指定对外提供的模块列表

import oop

oop.test.send()

# 发布模块 from distutils.core import setup
# 1.创建setup.py ，调用setup（）  传入详细信息字典参数
# 2.构建模块 python setup.py build
# 3.生成发布压缩包 python setup.py sdist


# 安装模块
# 1.tar解压
# 2.sudo python setup.py install  安装到系统目录

# 卸载模块
# sudo rm -r 模块*

# pip 包管理工具（查找，下载，安装，卸载） 安装第三方模块
#　sudo pip install 包名


