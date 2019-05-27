#! /usr/bin/python3

students = [{'name': 'a'},
            {'name': 'b'}]


def contain(items):
    for s in items:
        if s['name'] == 'c':
            print('找到 %s ' % s['name'])
            break
    else:
        print('没找到')


contain(students)


# Shebbang+解释器路径 指明执行脚本文件的解释器
