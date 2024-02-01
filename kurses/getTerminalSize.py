"""
    Fonction getTerminalSize(), donne les dimensions du terminal utilisé
    @name: getTerminalSize
    @version: 1.0
    @date: 19/03/2022
    @authors: Harco Kuppens
    @functions:
        getTerminalSize()
        _getTerminalSize_windows()
        _getTerminalSize_tput()
        _getTerminalSize_linux()
    @datas:
        __all__ {list}['getTerminalSize']
    @imports:
        platform
        ctypes
        subprocess
        fcntl
        termios
        struct
        os
"""

__all__ = ['getTerminalSize']


def getTerminalSize() -> tuple :
    """
        Donne les dimensions du terminal utilisé
        @returns:
            tuple_xy {tuple}
    """

    import platform

    current_os = platform.system()
    tuple_xy   = None
    if current_os == 'Windows' :
        tuple_xy = _getTerminalSize_windows()
        if tuple_xy is None :
            tuple_xy = _getTerminalSize_tput()
    if current_os == 'Linux' or current_os == 'Darwin' or current_os.startswith('CYGWIN') :
        tuple_xy = _getTerminalSize_linux()
    if tuple_xy is None :
        tuple_xy = (80, 25)
    return tuple_xy

def _getTerminalSize_windows() -> tuple :
    """
        Donne les dimensions du terminal utilisé si le terminal est sous Windows
        @returns:
            {tuple}|{None}
    """

    res = None
    try :
        from ctypes import windll, create_string_buffer

        h    = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res  = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    except :
        return None
    if res :
        import struct

        (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        sizex = right  - left + 1
        sizey = bottom - top  + 1

        return sizex, sizey
    else :
        return None

def _getTerminalSize_tput() -> tuple :
    """
        Donne les dimensions du terminal utilisé si le terminal est sous Windows et que la fonction précédente ne renvoie rien
        @returns:
            {tuple}|{None}
    """

    try :
        import subprocess
        proc   = subprocess.Popen(["tput", "cols"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        output = proc.communicate(input=None)
        cols   = int(output[0])
        proc   = subprocess.Popen(["tput", "lines"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        output = proc.communicate(input=None)
        rows   = int(output[0])

        return (cols, rows)
    except :
        return None


def _getTerminalSize_linux() -> tuple :
    """
        Donne les dimensions du terminal utilisé si le terminal est sous Linux
        @returns:
            {tuple}|{None}
    """

    def ioctl_GWINSZ(fd) :
        try :
            import fcntl, termios, struct, os

            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,'1234'))
        except :
            return None
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr :
        try :
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except :
            pass

    if not cr :
        try :
            cr = (env['LINES'], env['COLUMNS'])
        except :
            return None

    return int(cr[1]), int(cr[0])

if __name__ == "__main__" :
    sizex, sizey = getTerminalSize()
    print('width =', sizex, 'height =', sizey)