import socket


def listen_function(conn):
    pass


class Client:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, port, ip="localhost"):
        self.sock.connect(ip, port)

    def send(self, byte):
        self.sock.send(byte)

    def listen(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()

    def __exit__(self, arg, value, traceback):
        self.close()
