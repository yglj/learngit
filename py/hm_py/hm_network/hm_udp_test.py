import socket


def main():
    des_ip = '192.168.1.103'
    des_port = 6667

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建udpSocket
    # 绑定端口,参数是一个元组，如果不绑定端口，系统会自动分配动态端口
    udp_socket.bind(('192.168.1.103', 888))

    while True:
        # send_str = input("请输入：").encode('gbk')  # 编码成能发送的二进制数据
        send_str = 'hhh'.encode('utf-8')
        udp_socket.sendto(send_str, (des_ip, des_port))  # 向目标ip地址的端口发信息
        # print(udp_socket)
        rec_info, rec_ip = udp_socket.recvfrom(1024)  # 一次从端口接收1024字节
        print('[从 %s 收到的数据]:%s' % (rec_ip, rec_info.decode('gbk')))  # 汉字要gbk编码， .recv()调用一次接收一次
        print(udp_socket.recv(1024).decode('gbk'))
        if send_str == 'exit' or rec_info == 'exit':
            break
    try:
        if udp_socket:
            udp_socket.close()  # 关闭
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
