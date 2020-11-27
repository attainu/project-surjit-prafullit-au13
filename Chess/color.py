import os

os.system("cls")


class Colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class Foreground:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        grey = '\033[90m'
        yellow = '\033[93m'
        white = '\u001b[37m'

    class Background:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        yellow = '\033[93m'
        grey = '\033[47m'
        white = '\u001b[37m'
        Magenta = '\u001b[45m'
