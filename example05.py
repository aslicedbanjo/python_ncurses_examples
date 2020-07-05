#! /usr/bin/env python
#
# A Python port of Example 5 from
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
#
# pager functionality by Joseph Spainhour" <spainhou@bellsouth.net>
#
# Python port notes: I'm not convinced the original example worked properly since the
# lines disappear as soon as the last character is printed (in both C and the initial
# Python version). In this Python version, I have added a short sleep so that the
# characters can be seen.

import curses
import sys
import time


def main():
    """ Entry point for example 5
    """

    if len(sys.argv) != 2:
        print("Usage: %s <path to a C file>\n" % (sys.argv[0],))
        sys.exit(1)

    prev = None

    screen = curses.initscr()   # Start curses mode
    row, _ = screen.getmaxyx()   # find the boundaries of the screen

    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            for char in line:   # read the file character by character till we reach the end
                y, x = screen.getyx()   # get the current cursor position

                if y == (row - 1):   # are we are at the end of the screen
                    screen.addstr("<-Press Any Key->")   # tell the user to press a key
                    screen.getch()
                    screen.clear()   # clear the screen
                    screen.move(0, 0)   # start at the beginning of the screen

                if prev == '/' and char == '*':   # If it's / and * then only switch bold on
                    screen.attron(curses.A_BOLD)   # put bold on
                    y, x = screen.getyx()   # get the current cursor position
                    screen.move(y, x - 1)   # back up one space
                    screen.addstr("%s%s" % ('/', char))    # The actual printing is done here
                else:
                    screen.addstr("%s" % (char,))

                if prev == '*' and char == '/':
                    screen.attroff(curses.A_BOLD)   # Switch bold off once we find a * and then /

                screen.refresh()
                time.sleep(0.01)

                prev = char

    screen.addstr("\n<-Press Any Key->")   # tell the user to press a key
    screen.getch()
    curses.endwin()   # End curses mode
    sys.exit(0)


if __name__ == "__main__":
    main()
