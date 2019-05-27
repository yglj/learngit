"""
实现长连接 http/1.1
短连接
"""
import socket
import re
import time


def handler_request(service_socket,request_data):
    data_lines = request_data.splitlines()
    for line in data_lines:
        # print(line)
        pass
    print('-' * 50)

    request_path = re.match(r'[^/]+(/[^ ]*)', data_lines[0].decode('utf-8'))
    # print('---->>>>', request_path)
    if request_path:
        request_path = request_path.group(1)
        if request_path == '/':
            request_path += 'index.html'

    request_path = './html' + request_path
    try:
        content_html = b''
        print(request_path)
        with open(request_path, 'rb') as f:
            content_html = f.read()
    except:
        response_headers = 'HTTP/1.1 404 not found \r\n\r\n'
        content_html = b'<h1>are you monkey?</h1>'
    else:
        response_headers = 'HTTP/1.1 200 ok \r\n'
        response_headers += 'Content-Length: %d \r\n\r\n' % len(content_html)

    # print(content_html)
    service_socket.send(response_headers.encode('utf-8'))
    service_socket.send(content_html)
    print('+' * 50)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 8866))
    server.listen(128)
    server.setblocking(False)
    client_socket_list = []
    print('服务器开始监听...')
    while True:
        time.sleep(1)
        try:
            new_socket, client_address = server.accept()
            print(client_address)
        except Exception as e:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        print('有%s个client连接' % len(client_socket_list))
        for client in client_socket_list:
            print(client.getpeername())
            try:
                request_data = client.recv(1024)
            except Exception as e:
                pass
            else:
                if request_data:
                    handler_request(client, request_data)
                else:
                    print('【%s】 已关闭' % client)
                    client.close()
                    client_socket_list.remove(client)
    # server.close()


if __name__ == '__main__':
    main()
