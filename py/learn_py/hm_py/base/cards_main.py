#! /usr/bin/python3
# -*-  coding=utf-8 -*-


from cards_tools import *


uuid = 0
while True:

    show_menu()
    action_str = input('请输入你的选择(1/2/3/0)：')
    print('你选择的是：【%s】' % action_str)

    if action_str in ['1', '2', '3']:
        # 选择操作
        if action_str == '1':
            # 新增
            new_role(uuid)
            uuid += 1

        elif action_str == '2':
            # 搜索
            name = input('请输入搜索的名字：')
            find_role(name)

        elif action_str == '3':
            # 显示全部
            show_all()

    elif action_str == '0':
        # 退出
        print('已退出系统')
        break

    else:
        print('选择不符合规定，请重新输入')