#vitualenv就是用来为应用创建一套“隔离”的python的运行环境，
#解决不同应用间多版本冲突问题

#所有的第三方包安装在site-packages目录下

'''
第一步，创建目录：
第二步，创建一个独立的Python运行环境，命名为venv：

命令virtualenv就可以创建一个独立的Python运行环境，
我们还加上了参数--no-site-packages，
这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，
这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境。

virtualenv是如何创建“独立”的Python运行环境的呢？
原理很简单，就是把系统Python复制一份到virtualenv的环境，
用命令source venv/bin/activate进入一个virtualenv环境时，
virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。
'''
