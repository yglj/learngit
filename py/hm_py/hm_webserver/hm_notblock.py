"""
单进程，单线程，下实现非堵塞并发服务器
"""
import socket
import time


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 3344))
    server.listen(128)
    server.setblocking(False)  # 设为不堵塞
    client_socket_list = []
    while True:
        time.sleep(2)
        try:
            new_socket, client_address = server.accept()  # 堵塞
        except Exception as e:
            print('没有客户端连接...')
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
            print('已连上客户端【%s:%s】' % client_address)

        print('有%s个client连接' % len(client_socket_list))
        for client in client_socket_list:
            try:
                client_data = client.recv(1024)  # 堵塞
            except Exception as e:
                # print(e)
                print('没有收到客户端的数据,等待中...')
            else:
                if client_data:
                    print('收到客户端%s的数据---->%s' % (client.getpeername(), client_data))
                else:
                    client.close()
                    client_socket_list.remove(client)
                    print('关闭客户端【%s】' % client)


if __name__ == '__main__':
    main()
