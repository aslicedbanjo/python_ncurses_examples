#! /usr/bin/env python

# A Python port of Example 13 from
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
import sys


def main():
    """ Entry point for example 13
    """
    screen = curses.initscr()

    # Added when porting to allow scrolling of screen which prevents
    # addstr returning ERR and therefore prevents crashing the program.
    screen.scrollok(True)

    # Output messages reformatted during porting.
    screen.addstr("Upper left corner        ")
    screen.addch(curses.ACS_ULCORNER)
    screen.addstr("\t")

    screen.addstr("Lower left corner        ")
    screen.addch(curses.ACS_LLCORNER)
    screen.addstr("\n")

    screen.addstr("Lower right corner       ")
    screen.addch(curses.ACS_LRCORNER)
    screen.addstr("\t")

    screen.addstr("Tee pointing right       ")
    screen.addch(curses.ACS_LTEE)
    screen.addstr("\n")

    screen.addstr("Tee pointing left        ")
    screen.addch(curses.ACS_RTEE)
    screen.addstr("\t")

    screen.addstr("Tee pointing up          ")
    screen.addch(curses.ACS_BTEE)
    screen.addstr("\n")

    screen.addstr("Tee pointing down        ")
    screen.addch(curses.ACS_TTEE)
    screen.addstr("\t")

    screen.addstr("Horizontal line          ")
    screen.addch(curses.ACS_HLINE)
    screen.addstr("\n")

    screen.addstr("Vertical line            ")
    screen.addch(curses.ACS_VLINE)
    screen.addstr("\t")

    screen.addstr("Large Plus or cross over ")
    screen.addch(curses.ACS_PLUS)
    screen.addstr("\n")

    screen.addstr("Scan Line 1              ")
    screen.addch(curses.ACS_S1)
    screen.addstr("\t")

    screen.addstr("Scan Line 3              ")
    screen.addch(curses.ACS_S3)
    screen.addstr("\n")

    screen.addstr("Scan Line 7              ")
    screen.addch(curses.ACS_S7)
    screen.addstr("\t")

    screen.addstr("Scan Line 9              ")
    screen.addch(curses.ACS_S9)
    screen.addstr("\n")

    screen.addstr("Diamond                  ")
    screen.addch(curses.ACS_DIAMOND)
    screen.addstr("\t")

    screen.addstr("Checker board (stipple)  ")
    screen.addch(curses.ACS_CKBOARD)
    screen.addstr("\n")

    screen.addstr("Degree Symbol            ")
    screen.addch(curses.ACS_DEGREE)
    screen.addstr("\t")

    screen.addstr("Plus/Minus Symbol        ")
    screen.addch(curses.ACS_PLMINUS)
    screen.addstr("\n")

    screen.addstr("Bullet                   ")
    screen.addch(curses.ACS_BULLET)
    screen.addstr("\t")

    screen.addstr("Arrow Pointing Left      ")
    screen.addch(curses.ACS_LARROW)
    screen.addstr("\n")

    screen.addstr("Arrow Pointing Right     ")
    screen.addch(curses.ACS_RARROW)
    screen.addstr("\t")

    screen.addstr("Arrow Pointing Down      ")
    screen.addch(curses.ACS_DARROW)
    screen.addstr("\n")

    screen.addstr("Arrow Pointing Up        ")
    screen.addch(curses.ACS_UARROW)
    screen.addstr("\t")

    screen.addstr("Board of squares         ")
    screen.addch(curses.ACS_BOARD)
    screen.addstr("\n")

    screen.addstr("Lantern Symbol           ")
    screen.addch(curses.ACS_LANTERN)
    screen.addstr("\t")

    screen.addstr("Solid Square Block       ")
    screen.addch(curses.ACS_BLOCK)
    screen.addstr("\n")

    screen.addstr("Less/Equal sign          ")
    screen.addch(curses.ACS_LEQUAL)
    screen.addstr("\t")

    screen.addstr("Greater/Equal sign       ")
    screen.addch(curses.ACS_GEQUAL)
    screen.addstr("\n")

    screen.addstr("Pi                       ")
    screen.addch(curses.ACS_PI)
    screen.addstr("\t")

    screen.addstr("Not equal                ")
    screen.addch(curses.ACS_NEQUAL)
    screen.addstr("\n")

    screen.addstr("UK pound sign            ")
    screen.addch(curses.ACS_STERLING)
    screen.addstr("\n")

    screen.refresh()
    screen.getch()
    curses.endwin()

    sys.exit(0)


if __name__ == "__main__":
    main()
