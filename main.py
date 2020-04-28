import curses
import curses.panel as panel

def main(stdscr):
    stdscr.clear()

    stdscr.addstr(f'Hello, World!')

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)