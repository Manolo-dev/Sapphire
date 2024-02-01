from kurses.color           import *

class _ANSI:
	BEL = "\007"
	BS  = "\010"
	HT  = "\011"
	LF  = "\012"
	VT  = "\013"
	FF  = "\014"
	CR  = "\015"
	ESC = "\x1B"
	CSI = "\x9B"
	DCS = "\x90"
	OSC = "\x9D"
	DEL = "\177"

class _cursor:
	home      = lambda: _ANSI.CSI + "H"
	locate    = lambda x, y: _ANSI.CSI + f"{y};{x}H"
	up        = lambda y: _ANSI.CSI + f"{y}A"
	down      = lambda y: _ANSI.CSI + f"{y}B"
	right     = lambda x: _ANSI.CSI + f"{x}C"
	left      = lambda x: _ANSI.CSI + f"{x}D"
	beg_down  = lambda y: _ANSI.CSI + f"{y}E"
	beg_up    = lambda y: _ANSI.CSI + f"{y}F"
	collumn   = lambda x: _ANSI.CSI + f"{x}G"
	get_pos   = _ANSI.CSI + "6n"
	scroll_up = _ANSI.ESC + "M"
	DEC_save  = _ANSI.ESC + "7"
	DEC_load  = _ANSI.ESC + "8"
	SCO_save  = _ANSI.CSI + "s"
	SCO_load  = _ANSI.CSI + "u"

class _erase:
	curs_end      = _ANSI.CSI + "0J"
	curs_beg      = _ANSI.CSI + "1J"
	all           = _ANSI.CSI + "2J"
	saved         = _ANSI.CSI + "3J"
	curs_end_line = _ANSI.CSI + "0K"
	curs_beg_line = _ANSI.CSI + "1K"
	line          = _ANSI.CSI + "2K"

