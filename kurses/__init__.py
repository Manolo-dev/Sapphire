name    = "kurses"
version = 1.0
author  = "Manolo Sardo"

import os
import sys
import textwrap
if os.name == "nt":
    import msvcrt
else:
    import tty
    import termios
import math

from kurses.color           import *
from kurses.ANSI            import ANSI
from kurses.getch           import getch, keyboard
from kurses.getTerminalSize import getTerminalSize
from kurses.input           import kinput
from kurses.wrap            import wrap