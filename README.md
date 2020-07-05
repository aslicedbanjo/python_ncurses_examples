Python `ncurses` examples
-------------------------

This repository contains my ports of the C ncurses examples from
http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/index.html using Python and
its `curses` module.

The C examples didn't have a license, so I am releasing these Python ports
under the GPLv3 license. If anyone knows this to be wrong, please let me know
and I will correct it.

I have only ported examples 1 to 17 inclusive, as the subsequent examples make
use of the menu and forms libraries and these are not exposed in the Python
`curses` module.

Several of the C examples use F1 to exit the application. However, in many
terminal emulators such as Gnome Terminal and Konsole F1 will launch the
terminal emulator help leaving the example application running. I have
therefore changed the exit key to F2 in those examples.

Homepage: https://github.com/aslicedbanjo/python_ncurses_examples 

As of January 2016, the ports have been updated to work with both Python 2.x
and Python 3.x. In the course of making the updates, I have improved PEP8
compliance, reduced PyLint violations, and made some of the examples more
Pythonic. Making the un-Pythonic parts Pythonic is left as an exercise for
the reader ;-)

Previously, example 11 (which demonstrates mouse click events) simply didn't
work, with clicks being ignored. I have now fixed this problem and it works
correctly. I assume this was an error in the original C version.

Copyright
---------

All Python files are Copyright (C) Dan Jacobs 2013 - 2016, 2020
under the GNU GPL v3 license. See the file LICENSE for more details.

Installation
------------

None as such. Just clone the repository (or download the zip and
unpack it), and run

	python exampleNN.py

in the top-level directory.

Example 5 requires a single command line argument, which should be a path to a
C file.

Documentation
-------------

See the corresponding C example from
http://www.tldp.org/HOWTO/NCURSES-Programming-HOWTO/index.html

Known Issues
------------

A couple of the examples have small problems, which are detailed below.

Example 5: reads a C file and echoes it back to stdout making comments bold. In
some terminals, lines above the current line disappear. The C version behaves
the same way.

Example 16: there is a bug when resizing a window, it is not redrawn
immediately.

In either case, I haven't been able to track down the problem. Any fixes will
be gratefully accepted.
