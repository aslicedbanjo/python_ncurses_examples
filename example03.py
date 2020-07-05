#! /usr/bin/env python

# A Python port of Example 3 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/printw.html
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


def main():
    """ Entry point for example 3
    """
    msg = "Just a string"  # message to be shown on the screen

    screen = curses.initscr()  # start curses mode
    row, col = screen.getmaxyx()  # get the number of rows and number of columns

    # The Python API doesn't have mvprintw or printw, so use addstr
    screen.addstr(  # print the message at the centre of the screen
        row // 2, (col - len(msg)) // 2, msg
    )
    screen.addstr(row - 2, 0, "This screen has %s rows and %s cols" % (row, col))

    resize_msg = "Try resizing your window (if possible) and then run this program again."
    screen.addstr(row - 1, 0, resize_msg)

    screen.refresh()
    screen.getch()
    curses.endwin()

    sys.exit(0)


if __name__ == "__main__":
    main()
