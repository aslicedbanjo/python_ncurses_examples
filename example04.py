#! /usr/bin/env python

# A Python port of Example 4 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/scanw.html
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

# Python porting comment: the example is described on the web page as
# "Example 4. A Simple scanw example" but scanw is not used directly.

import curses
import sys


def main():
    """ Entry point for example 4
    """
    mesg = "Enter a string: "  # message to be shown on the screen

    screen = curses.initscr()  # start curses mode
    row, col = screen.getmaxyx()  # get the number of rows and columns

    # The Python API doesn't have mvprintw, so use addstr
    screen.addstr(  # print the message at the centre of the screen
        row // 2, (col - len(mesg)) // 2, mesg
    )

    string = screen.getstr()
    screen.addstr(row - 2, 0, "You Entered: %s" % (string.decode("UTF-8"),))
    screen.getch()
    curses.endwin()

    sys.exit(0)


if __name__ == "__main__":
    main()
