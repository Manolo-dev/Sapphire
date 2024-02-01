import os
import sys
from kurses import getch, ANSI, keyboard

def kinput(string="", end="\n", pos=(0, 0), placeholder="", max=-1, width=-1, background="") :
    line  = ""
    i     = 0
    start = 0

    if width == -1 :
        width = getTerminalSize()[0] - 2
    width -= len(string) + pos[0]
    stop  = ANSI.cursor.right(width+1)
    placeholder = placeholder[:width]

    y_pos = ANSI.cursor.beg_down(pos[1]) if pos[1] != 0 else ""
    print(f"{y_pos}{ANSI.cursor.collumn(pos[0] + 1)}{ANSI.cursor.DEC_save}{ANSI.cursor.collumn(0)}{background}{ANSI.cursor.DEC_load}{string}◄{ANSI.color.placeholder(placeholder)}{ANSI.cursor.DEC_load}{stop} {ANSI.cursor.DEC_load} ", end="")
    while True :
        sys.stdout.flush()
        char = getch()

        if char == keyboard.NL : # entry
            break
        if char == keyboard.ctrl_NL : # crl entry
            line = ""
            break
        if char == keyboard.BS : # backspace
            if i != 0 :
                temp = len(line)
                line = line[:i-1] + line[i:]
                i -= temp - len(line)
            char = ""
        if char == keyboard.LEFT : # left
            if i > 0 :
                i -= 1
            char = ""
        if char == keyboard.RIGHT : # right
            if i < len(line) :
                i += 1
            char = ""
        if char == keyboard.DEL : # del
            if len(line) - i != 0 :
                line = line[:i] + line[i+1:]
            char = ""
        if char == keyboard.TAB : # tab
            char = "    "
        ctrl = keyboard.ctrl(char)
        if ctrl != None : # ctrl
            char = ctrl
        if max != -1 and len(line) >= max : # max lenght
            char = ""

        line = line[:i] + char + line[i:]
        i += len(char)

        if i > width :
            width += 1
            start += 1
        elif i < start :
            start -= 1
            width -= 1

        right = left = 0
        if width < len(line) :
            right = 1
        if start > 0 :
            left = 1

        j = ANSI.cursor.right(i-start+1) if i-start+1 != 0 else ""
        l = "◄" if left  else " "
        r = "►" if right else " "
        ph = ANSI.color.placeholder(placeholder) if len(line) == 0 else ""
        print(f"{ANSI.erase.line}{ANSI.cursor.collumn(0)}{background}{ANSI.cursor.DEC_load}{string}{l}{ph}{line[start:width]}{ANSI.cursor.DEC_load}{stop}{r}{ANSI.cursor.DEC_load}{j}", end="")

    print(end, end="")
    return line