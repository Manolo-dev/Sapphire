import os
from kurses import ANSI, getTerminalSize, kinput, wrap

class Skreen :
    """Skreen is a class that allows you to create a screen with a chat-like interface."""
    def __init__(self, clear=False, sender=False, color=(0, 160, 0)):
        """Create a new Skreen object."""
        self.size = getTerminalSize()
        if clear : self.clear()
        self.sender = sender
        self.color = lambda string: ANSI.color.rgb(string, *color)
        print()

    def clear(self) :
        """Clear the screen."""
        if os.name == 'nt' :
            os.system('cls')
        else :
            os.system('clear')

    def input(self):
        """Create an input field."""
        self.size = getTerminalSize()
        print(self.color("╭" + "─" * (self.size[0] - 2) + "╮"), end="\n\n")
        print(self.color("╰" + "─" * (self.size[0] - 2) + "╯"), end="")
        print(ANSI.cursor.beg_up(0), end="")
        result = kinput(pos=(1, 0), max=4096, placeholder="Taper un message", width=self.size[0] - 3, background=self.color(f"│{ANSI.cursor.right(self.size[0] - 2)}│"))
        print(ANSI.cursor.beg_up(2) + (ANSI.erase.line + "\n") * 3 + ANSI.cursor.beg_up(3), end="")
        return result

    def print(self, string):
        wr, length = wrap(string, self.size[0] - 8 if self.sender else self.size[0] - 12, oneline=True)

        if self.sender :
            tab = " " * (self.size[0] - length - 2)
        else :
            tab = ""

        print(tab + self.color("╭" + "─" * length + "╮"))
        for i in wr :
            print(tab + self.color("│") + i + self.color("│"))
        print(tab + self.color(f"╰" + "─" * length + "╯"))

        return {"height": len(wr)}

    def close(self):
        print((ANSI.erase.line + "\n") * 5)
        print(ANSI.cursor.beg_up(7))