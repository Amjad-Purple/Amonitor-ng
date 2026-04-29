import time

import time
import sys

class Printer:
    def __init__(self):
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'bg_red': '\033[41m',
            'bg_green': '\033[42m',
            'bg_yellow': '\033[43m',
            'bg_blue': '\033[44m',
            'bg_cyan': '\033[46m',
            'end': '\033[0m'
        }

    def print_msg(self, msg, MODE):
        mode = MODE.lower()
        if mode == 'info':
            color = 'cyan'
            bg_color = '46'
            type = 'INFO'
        elif mode == 'success':
            color = 'green'
            bg_color = '42'
            type = 'SUCCESS'
        elif mode == 'error':
            color = 'red'
            bg_color = '41'
            type = 'ERROR'
        elif mode == 'warning':
            color = 'yellow'
            bg_color = '43'
            type = 'WARNING'
        else:
            color = 'white'
            bg_color = '0'
            type = ''

        print(f"[\033[94m{time.strftime('%X')}\033[0m] [\033[{bg_color}m\033[30m{type}\033[0m] \033[97m{msg}\033[0m")


def print_msg(msg, mode):
    printer = Printer()
    printer.print_msg(msg, mode)
