
import socket


def main():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建连接
    server_ip = '192.168.1.103'
    server_port = 12345
    tcp_client.connect((server_ip, server_port))  # 连接服务器
    print('客户端连接服务器%s...' % server_ip)
    tcp_client.send('你好，未来'.encode('gbk'))

    data = tcp_client.recv(1024)
    print('来自server:%s' % (data.decode('gbk')))

    tcp_client.close()


if __name__ == '__main__':
    main()
