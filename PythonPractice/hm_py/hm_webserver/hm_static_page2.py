import socket
import re
import multiprocessing
import threading
import gevent
from gevent import monkey

monkey.patch_all()


def service_client(socket):
    print('定位')
    # recvice client data
    client_data = socket.recv(1024)
    request_lines = client_data.splitlines()
    for line in request_lines:
        print(line)
    print('*' * 50)

    # get request url
    request_path = re.match(r'[^/]+(/[^ ]*)', request_lines[0].decode('utf-8'))
    if request_path:
        request_path = request_path.group(1)
        if request_path == '/':
            request_path = request_path + 'index.html'
        print('==========>>>>>>>>>>', request_path)

    # from index open html
    html_content = None
    try:
        request_path = './html' + request_path
        print(request_path)
        with open(request_path, 'rb') as f:
            html_content = f.read()
    except:
        response_headers = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        response_body = '----- not have the page -----'
        socket.send(response_headers.encode('utf-8'))
        socket.send(response_body.encode('utf-8'))
    else:
        response_headers = 'HTTP/1.1 200 ok \r\n\r\n'
        socket.send(response_headers.encode('utf-8'))
        socket.send(html_content)

    print('xxxx' * 10)
    socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(('', 4567))

    server.listen(128)

    print('服务器运行......')
    while True:
        service_socket, client_address = server.accept()

        # service_client(service_socket)

        # 多进程 fd 文件描述符，一个数字，对应一个特殊的文件，例如网络接口
        '''
        service_process = multiprocessing.Process(target=service_client, args=(service_socket,))
        service_process.start()
        service_socket.close()  # 子进程已复制fd，删除主进程的引用
        '''
        # 多进程
        '''
        service_thread = threading.Thread(target=service_client, args=(service_socket,))
        service_thread.start()
        service_thread.join()
        print('one socket already close!')
        '''
        # 协程
        gevent.spawn(service_client, service_socket)


if __name__ == '__main__':
    main()
