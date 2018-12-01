# coding:utf-8

import socket


def handler_socket(service_socket):
    recv_data = service_socket.recv(1024)
    data_lines = recv_data.splitlines()
    for line in data_lines:
        print(line)

    response_header = "HTTP/1.1 200 OK\r\n"  #r'HTTP/1.1  200 ok \r\n'
    response_header += '\r\n'
    response_body = "hello,world?"

    response = response_header + response_body
    service_socket.send(response.encode('utf-8'))
    service_socket.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 7788))
    # 设置服务端关闭时，4次挥手（tcp连接释放）后立即释放资源，保证端口的复用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.listen(128)
    while True:
        service, address = sock.accept()
        handler_socket(service)


if __name__ == '__main__':
    main()
