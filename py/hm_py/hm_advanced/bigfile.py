"""
查找大于100M的大文件，打印目录树
c盘权限问题，拒绝访问
"""
# coding='utf-8'

import os
import os.path
import shutil
import datetime


def search_file(fpath, depth = 0):
    depth += 1
    fname = fpath
    try:
        if os.listdir(fpath):
            for file in os.listdir(fname):
                fname = os.path.join(fpath, file)
                # print('  ' * depth + '|')
                # print('  ' * depth + '*-' * depth, file)
                if os.path.isdir(fname):
                    print('|  ' * depth + '|')
                    print('|  ' * depth + '*-' * depth, file, '<dir>')                    
                    search_file(fname, depth)
                else:
                    size = os.path.getsize(fname) if (not os.path.isdir(fname)) else ''
                    if  size > 1024 ** 2 * 100:
                        print('  ' * depth, end='！！！')
                        print('【%s>>>%s】 %s M' % (fname, file, size // (1024 ** 2)))
    except Exception as e:
        print(e)
        
 
# size = os.path.getsize(fname) if (not os.path.isdir(fname)) else ''

if __name__ == '__main__':
    search_file(r'D:')
    
# search_file(r'C:\Users')


