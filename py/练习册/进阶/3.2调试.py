'''
程序会有各种各样的bug需要修正，这需要一整套调试程序的手段来修复bug

第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看
缺点：是将来还得删掉它，运行结果也会包含很多无用信息

第二种方法断言
凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
'''
def test(n):
     assert n != 0,'n value is zero'
     print(9//n,'\nexit')

##test(0)
##test(2)

'''
如果断言失败，assert语句本身就会抛出AssertionError
启动Python解释器时可以用-O参数来关闭assert
关闭后，你可以把所有的assert语句当成pass来看
'''
import logging
logging.basicConfig(level=logging.INFO)

def test1(n):
     logging.info("\n n=%s \n"%n)
     print(8/n)
     print('end')


##test1(0)
'''
第三种方式logging
logging不会抛出错误，而且可以输出到文件
logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
优先级不同
另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方
'''


'''
第四种pdb,启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
pdb.set_trace() 以设置一个断点
# err.py
s = '0'
n = int(s)
print(10 / n)
然后启动：

$ python -m pdb err.py
> /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
-> s = '0'
以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：

(Pdb) l
  1     # err.py
  2  -> s = '0'
  3     n = int(s)
  4     print(10 / n)
输入命令n可以单步执行代码：

(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
-> n = int(s)
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
-> print(10 / n)
任何时候都可以输入命令p 变量名来查看变量：

(Pdb) p s
'0'
(Pdb) p n
0
输入命令q结束调试，退出程序：

(Pdb) q
这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了
'''
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)


#IDE  如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE
