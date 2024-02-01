#!/usr/bin/python3
from skreen import Skreen

if __name__ == "__main__" :
    s = Skreen(clear=True)

    msg = ""
    while True :
        msg = s.input()
        if msg == "" or msg == " " * len(msg) :
            continue
        if msg == "!quit" :
            break
        s.print(msg, True)
    s.close()