from kurses import *

class Skreen :
    def __init__(self, clear=False) :
        self.size = getTerminalSize()
        if clear : self.clear()
        self.color = lambda string: ANSI.color.rgb(string, 0, 85, 0)
        self.file  = open("contact.csv", "w+")
        print()

    def clear(self) :
        if os.name == 'nt' :
            os.system('cls')
        else :
            os.system('clear')

    def input(self) :
        print(self.color("╭" + "─" * (self.size[0] - 2) + "╮"), end="\n\n")
        print(self.color("╰" + "─" * (self.size[0] - 2) + "╯"), end="")
        print(ANSI.cursor.beg_up(0), end="")
        result = kinput(pos=(1, 0), max=4096, placeholder="Taper un message", width=self.size[0] - 3, background=self.color(f"│{ANSI.cursor.right(self.size[0] - 2)}│"))
        print(ANSI.cursor.beg_up(2) + (ANSI.erase.line + "\n") * 3 + ANSI.cursor.beg_up(3), end="")
        return result

    def print(self, string, sender=False) :
        wr, length = wrap(string, self.size[0] - 8, oneline=True)

        if sender :
            tab = " " * (self.size[0] - length - 2)
        else :
            tab = ""

        print(tab + self.color("╭" + "─" * length + "╮"))
        for i in wr :
            print(tab + self.color("│") + i + self.color("│"))
        print(tab + self.color(f"╰" + "─" * length + "╯"))

        return {"height": len(wr)}

    def close(self) :
        print((ANSI.erase.line + "\n") * 5)
        print(ANSI.cursor.beg_up(7))