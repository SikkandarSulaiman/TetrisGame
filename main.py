import curses

from fitter import PieceFitter
from fields import Field

def main(stdscr):
	stdscr.clear()
	stdscr.nodelay(1)
	stdscr.timeout(1000)
	curses.curs_set(0)
	
	pf = PieceFitter(Field(width=16, height=30), stdscr)
	pf.spawn_new_piece()

	while True:
		pf.print_field_piece()
		key = stdscr.getch()
		dir = {
			ord('4'): 'left',
			ord('6'): 'right',
			ord('5'): 'down',
			-1: 'down',
			ord('8'): 'rotate'
		}.get(key, 'quit')

		if dir == 'quit' or (x:=pf.move_piece(dir)) == 'Game over':
			break

	stdscr.refresh()


if __name__ == '__main__':
	curses.wrapper(main)
