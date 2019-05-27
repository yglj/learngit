"""
模拟一个聊天室
"""

import socket


def man():
    print('-' * 30)
    print('欢迎来到xxx聊天室')
    print('1.发送消息')
    print('2.接收消息')
    print('0.退出')
    print('-' * 30)


def send_msg(udp_socket):
    # ip = input('目标ip：')
    # port = input('目标port：')
    ip = '192.168.1.103'
    port = 6666
    msg_str = input('发送的数据：')
    udp_socket.sendto(msg_str.encode('utf-8'), (ip, port))


def recv_msg(udp_socket):
    data = udp_socket.recvfrom(1024)
    print('%s:%s' % (data[1], data[0].decode('gbk')))


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('192.168.1.103', 7777))
    # print(s)
    while True:
        man()
        inp = input('选择功能：')
        if inp == '1':
            send_msg(s)
        elif inp == '2':
            recv_msg(s)
        elif inp == '0':
            break
        else:
            print('选择错误，请重新选择!')
    s.close()


if __name__ == '__main__':
    main()
