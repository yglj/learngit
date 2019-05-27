
import socket


def send_file(service_socket, file):
    try:
        with open(file + '.jpg', 'rb') as f:
            content = f.read()
        if content:
            service_socket.send(content)
    except FileNotFoundError:
        service_socket.send('文件不存在'.encode('utf-8'))
    else:
        print('send successful')


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server.bind(('192.168.1.103', 666))

    print('server open...')

    tcp_server.listen(128)

    service_socket, client_addr = tcp_server.accept()
    print('already connection from %s:%s ...' % client_addr)

    while True:
        # print(client_addr)

        req_data = service_socket.recv(1024).decode('utf-8')

        if not req_data:
            # print('?' + req_data)
            break

        print('client request download <<< %s' % req_data)

        send_file(service_socket, req_data)

    tcp_server.close()
    print('server close')


if __name__ == '__main__':
    main()
