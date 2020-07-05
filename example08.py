#! /usr/bin/env python

# A Python port of Example 8 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/windows.html
#
# Copyright (C) 2013 - 2016, 2020 Dan Jacobs
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import curses
import sys


class WinBorder(object):
    def __init__(self, ls, rs, ts, bs, tl, tr, bl, br):
        self.ls = ls
        self.rs = rs
        self.ts = ts
        self.bs = bs
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br


class Win(object):
    def __init__(self, startx, starty, height, width, border):
        self.startx = startx
        self.starty = starty
        self.height = height
        self.width = width
        self.border = border


def init_win_params():
    """ Create and initialise a Win object
    """
    border = WinBorder('|', '|', '-', '-', '+', '+', '+', '+')

    height = 3
    width = 10
    win = Win((curses.COLS - width) // 2, (curses.LINES - height) // 2, height, width, border)

    return win


def print_win_params(scrn, win):
    """ Write the window parameters to the screen
    """
    scrn.addstr(20, 0, "%s %s %s %s " % (win.startx, win.starty, win.width, win.height))
    scrn.refresh()


def create_box(scrn, win, flag):
    """ Create a box on the given screen
    """
    x = win.startx
    y = win.starty
    w = win.width
    h = win.height

    if flag:
        scrn.addch(y, x, win.border.tl)
        scrn.addch(y, x + w, win.border.tr)
        scrn.addch(y + h, x, win.border.bl)
        scrn.addch(y + h, x + w, win.border.br)
        scrn.hline(y, x + 1, win.border.ts, w - 1)
        scrn.hline(y + h, x + 1, win.border.bs, w - 1)
        scrn.vline(y + 1, x, win.border.ls, h - 1)
        scrn.vline(y + 1, x + w, win.border.rs, h - 1)
    else:
        for j in range(y, y + h + 1):
            for i in range(x, x + w + 1):
                scrn.addch(j, i, ' ')

    scrn.refresh()


def main():
    """ Entry point for example 8
    """
    screen = curses.initscr()  # Start curses mode
    curses.start_color()  # Start the color functionality

    curses.cbreak()  # Line buffering disabled, pass everything to the program
    screen.keypad(True)  # Need F2 key
    curses.noecho()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # Initialize the window parameters
    win = init_win_params()

    print_win_params(screen, win)

    screen.attron(curses.color_pair(1))
    screen.addstr("Press F2 to exit")
    screen.refresh()
    screen.attroff(curses.color_pair(1))

    create_box(screen, win, True)

    char = screen.getch()
    while char != curses.KEY_F2:

        if char == curses.KEY_LEFT:
            create_box(screen, win, False)
            win.startx = win.startx - 1
            create_box(screen, win, True)

        if char == curses.KEY_RIGHT:
            create_box(screen, win, False)
            win.startx = win.startx + 1
            create_box(screen, win, True)

        if char == curses.KEY_UP:
            create_box(screen, win, False)
            win.starty = win.starty - 1
            create_box(screen, win, True)

        if char == curses.KEY_DOWN:
            create_box(screen, win, False)
            win.starty = win.starty + 1
            create_box(screen, win, True)

        char = screen.getch()

    curses.endwin()  # End curses mode
    sys.exit(0)


if __name__ == "__main__":
    main()
