#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
from functools import partial
import curses
from curses.textpad import Textbox, rectangle

class Screen(object):
    def __init__(self, echomode=False, wait4enter=False, keyparse=True):
        self.screen = curses.initscr()
        self.screen.keypad(keyparse)
        if not echomode: curses.noecho()
        if not wait4enter: curses.cbreak()
        self.windows = []
        self.buffers = []

    def on(self):
        self.screen.border(0)
        editwin = curses.newwin(2,60, 2,2)
        self.screen.refresh()
        box = Textbox(editwin)
        # Let the user edit until Ctrl-G is struck.
        box.edit()
        # Get resulting contents
        message = box.gather()
        self.repl()

    def repl(self):
        while True:
            try:
                key = self.screen.getkey()
                self.clear()
            except KeyboardInterrupt:
                self.off()
                break

    def wait(self):
        self.screen.getch()

    def clear(self):
        self.screen.clear()
        self.screen.refresh()

    def switch():
        """Cycles/switches the contents of this buffer to display the
        contents of another window
        """
        raise NotImplementedError

    def create_window():
        raise NotImplementedError

    def vsplit(self):
        raise NotImplementedError

    def hsplit(self):
        raise NotImplementedError

    def off(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()
        
if __name__ == "__main__":
    screen = Screen()
    screen.on()

