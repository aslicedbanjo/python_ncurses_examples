#! /usr/bin/env python

# A Python port of Example 2 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/init.html
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
    """ Entry point for example 2
    """
    screen = curses.initscr()  # Start curses mode
    curses.raw()  # Line buffering disabled
    screen.keypad(True)  # We get F1, F2 etc..
    curses.noecho()  # Don't echo() while we do getch

    # The Python API doesn't have printw, so use addstr
    screen.addstr("Type any character to see it in bold\n")

    # If raw() hadn't been called we have to press enter
    # before it gets to the program
    # Note that this is a C-character (an integer between 0 and 255)
    char = screen.getch()

    # Without keypad enabled this will not get to us either
    if char == curses.KEY_F2:
        # Without noecho() some ugly escape charachters might
        # have been printed on screen
        screen.addstr("F2 Key pressed")
    else:
        screen.addstr("The pressed key is ")
        screen.attron(curses.A_BOLD)
        screen.addstr("%s" % (chr(char),))
        screen.attroff(curses.A_BOLD)

    screen.refresh()  # Print it on to the real screen
    screen.getch()  # Wait for user input
    curses.endwin()  # End curses mode

    sys.exit(0)


if __name__ == "__main__":
    main()
