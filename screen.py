#!/usr/bin/python3
from skreen import Skreen
from microlanguage import execml

if __name__ == "__main__" :
    s = Skreen(clear=True)

    msg = ""
    while True :
        msg = s.input()
        if msg == "" or msg == " " * len(msg) :
            continue
        if msg[0] == "!":
            msg = execml(msg[1:])
        s.print(msg)
    s.close()