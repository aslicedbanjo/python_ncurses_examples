#! /usr/bin/env python

# A Python port of Example 11 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/mouse.html
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

WIDTH = 30
HEIGHT = 10

startx = 0
starty = 0

choices = (
    "Choice 1",
    "Choice 2",
    "Choice 3",
    "Choice 4",
    "Exit",
)


def print_menu(menu_win, highlight):
    """ Print a menu
    """
    x = 2
    y = 2

    menu_win.box(0, 0)

    for index, choice in enumerate(choices):
        if highlight == index + 1:
            menu_win.attron(curses.A_REVERSE)
            menu_win.addstr(y, x, choice)
            menu_win.attroff(curses.A_REVERSE)
        else:
            menu_win.addstr(y, x, choice)
        y = y + 1

    menu_win.refresh()


def report_choice(mouse_x, mouse_y):
    """ Report the choice according to mouse position
    """
    i = startx + 2
    j = starty + 3

    n_choices = len(choices)
    p_choice = None

    for index, choice in enumerate(choices):
        if (mouse_y == j + index) and \
           (i <= mouse_x <= i + len(choice)):

            if index == n_choices - 1:
                p_choice = -1
            else:
                p_choice = index + 1
            break
    return p_choice


def main():
    """ Entry point for example 11
    """
    choice = 0

    # Initialize curses
    screen = curses.initscr()
    screen.clear()
    curses.noecho()
    curses.cbreak()  # Line buffering disabled. Pass on everything

    # Get all the mouse events
    curses.mousemask(curses.ALL_MOUSE_EVENTS)

    # Try to put the window in the middle of screen
    startx = (80 - WIDTH) // 2
    starty = (24 - HEIGHT) // 2

    screen.attron(curses.A_REVERSE)
    screen.addstr(23, 1, "Click on Exit to quit (Works best in a virtual console)")
    screen.refresh()
    screen.attroff(curses.A_REVERSE)

    # Create the menu window
    menu_win = curses.newwin(HEIGHT, WIDTH, starty, startx)

    # Enable mouse and keypad events on the menu window
    menu_win.keypad(True)

    # Print the menu for the first time
    print_menu(menu_win, 1)
    menu_y, menu_x = menu_win.getbegyx()

    while True:
        char = menu_win.getch()

        if char == curses.KEY_MOUSE:
            event = curses.getmouse()
            if event:
                (_, x, y, z, bstate) = event

                # When the user clicks the left mouse button and the location is
                # enclosed by the menu's entry
                if bstate & curses.BUTTON1_CLICKED and menu_win.enclose(y, x):
                    # In Python, we have to add-in the offset for the position
                    # of the menu's window
                    choice = report_choice(x - menu_x + 1, y - menu_y + 1)

                    if choice is None:
                        continue

                    if choice == -1:  # Exit chosen
                        break

                    fmtString = "Choice made is : {0} String Chosen is {1!r: >10}"
                    screen.addstr(
                        22, 1,
                        fmtString.format(choice, choices[choice - 1])
                    )

                    screen.refresh()

            print_menu(menu_win, choice)

    curses.endwin()
    sys.exit(0)


if __name__ == "__main__":
    main()
