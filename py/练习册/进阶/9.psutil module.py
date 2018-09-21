#用python编写脚本简化运维工作是python的一个重要用途


#第三方模块psutil(process and system utilities) 可以通过一两行代码进行系统监控
import psutil

'''
#获取cpu信息
print('cpu逻辑数：:',psutil.cpu_count()) #cpu逻辑数量
print(psutil.cpu_count(logical=False))  #cpu物理核心 # 2说明是双核超线程, 4则是4核非超线程
print(psutil.cpu_times()) #统计cpu用户/系统/空闲时间
#再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
##for x in range(10):
##     print(psutil.cpu_percent(interval=1,percpu=True))
#获取内存信息
print(psutil.virtual_memory())#物理内存和交换内存信息
print(psutil.swap_memory())   #返回字节单位的整数

#获取磁盘信息
print(psutil.disk_partitions()) #磁盘分区信息 fstype='NTFS', opts='rw,fixed'
print(psutil.disk_usage('/'))  #磁盘使用情况
print(psutil.disk_io_counters()) #磁盘io
'''
#获取网络信息
'''
print(psutil.net_io_counters())     #获取网络读写字节/包的个数
print(psutil.net_if_addrs())         #获取网络接口
print(psutil.net_if_stats())      #获取网络接口状态
print(psutil.net_connections())  #获取当前连接信息
'''
#获取进程信息
import os
#print(psutil.test())  #模拟ps命令
#print(psutil.pids())
print(os.getpid())
pids = psutil.pids()
p = psutil.Process(os.getpid())
print('名称-->',p.name())
print('exe路径-->',p.exe())
print('工作目录-->',p.cwd())
print('启动命令行-->',p.cmdline())
print('父进程id-->',p.ppid())
print('父进程-->',p.parent())
print('状态-->',p.status())
print('用户名-->',p.username())
print('创建时间-->',p.create_time())
#print('终端-->,', p.terminal())
print('使用cpu时间-->',p.cpu_times())
print('使用内存-->',p.memory_info())
print('打开的文件-->',p.open_files())
print('相关的网络连接-->',p.connections())
print('线程的数量-->',p.num_threads())
print('所有线程信息-->',p.threads())
print('环境变量-->',p.environ())
#print('结束进程-->',p.terminate())
#psutil 能轻松获取系统信息，还可以获取用户信息，windows服务等有用系统信息

