import socket
import csv
from skreen import Skreen
from server import Server
import os
import multiprocessing
import json
import uuid
import psutil

def get_ip_addresses():
    for interface, snics in psutil.net_if_addrs().items():
        mac = None
        for snic in snics:
            if snic.family == -1 :
                mac = snic.address
            if snic.family == 2 :
                yield (interface, snic.address, snic.netmask, mac)

mac_address = list(get_ip_addresses())
print(mac_address)

self_skreen = Skreen()
receive_skreen:dict[str, Skreen] = {}
if not os.path.exists("contact.csv"):
    file = open("contact.csv", "w")
    fieldnames = ["name", "mac", "color"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

# mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
print(mac_address)
name = input("Name: ")

contacts = list(csv.DictReader(open("contact.csv", "r")))
print(contacts)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for row in contacts:
    try:
        s.connect((row["mac"], 5000))
        break
    except:
        pass
else:
    try:
        s.connect((mac_address, 5000))
    except:
        server = Server()
        multiprocessing.Process(target=server.start).start()
        s.connect((mac_address, 5000))

s.send(bytes(json.dumps({"name": name, "mac": mac_address, "color": (0, 85, 0)}), "utf-8"))
get_contacts = s.recv(4096)
get_contacts = json.loads(get_contacts)
for contact in get_contacts:
    receive_skreen[contact["mac"]] = Skreen(clear=True, sender=True, color=contact["color"])
    for former_contact in contacts:
        if former_contact["mac"] == contact["mac"]:
            former_contact.update(contact)
            break
    else:
        contacts.append(contact)

quit_ = False

def connection_receive():
    while not quit_:
        msg = s.recv(4096)
        msg = json.loads(msg)
        if "msg" in msg:
            receive_skreen[msg["mac"]].print(msg["msg"])
        if "new" in msg:
            receive_skreen[msg["new"]["mac"]] = Skreen(clear=True, sender=True, color=msg["new"]["color"])
            print(f"{msg["new"]} Vient de se connecter")

recv:multiprocessing.Process = multiprocessing.Process(target=connection_receive).start()

while True:
    msg = self_skreen.input()
    if msg == "!quit":
        quit_ = True
        recv.terminate()
        break
    if msg == "!clear":
        self_skreen.clear()
        continue
    if msg == "!help":
        print("quit: Quitte le programme")
        print("clear: Efface l'écran")
        print("contacts: Affiche les contacts")
        print("add: Ajoute un contact")
        print("remove: Supprime un contact")
        print("color: Change la couleur du texte")
        print("help: Affiche l'aide")
        continue
    s.send(bytes(json.dumps({"msg": msg, "mac": mac_address}), "utf-8"))
    self_skreen.print(msg)
    