class _color:
	reset   = lambda: f"{_ANSI.CSI}0m"
	bold    = lambda string: f"{_ANSI.CSI}1m{string}{_ANSI.CSI}22m"
	dim     = lambda string: f"{_ANSI.CSI}2m{string}{_ANSI.CSI}22m"
	italic  = lambda string: f"{_ANSI.CSI}3m{string}{_ANSI.CSI}23m"
	under   = lambda string: f"{_ANSI.CSI}4m{string}{_ANSI.CSI}24m"
	blink   = lambda string: f"{_ANSI.CSI}5m{string}{_ANSI.CSI}25m"
	inverse = lambda string: f"{_ANSI.CSI}7m{string}{_ANSI.CSI}27m"
	hidden  = lambda string: f"{_ANSI.CSI}8m{string}{_ANSI.CSI}28m"
	strike  = lambda string: f"{_ANSI.CSI}9m{string}{_ANSI.CSI}29m"

	placeholder = lambda string: f"{_ANSI.CSI}3m\033[1;30m{string}{_ANSI.CSI}23m\033[0m\033[{len(string)}D"

	bold_beg    = f"{_ANSI.CSI}1m"
	dim_beg     = f"{_ANSI.CSI}2m"
	italic_beg  = f"{_ANSI.CSI}3m"
	under_beg   = f"{_ANSI.CSI}4m"
	blink_beg   = f"{_ANSI.CSI}5m"
	inverse_beg = f"{_ANSI.CSI}7m"
	hidden_beg  = f"{_ANSI.CSI}8m"
	strike_beg  = f"{_ANSI.CSI}9m"

	bold_end    = f"{_ANSI.CSI}22m"
	dim_end     = f"{_ANSI.CSI}22m"
	italic_end  = f"{_ANSI.CSI}23m"
	under_end   = f"{_ANSI.CSI}24m"
	blink_end   = f"{_ANSI.CSI}25m"
	inverse_end = f"{_ANSI.CSI}27m"
	hidden_end  = f"{_ANSI.CSI}28m"
	strike_end  = f"{_ANSI.CSI}29m"

	black   = lambda string: f"{_ANSI.CSI}30m{string}{_ANSI.CSI}0m"
	red     = lambda string: f"{_ANSI.CSI}31m{string}{_ANSI.CSI}0m"
	green   = lambda string: f"{_ANSI.CSI}32m{string}{_ANSI.CSI}0m"
	yellow  = lambda string: f"{_ANSI.CSI}33m{string}{_ANSI.CSI}0m"
	blue    = lambda string: f"{_ANSI.CSI}34m{string}{_ANSI.CSI}0m"
	magenta = lambda string: f"{_ANSI.CSI}35m{string}{_ANSI.CSI}0m"
	cyan    = lambda string: f"{_ANSI.CSI}36m{string}{_ANSI.CSI}0m"
	white   = lambda string: f"{_ANSI.CSI}37m{string}{_ANSI.CSI}0m"
	default = lambda string: f"{_ANSI.CSI}39m{string}{_ANSI.CSI}0m"

	bright_black   = lambda string: f"{_ANSI.CSI}90m{string}{_ANSI.CSI}0m"
	bright_red     = lambda string: f"{_ANSI.CSI}91m{string}{_ANSI.CSI}0m"
	bright_green   = lambda string: f"{_ANSI.CSI}92m{string}{_ANSI.CSI}0m"
	bright_yellow  = lambda string: f"{_ANSI.CSI}93m{string}{_ANSI.CSI}0m"
	bright_blue    = lambda string: f"{_ANSI.CSI}94m{string}{_ANSI.CSI}0m"
	bright_magenta = lambda string: f"{_ANSI.CSI}95m{string}{_ANSI.CSI}0m"
	bright_cyan    = lambda string: f"{_ANSI.CSI}96m{string}{_ANSI.CSI}0m"
	bright_white   = lambda string: f"{_ANSI.CSI}97m{string}{_ANSI.CSI}0m"

	color256 = lambda string, i: f"{_ANSI.CSI}38;5;{i}m{string}{_ANSI.CSI}0m"
	rgb      = lambda string, *rgb: f"{_ANSI.CSI}38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}{_ANSI.CSI}0m"
	hsv      = lambda string, *hsv: (lambda string, rgb: f"{_ANSI.CSI}38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}{_ANSI.CSI}0m")(string, hsv_to_rgb(hsv))
	hsl      = lambda string, *hsl: (lambda string, rgb: f"{_ANSI.CSI}38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}{_ANSI.CSI}0m")(string, hsl_to_rgb(hsl))
	hex      = lambda string,  h_x: (lambda string, rgb: f"{_ANSI.CSI}38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}{_ANSI.CSI}0m")(string, hex_to_rgb(h_x))

	class background:
		black   = lambda string: f"{_ANSI.CSI}40m{string}{_ANSI.CSI}0m"
		red     = lambda string: f"{_ANSI.CSI}41m{string}{_ANSI.CSI}0m"
		green   = lambda string: f"{_ANSI.CSI}42m{string}{_ANSI.CSI}0m"
		yellow  = lambda string: f"{_ANSI.CSI}43m{string}{_ANSI.CSI}0m"
		blue    = lambda string: f"{_ANSI.CSI}44m{string}{_ANSI.CSI}0m"
		magenta = lambda string: f"{_ANSI.CSI}45m{string}{_ANSI.CSI}0m"
		cyan    = lambda string: f"{_ANSI.CSI}46m{string}{_ANSI.CSI}0m"
		white   = lambda string: f"{_ANSI.CSI}47m{string}{_ANSI.CSI}0m"
		default = lambda string: f"{_ANSI.CSI}49m{string}{_ANSI.CSI}0m"

		bright_black   = lambda string: f"{_ANSI.CSI}100m{string}{_ANSI.CSI}0m"
		bright_red     = lambda string: f"{_ANSI.CSI}101m{string}{_ANSI.CSI}0m"
		bright_green   = lambda string: f"{_ANSI.CSI}102m{string}{_ANSI.CSI}0m"
		bright_yellow  = lambda string: f"{_ANSI.CSI}103m{string}{_ANSI.CSI}0m"
		bright_blue    = lambda string: f"{_ANSI.CSI}104m{string}{_ANSI.CSI}0m"
		bright_magenta = lambda string: f"{_ANSI.CSI}105m{string}{_ANSI.CSI}0m"
		bright_cyan    = lambda string: f"{_ANSI.CSI}106m{string}{_ANSI.CSI}0m"
		bright_white   = lambda string: f"{_ANSI.CSI}107m{string}{_ANSI.CSI}0m"

		color256 = lambda string, i: f"{_ANSI.CSI}48;5;{i}m{string}{_ANSI.CSI}0m"
		rgb      = lambda string, *rgb: f"{_ANSI.CSI}48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}{_ANSI.CSI}0m"
		hsv      = lambda string, *hsv: (lambda string, rgb: f"{_ANSI.CSI}48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}{_ANSI.CSI}0m")(string, hsv_to_rgb(hsv))
		hsl      = lambda string, *hsl: (lambda string, rgb: f"{_ANSI.CSI}48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{string}{_ANSI.CSI}0m")(string, hsl_to_rgb(hsl))

class ANSI(_ANSI):
	class cursor(_cursor):
		pass
	class erase(_erase):
		pass
	class color(_color):
		pass

if __name__ == "__main__" :
	for i in range(4096) :
		print(ANSI.color.background.hsv(" " * getTerminalSize()[0], i%128, 128, 128) + ANSI.color.reset())
