
import socket


def demo1(tcp_server):
    service_socket, client_addr =  tcp_server.accept()  # 创建服务socket，服务客户端  返回（socket， addr）
    print(client_addr)
    while True:
        data = service_socket.recv(1024)

        print('收到来自%s的数据：%s' % (client_addr, data.decode('gbk')))
        if not data:
            break
        service_socket.send(('服务器返回的数据：hi，%s' % data.decode('gbk')).encode('gbk'))


def demo2(tcp_server):
    """
    串行循环，为多个客户端服务
    :param tcp_server:
    :return:
    """
    while True:

        service_socket, client_addr =  tcp_server.accept()
        print('%s:%s already connection server....' % client_addr)
        while True:
            recv_data = service_socket.recv(1024)  # 堵塞 ，直到客户端主动关闭
            if not recv_data:  # 有客户端调用close主动关闭
                break
            print('收到客户端的数据：', recv_data.decode('gbk'))
            send_str = ('server return from %s message: %s' % (client_addr,recv_data.decode('gbk'))).encode('gbk')
            service_socket.send(send_str)
        service_socket.close()
        print('finish service...')


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建监听服务器

    tcp_server.bind(('192.168.1.103', 3333))  # 绑定端口
    print('服务器启动...')

    tcp_server.listen(128)  # 监听客户端连接请求

    # service_socket, client_addr =  tcp_server.accept()  # 创建服务socket，服务客户端  返回（socket， addr）
    demo2(tcp_server)

    tcp_server.close()


if __name__ == '__main__':
    main()
