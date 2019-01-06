import socket
import multiprocessing
import re
# from mini_web.dynamic import mini_frame
import sys


class WSGIServer:
    def __init__(self, port, application, static_path):
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind(('', port))
        self.listen_sock.listen(128)
        self.application = application
        self.static_path = static_path

    def response_client(self, new_socket):
        request_data = new_socket.recv(1024).decode('utf-8')
        req_lines = request_data.splitlines()
        # for line in req_lines:
        #     print(line)
        if not req_lines:
            return
        print('+' * 50)
        print(req_lines[0])
        # page = '../hm_webserver/html'
        page = self.static_path
        path = re.match('[^/]+(/[^ ]*)', req_lines[0]).group(1)
        if path:
            if path == '/':
                page += '/index.html'
            else:
                page += path

        response_body = ''
        response_head = ''
        try:
            if not page.endswith('.html'):
                print('客户端请求的页面->%s' % page)
                print('*'*50, end='\n\n')
                with open(page, 'rb') as f:
                    response_body = f.read()
                response_head = 'HTTP/1.1 200 OK \r\n\r\n'
            else:
                # response_head += 'HTTP/1.1 200 OK\r\n\r\n'
                # response_body = mini_frame.application(path).encode('gbk')
                # print(response_body.decode('utf-8'))
                env = dict()  # web服务器传递给web框架的数据，实现动态处理请求资源
                env['PATH'] = path
                response_body = self.application(env, self.set_response_headers)
                response_head = 'HTTP/1.1 %s \r\n' % self.status
                for head in self.headers:
                    response_head += '%s: %s \r\n' % head
                response_head += '\r\n'
        except:
            response_head = 'HTTP/1.1 404 NOT FOUND \r\n\r\n'
            response_body = 'ni shi mo gui ma 服务器异常：找不到相关资源'
        if not isinstance(response_body, bytes):
            response_body = response_body.encode('utf-8')
        # print(response_head, response_body)
        response_data = response_head.encode('utf-8') + response_body
        new_socket.send(response_data)
        new_socket.close()

    def set_response_headers(self, status, headers):
        self.status = status
        self.headers = headers
        self.headers.append(('server', 'mini_web'))

    def run_forever(self):
        while True:
            new_socket, address = self.listen_sock.accept()
            process = multiprocessing.Process(target=self.response_client, args=(new_socket,))
            process.start()
            new_socket.close()


def main():
    # 运行web服务器时指定端口及框架
    if len(sys.argv) == 3:
        web_frame = ''
        port = ''
        try:
            port = int(sys.argv[1])
            web_frame = sys.argv[2]
        except Exception as ret:
            print('参数错误!')
    else:
        print('请按照...')
        return

    with open('./profile.conf') as f:
        conf = eval(f.read())

    sys.path.append(conf['dynamic_path'])

    frame, app_func = web_frame.split(':')
    frame = __import__(frame)
    app_func = getattr(frame, app_func)

    # print(port, app_func)
    service = WSGIServer(port, app_func, conf['static_path'])
    service.run_forever()


if __name__ == '__main__':
    main()


