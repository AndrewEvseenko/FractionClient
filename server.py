import socket
import threading


def tcp_listener(server_inst):
    while server_inst.started:
        data = server_inst.connection.recv(1024)
        if data:
            for handle in server_inst.handlers:
                handle(data)


class Server:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handlers = []
        self.started = False

    def start(self, handler, port, ip="127.0.0.1", connections=30):
        self.sock.bind(ip, port)
        self.sock.listen(connections)
        conn, addr = self.sock.accept()
        self.connection = conn
        self.started = True
        thread = threading.Thread(target=tcp_listener, args=(self, ))
        thread.run()

    def send(self, byte):
        self.sock.send(byte)

    def close(self):
        if self.started:
            self.started = False
            self.connection.close()

    def addHandler(self, handler):
        self.handlers.append(handler)

    def removeHandler(self, value):
        self.handlers.remove(value)

    def getHandlers(self):
        return self.handlers
