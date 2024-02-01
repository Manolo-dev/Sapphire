import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "194.254.24.226"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = int(self.connect())

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

network = Network()
print(f"Connected as client {network.id}")