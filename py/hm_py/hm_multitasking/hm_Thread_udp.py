
import socket
import threading


def rec_msg(udp_socket):
    while True:
        rec_data = udp_socket.recvfrom(1024)
        print('\n收到的数据：%s--%s' % rec_data)


def send(udp_socket):
    ip = '192.168.1.107'
    port = 8888
    while True:
        send_str = input('要发送的数据：')
        udp_socket.sendto(send_str.encode('gbk'), (ip, port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('192.168.1.107', 2222))
    send_thread = threading.Thread(target=send, args=(udp_socket,))
    rec_thread = threading.Thread(target=rec_msg, args=(udp_socket,))
    send_thread.start()
    rec_thread.start()
    rec_thread.join()
    send_thread.join()
    udp_socket.close()


if __name__ == '__main__':
    main()
