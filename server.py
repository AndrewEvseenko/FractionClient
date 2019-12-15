import socket
import threading
from certificate import Certificate
import rsa

host = socket.gethostbyname(socket.gethostname())


def on_client_connect(server_inst):
    while server_inst.started:
        conn, addr = server_inst.accept()
        data = conn.recv(1024)
        if data == b"connect":
            if conn not in server_inst.clients:
                server_inst.clients.append(conn)
                rsa_connect(conn, server_inst)
        elif data == b"disconnect":
            if conn in server_inst.clients:
                server_inst.clients.remove(conn)
        elif not data:
            if conn in server_inst.clients:
                server_inst.clients.remove(conn)
        else:
            for handler in server_inst.handlers:
                handler(server_inst, conn, data)


def rsa_connect(conn, server_inst):
    conn.send(server_inst.certificate.getJSON().encode())
    server_inst.queue.append(conn)
    server_inst.addHandler(client_certificate)


def client_certificate(server, conn, data):
    if conn in server.queue:
        server.queue.remove(conn)
        client_cert = Certificate.fromJSON(data.decode())
        server_cert = server.certificate
        if client_cert.getName() == server_cert.getName():
            pass


class Server:

    def __init__(self, certificate):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.started = False
        self.certificate = certificate
        self.pubkey, self.privkey = rsa.newkeys(2048)

    def start(self, port, ip=host, connections=30):
        self.sock.bind(ip, port)
        self.sock.listen(connections)
        self.handlers = []
        self.clients = []
        self.queue = []
        self.started = True
        thread = threading.Thread(target=on_client_connect, args=(self, ))
        thread.run()

    def send(self, byte):
        self.sock.send(byte)

    def close(self):
        if self.started:
            self.started = False
            for conn in self.clients:
                conn.close()
            del self.handlers
            del self.clients

    def addHandler(self, handler):
        self.handlers.append(handler)

    def removeHandler(self, value):
        self.handlers.remove(value)

    def getHandlers(self):
        return self.handlers
