#! /usr/bin/env python

# A Python port of Example 6 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/attrib.html
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
    """ Entry point for example 6
    """
    screen = curses.initscr()  # Start curses mode
    curses.start_color()  # Start color functionality

    # This initialises the color pair at index 1 to have foreground cyan
    # and background black
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    screen.addstr("A Big string which I didn't care to type fully ")

    # The original C example states:
    #
    # First two parameters specify the position at which to start
    # Third parameter number of characters to update. -1 means till
    # end of line
    # Forth parameter is the normal attribute you wanted to give
    # to the character
    # Fifth is the color index. It is the index given during init_pair()
    # use 0 if you didn't want color
    # Sixth one is always NULL

    # In the Python API, we must pass the color pair as an attribute, so
    # bitwise-or it with the A_BLINK parameter
    # (chgat takes between 1 and 4 arguments only in the Python API).
    screen.chgat(0, 0, -1, curses.A_BLINK | curses.color_pair(1))

    screen.refresh()
    screen.getch()
    curses.endwin()  # End curses mode

    sys.exit(0)


if __name__ == "__main__":
    main()
