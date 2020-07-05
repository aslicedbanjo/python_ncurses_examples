#! /usr/bin/env python

# A Python port of Example 16 from
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


class PANEL_DATA(object):
    def __init__(self, x, y, w, h, label, label_color, next_=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.label = label
        self.label_color = label_color
        self.next_ = next_


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


def init_wins(num):
    """ Create all the windows
    """
    wins = []
    y = 2
    x = 10

    for i in range(num):
        win = curses.newwin(NLINES, NCOLS, y, x)
        wins.append(win)
        win_show(win, "Window Number %d" % (i + 1,), i + 1)
        y += 3
        x += 7

    return wins


def set_user_ptrs(panels, num):
    """ Set the PANEL_DATA structures for individual panels
    """
    ptrs = []
    for i in range(num):
        win = panels[i].window()
        y, x = win.getbegyx()
        h, w = win.getmaxyx()

        panel_data = PANEL_DATA(x, y, w, h, "Window Number %d" % (i + 1,), i + 1)

        panel_data.next_ = panels[(i + 1) % num]
        ptrs.append(panel_data)

        panels[i].set_userptr(ptrs[i])


def main():
    """ Entry point for example 16
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

    # Attach a panel to each window, order is bottom up
    my_panels = (
        panel.new_panel(my_wins[0]),  # Push 0, order: stdscr-0
        panel.new_panel(my_wins[1]),  # Push 1, order: stdscr-0-1
        panel.new_panel(my_wins[2]),  # Push 2, order: stdscr-0-1-2
    )

    set_user_ptrs(my_panels, len(my_panels))

    # Update the stacking order. 2nd panel will be on top
    panel.update_panels()

    # Show it on the screen
    screen.attron(curses.color_pair(4))
    screen.addstr(curses.LINES - 3, 0, "Use 'm' for moving, 'r' for resizing")
    screen.addstr(curses.LINES - 2, 0, "Use tab to browse through the windows (F2 to Exit)")
    screen.attroff(curses.color_pair(4))
    curses.doupdate()

    stack_top = my_panels[2]
    top = stack_top.userptr()
    newx = top.x
    newy = top.y
    neww = top.w
    newh = top.h

    char = screen.getch()  # Note this is an integer - the ANSI character code

    size = False
    move = False

    while char != curses.KEY_F2:
        if char == ord("\t"):  # Tab
            top = stack_top.userptr()
            top.next_.top()
            stack_top = top.next_
            top = stack_top.userptr()
            newx = top.x
            newy = top.y
            neww = top.w
            newh = top.h

        elif char == ord("r"):  # Re-size
            size = True
            screen.attron(curses.color_pair(4))
            resize_msg = "Entered Resizing: Use Arrow Keys " \
                "to resize and press <ENTER> to end resizing"
            screen.addstr(curses.LINES - 4, 0, resize_msg)
            screen.refresh()
            screen.attroff(curses.color_pair(4))

        elif char == ord("m"):  # Move
            screen.attron(curses.color_pair(4))
            mv_msg = "Entered Moving: Use Arrow Keys to Move and press <ENTER> to end moving"
            screen.addstr(curses.LINES - 4, 0, mv_msg)
            screen.refresh()
            screen.attroff(curses.color_pair(4))
            move = True

        elif char == curses.KEY_LEFT:
            if size:
                newx = newx - 1
                neww = neww + 1

            if move:
                newx = newx - 1

        elif char == curses.KEY_RIGHT:
            if size:
                newx = newx + 1
                neww = neww - 1

            if move:
                newx = newx + 1

        elif char == curses.KEY_UP:
            if size:
                newy = newy - 1
                newh = newh + 1

            if move:
                newy = newy - 1

        elif char == curses.KEY_DOWN:
            if size:
                newy = newy + 1
                newh = newh - 1

            if move:
                newy = newy + 1

        elif char == ord("\n"):  # Enter
            screen.move(curses.LINES - 4, 0)
            screen.clrtoeol()
            screen.refresh()

            if size:
                old_win = stack_top.window()
                temp_win = curses.newwin(newh, neww, newy, newx)
                stack_top.replace(temp_win)
                win_show(temp_win, top.label, top.label_color)
                del old_win
                size = False

            if move:
                stack_top.move(newy, newx)
                move = False

        screen.attron(curses.color_pair(4))
        screen.addstr(curses.LINES - 3, 0, "Use 'm' for moving, 'r' for resizing")
        screen.addstr(curses.LINES - 2, 0, "Use tab to browse through the windows (F2 to Exit)")
        screen.attroff(curses.color_pair(4))
        screen.refresh()
        panel.update_panels()
        curses.doupdate()

        char = screen.getch()

    curses.endwin()
    sys.exit(0)


if __name__ == "__main__":
    main()
