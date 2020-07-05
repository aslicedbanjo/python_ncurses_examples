#! /usr/bin/env python

# A Python port of Example 12 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/misc.html
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
import os
import sys


def main():
    """ Entry point for example 12
    """
    screen = curses.initscr()  # Start curses mode
    screen.addstr("Hello World !!!\n")  # Print Hello World
    screen.refresh()  # Print it on to the real screen

    # Wait for user input to see printed message (added during porting)
    screen.getch()

    curses.def_prog_mode()  # Save the tty mode
    curses.endwin()  # End curses mode temporarily

    os.system("/bin/sh")  # Do whatever you like in cooked mode

    curses.reset_prog_mode()  # Return to the previous tty mode stored by def_prog_mode()

    screen.refresh()  # Do refresh() to restore the screen contents
    screen.addstr("Another String\n")  # Back to curses use the full capabilities of curses
    screen.refresh()

    # Wait for user input to see printed message (added during porting)
    screen.getch()

    curses.endwin()  # End curses mode

    sys.exit(0)


if __name__ == "__main__":
    main()
