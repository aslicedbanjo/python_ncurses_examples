#! /usr/bin/env python

# A Python port of Example 14 from
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


def main():
    """ Entry point for example 14
    """
    lines, cols, y, x = 10, 40, 2, 4

    screen = curses.initscr()
    curses.cbreak()
    curses.noecho()

    # Create windows for the panels
    my_wins = (
        curses.newwin(lines, cols, y, x),
        curses.newwin(lines, cols, y + 1, x + 5),
        curses.newwin(lines, cols, y + 2, x + 10),
    )

    # Create borders around the windows so that you can see the effect of panels
    for my_win in my_wins:
        my_win.box(0, 0)

    # Attach a panel to each window; order is bottom up
    # The panels aren't used, but we need to keep references to
    # them around, otherwise they are cleaned up too early and
    # nothing is shown.
    _ = (
        panel.new_panel(my_wins[0]),  # Push 0, order: stdscr-0
        panel.new_panel(my_wins[1]),  # Push 1, order: stdscr-0-1
        panel.new_panel(my_wins[2]),  # Push 2, order: stdscr-0-1-2
    )

    # Update the stacking order. 2nd panel will be on top
    panel.update_panels()

    # Show it on the screen
    curses.doupdate()

    screen.getch()
    curses.endwin()

    sys.exit(0)


if __name__ == "__main__":
    main()
