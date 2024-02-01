from kurses import *
from skreen import Skreen

if __name__ == "__main__" :
    s = Skreen(True)

    msg = ""
    while True :
        msg = s.input()
        if msg == "" or msg == " " * len(msg) :
            continue
        if msg == "^Z" :
            break
        s.print(msg, True)
    s.close()