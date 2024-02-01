import socket
import uuid
import threading

from kurses import *
from skreen import Skreen

class Sapphire :
    mac = hex(uuid.getnode())[2:]
    ip  = socket.gethostbyname(socket.gethostname())

    def __init__(self) :
        """
            Crée un socket et ouvre une interface
            @params:
                self {selfObject}
        """

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn   = None
        self.Screen = Skreen()

    def open(self, host, port) :
        """
            Open server
            @params:
                self {selfObject}
                host {str} IP du client
                port {int} port du client
        """

        self.socket.bind((host, port))
        self.socket.listen()
        self.conn = self.socket.accept()[0]

    def close(self) :
        """
            Ferme le socket et termine l'interface
            @params:
                self {selfObject}
        """

        self.socket.close()
        self.Screen.close()

    def connect(self, host, port) :
        """
            Connecte au server
            @params:
                self {selfObject}
                host {str} IP du serveur
                port {int} port du serveur
        """

        self.socket.connect((host, port))

    def input(self) :
        """
            Attend une entrée et l'envoie, le repète tant que l'entrée n'est pas "exit"
            @params:
                self {selfObject}
        """

        msg = ""
        while msg == "" :
            try :
                msg = self.Screen.input()
                self.socket.send(msg.encode('UTF-8'))
            except EOFError :
                break
        return msg

    def receive(self) :
        """
            Attend un message et l'affiche
            @params:
                self {selfObject}
        """

        msg = ""
        while msg == "" :
            try :
                data = self.conn.recv(1024)
            except :
                break
            if not data :
                break
            msg = data.decode()

        return msg

def server() :
    serv = Sapphire()
    serv.open("10.86.24.183", 65001)
    msg = serv.receive()
    serv.Screen.print(msg, False)
    serv.close()

    return msg

def client() :
    clnt = Sapphire()
    clnt.connect("10.86.24.183", 65001)
    msg = clnt.input()
    clnt.Screen.print(msg, True)
    clnt.close()

    return msg

if __name__ == "__main__" :
    if len(sys.argv) > 1 and sys.argv[1] == "-s" :
        while True :
            msg = server()
            if msg[-2:] == "^Z" : break
            msg = client()
            if msg == "^Z" : break
    else :
        while True :
            msg = client()
            if msg == "^Z" : break
            msg = server()
            if msg == "^Z" : break
