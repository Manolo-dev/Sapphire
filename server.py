import socket
import json
import threading

class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), 5000))
        self.clients:dict[str, socket.socket] = {}
        self.contacts:list = []
    
    def client(self, socket:socket.socket, address:str):
        while True:
            try:
                msg = socket.recv(4096)
            except:
                break
            if msg == b"":
                break
            msg = json.loads(msg)
            if "msg" in msg:
                for client in self.clients:
                    self.clients[client].send(bytes(json.dumps({"msg": msg["msg"], "mac": msg["mac"]}), "utf-8"))
        for contact in self.contacts:
            if contact["mac"] == address:
                self.contacts.remove(contact)
                break
        del self.clients[address]
    
    def start(self):
        self.socket.listen(5)
        while True:
            clientsocket, _ = self.socket.accept()
            clientsocket.send(bytes(json.dumps(self.contacts), "utf-8"))
            log = clientsocket.recv(4096)
            log = json.loads(log)
            print(log)
            for client in self.clients:
                self.clients[client].send(bytes(json.dumps({"new": log}), "utf-8"))
            self.clients[log["mac"]] = clientsocket
            self.contacts.append(log)
            threading.Thread(target=self.client, args=(clientsocket, log["mac"])).start()