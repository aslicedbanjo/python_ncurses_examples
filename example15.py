#! /usr/bin/env python

# A Python port of Example 15 from
# http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/panels.html
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
from curses import panel
import sys

NLINES = 10
NCOLS = 40


def print_in_middle(win, starty, startx, width, string, color):
    """ Print a string in the middle of a window
    """
    y, x = win.getyx()

    if startx != 0:
        x = startx

    if starty != 0:
        y = starty

    if width == 0:
        width = 80

    length = len(string)
    temp = (width - length) // 2
    x = startx + temp
    win.attron(color)
    win.addstr(y, x, string)
    win.attroff(color)
    win.refresh()


def win_show(win, label, label_color):
    """ Show the window with a border and a label
    """
    starty, startx = win.getbegyx()
    height, width = win.getmaxyx()

    win.box(0, 0)
    win.addch(2, 0, curses.ACS_LTEE)
    win.hline(2, 1, curses.ACS_HLINE, width - 2)
    win.addch(2, width - 1, curses.ACS_RTEE)

    print_in_middle(win, 1, 0, width, label, curses.color_pair(label_color))


# Create all the windows
def init_wins(n):
    wins = []
    y, x = 2, 10

    for i in range(1, n + 1):
        win = curses.newwin(NLINES, NCOLS, y, x)
        wins.append(win)
        win_show(win, "Window Number %d" % (i,), i)
        y += 3
        x += 7
    return wins


def main():
    """ Entry point for example 15
    """
    # Initialize curses
    screen = curses.initscr()

    curses.start_color()
    curses.cbreak()
    curses.noecho()
    screen.keypad(True)

    # Initialize all the colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)

    my_wins = init_wins(3)

    # Attach a panel to each window. Order is bottom up
    my_panels = (
        panel.new_panel(my_wins[0]),  # Push 0, order: stdscr-0
        panel.new_panel(my_wins[1]),  # Push 1, order: stdscr-0-1
        panel.new_panel(my_wins[2]),  # Push 2, order: stdscr-0-1-2
    )

    # Set up the user pointers to the next panel
    my_panels[0].set_userptr(my_panels[1])
    my_panels[1].set_userptr(my_panels[2])
    my_panels[2].set_userptr(my_panels[0])

    # Update the stacking order. 2nd panel will be on top
    panel.update_panels()

    # Show it on the screen
    screen.attron(curses.color_pair(4))
    screen.addstr(curses.LINES - 2, 0, "Use tab to browse through the windows (F2 to Exit)")
    screen.attroff(curses.color_pair(4))
    curses.doupdate()

    top = my_panels[2]
    char = screen.getch()
    while char != curses.KEY_F2:
        if char == ord("\t"):
            top = top.userptr()
            top.top()

        panel.update_panels()
        curses.doupdate()
        char = screen.getch()

    curses.endwin()
    sys.exit(0)


if __name__ == "__main__":
    main()
