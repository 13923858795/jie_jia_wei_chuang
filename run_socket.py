import socketserver
import time
config = {
    'SOCKET_HOST': '0.0.0.0',
    'SOCKET_PORT': 20000
}


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        self.request.settimeout(5)

    def handle(self):
        while True:
            try:
                self.request.sendall(b'#4@0@4@5!')
                time.sleep(1)
                print("11111")
            except:
                break


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":

    while True:
        try:
            server = ThreadedTCPServer((config['SOCKET_HOST'], config['SOCKET_PORT']), ThreadedTCPRequestHandler)
            # print('starting server on {}:{}.'.format(config['SOCKET_HOST'], str(config['SOCKET_PORT'])))
            server.serve_forever()
        except Exception as e:
            # print('server error\n', str(e))
            pass
        time.sleep(1)
