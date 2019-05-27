
import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('192.168.1.103', 666))
    print('connect to server...')

    filename = 'girl'

    client_socket.send( filename.encode('utf-8'))

    rec_data = client_socket.recv(1024 * 1024)

    if rec_data:
        with open(filename + '(download).png', 'wb') as f:
            f.write(rec_data)
            print('ok')

    client_socket.close()


if __name__ == '__main__':
    main()
