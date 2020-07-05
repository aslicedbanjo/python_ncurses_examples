#! /usr/bin/env python

# A Python port of Example 9 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/color.html
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


def print_in_middle(win, starty, startx, width, string):
    """ Print the string in the middle of the window
    """
    y, x = win.getyx()

    if startx != 0:
        x = startx
    if starty != 0:
        y = starty
    if width == 0:
        width = 80

    length = len(string)
    temp = (width - length) // 2
    x = startx + temp
    win.addstr(y, x, string)
    win.refresh()


def main():
    """ Entry point for example 9
    """
    screen = curses.initscr()  # Start curses mode

    if not curses.has_colors():
        curses.endwin()
        print("Your terminal does not support color\n")
        sys.exit(1)

    curses.start_color()  # Start color
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    screen.attron(curses.color_pair(1))
    print_in_middle(screen, curses.LINES // 2, 0, 0, "Viola !!! In color ...")
    screen.attroff(curses.color_pair(1))

    screen.getch()
    curses.endwin()


if __name__ == "__main__":
    main()
