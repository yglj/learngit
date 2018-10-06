#! /usr/bin/python3
# -*-  coding=utf-8 -*-

role_list = []


def show_menu():
    """
    显示菜单
    :return:
    """
    print('*' * 30)
    print('欢迎进入卡片管理系统')
    print('1.新增信息')
    print('2.搜索信息')
    print('3.显示全部')
    print('0.退出')
    print('*' * 30)


def new_role(i):
    """
    新增信息
    :return:
    """
    print('-' * 30)
    role = {'id': i, 'name': input('名字：'), 'job': input('职业：'), 'work': input('作用：')}
    i += 1
    role_list.append(role)
    print('增加成功')


def find_role(find_name):
    """
    搜索信息
    :param find_name:name
    :return:
    """
    print('-' * 30)
    for role in role_list:
        if role['name'] == find_name:
            print(role)
            break
    else:
        print('未找到相关信息')


def show_all():
    """
    显示信息
    :return:
    """
    if not role_list:
        print('暂无信息')
        return
    print('=' * 30)
    print('全部信息'.center(30))
    print('序号\t\t姓名\t\t职业\t\t作用\t\t')
    for role in role_list:
        print('{}\t\t{}\t\t{}\t\t{}\t\t'.format(role['id'], role['name'], role['job'], role['work']))
    deal_role()


def deal_role():
    """
    修改/删除信息
    :return:
    """
    enter = input('是否要修改/删除？（1.修改,2.删除,按回车退出操作):')
    if len(enter) > 0:
        while True:
            id_str = input('请选择要修改的id：')
            if enter == '1':
                role = role_list[int(id_str)]
                for k in role:
                    if k == 'id':
                        continue
                    info = input(k + ':')
                    if len(info) > 0:
                        role[k] = info
                print('修改成功')
                return

            elif enter == '2':
                role_list.pop(int(id_str) - 1)
                print('删除成功')
                return

            else:
                print('选择错误，请重新输入')
    else:
        return