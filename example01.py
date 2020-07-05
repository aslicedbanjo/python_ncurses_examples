#! /usr/bin/env python

# A Python port of Example 1 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/helloworld.html
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
    """ Entry point for example 1
    """
    screen = curses.initscr()  # Start curses mode
    # The Python API doesn't have printw, so use addstr
    screen.addstr("Hello World !!!")  # Print Hello World !!!

    screen.refresh()  # Print it on to the screen
    screen.getch()  # Wait for user input
    curses.endwin()  # End curses mode

    sys.exit(0)


if __name__ == "__main__":
    main()
