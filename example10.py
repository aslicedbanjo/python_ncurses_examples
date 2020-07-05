#! /usr/bin/env python

# A Python port of Example 10 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/keys.html
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

# Constants
WIDTH = 30
HEIGHT = 10

choices = (
    "Choice 1",
    "Choice 2",
    "Choice 3",
    "Choice 4",
    "Exit",
)


def print_menu(menu_win, highlight):
    """ Draw a menu
    """
    x = 2
    y = 2
    menu_win.box(0, 0)

    for index, choice in enumerate(choices):
        if highlight == index + 1:  # High light the present choice
            menu_win.attron(curses.A_REVERSE)
            menu_win.addstr(y, x, choice)
            menu_win.attroff(curses.A_REVERSE)
        else:
            menu_win.addstr(y, x, choice)
        y = y + 1

    menu_win.refresh()


def main():
    """ Entry point for example 10
    """
    highlight = 1
    choice = 0

    screen = curses.initscr()
    screen.clear()
    curses.noecho()

    curses.cbreak()  # Line buffering disabled. pass on everything
    startx = (80 - WIDTH) // 2
    starty = (24 - HEIGHT) // 2

    menu_win = curses.newwin(HEIGHT, WIDTH, starty, startx)
    menu_win.keypad(True)

    screen.addstr(0, 0, "Use arrow keys to go up and down, Press enter to select a choice")
    screen.refresh()

    print_menu(menu_win, highlight)

    n_choices = len(choices)

    while True:
        char = menu_win.getch()

        if char == curses.KEY_UP:
            if highlight == 1:
                highlight = n_choices
            else:
                highlight = highlight - 1
        elif char == curses.KEY_DOWN:
            if highlight == n_choices:
                highlight = 1
            else:
                highlight = highlight + 1
        elif char == ord("\n"):  # Enter
            choice = highlight
        else:
            screen.addstr(24, 0, "Character pressed is = %s Hopefully it can be printed as %r" % (char, chr(char)))
            screen.refresh()

        print_menu(menu_win, highlight)

        if choice != 0:  # User made a choice to end the infinite loop
            break

    screen.addstr(23, 0, "You chose choice %r with choice string %r\n" % (choice, choices[choice - 1]))
    screen.clrtoeol()

    screen.refresh()
    screen.getch()
    curses.endwin()

    sys.exit(0)


if __name__ == "__main__":
    main()
