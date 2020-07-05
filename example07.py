#! /usr/bin/env python

# A Python port of Example 7 from
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


def create_newwin(height, width, starty, startx):
    """ Create a new window
    """
    local_win = curses.newwin(height, width, starty, startx)

    # 0, 0 gives default characters for the vertical and horizontal lines
    local_win.box(0, 0)
    local_win.refresh()  # Show the box
    return local_win


def destroy_win(local_win):
    """ Destroy a window
    """
    # box(local_win, ' ', ' ') : This won't produce the desired
    # result of erasing the window. It will leave its four corners
    # and so an ugly remnant of window.

    # Instead use the border() method
    local_win.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

    # The parameters taken are
    # 1. win: the window on which to operate
    # 2. ls: character to be used for the left side of the window
    # 3. rs: character to be used for the right side of the window
    # 4. ts: character to be used for the top side of the window
    # 5. bs: character to be used for the bottom side of the window
    # 6. tl: character to be used for the top left corner of the window
    # 7. tr: character to be used for the top right corner of the window
    # 8. bl: character to be used for the bottom left corner of the window
    # 9. br: character to be used for the bottom right corner of the window
    local_win.refresh()
    del local_win


def main():
    """ Entry point for example 7
    """
    screen = curses.initscr()  # Start curses mode
    curses.cbreak()  # Line buffering disabled, pass all characters to the program
    screen.keypad(True)

    height = 3
    width = 10

    lines, cols = screen.getmaxyx()
    starty = (lines - height) // 2  # Calculating for a center placement
    startx = (cols - width) // 2  # of the window

    screen.addstr("Press F2 to exit")
    screen.refresh()

    my_win = create_newwin(height, width, starty, startx)

    char = screen.getch()

    while char != curses.KEY_F2:
        if char == curses.KEY_LEFT:
            destroy_win(my_win)
            startx = startx - 1
            my_win = create_newwin(height, width, starty, startx)
        if char == curses.KEY_RIGHT:
            destroy_win(my_win)
            startx = startx + 1
            my_win = create_newwin(height, width, starty, startx)
        if char == curses.KEY_UP:
            destroy_win(my_win)
            starty = starty - 1
            my_win = create_newwin(height, width, starty, startx)
        if char == curses.KEY_DOWN:
            destroy_win(my_win)
            starty = starty + 1
            my_win = create_newwin(height, width, starty, startx)

        char = screen.getch()

    curses.endwin()  # End curses mode
    sys.exit(0)


if __name__ == "__main__":
    main()
