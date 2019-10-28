# -*-* coding:UTF-8 -*-*
import os


class ColorPrint(object):
    def __init__(self, message, style='info'):
        self.message = message
        self.style = style
        self._style_color_list = {'error': 'red', 'right': 'green', 'info': 'blue', 'warn': 'yellow'}
        self._style_symbol_list = {'error': '[-]', 'right': '[+]', 'info': '[*]', 'warn': '[!]'}
        self._unix_color_list = {'red': '\033[0;91m', 'green': '\033[0;92m', 'yellow': '\033[0;93m',
                                 'blue': '\033[0;94m', }
        self._windows_color_list = {'red': 0x04, 'green': 0x0a, 'yellow': 0x0e, 'blue': 0x03, }
        self._print()

    def _print(self):
        try:
            if os.name == 'nt':
                print('\r'+str(self._unix_color_list[self._style_color_list[self.style]]) + self._style_symbol_list[
                    self.style] + '\033[0m ' + self.message + 20 * ' ')
            else:
                print('\r'+str(self._windows_color_list[self._style_color_list[self.style]]) + self._style_symbol_list[
                    self.style] + '\033[0m ' + self.message + 20 * ' ')
            if self.style == 'error':
                raise SystemExit
        except:
            pass
