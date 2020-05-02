import json

import curses

from fitter import PieceFitter
from fields import Field
from config_read import *

def main(stdscr):
	stdscr.clear()
	stdscr.nodelay(1)
	stdscr.timeout(INITIAL_SPEED_MS)
	curses.curs_set(0)
	
	pf = PieceFitter(Field(width=FIELD_WIDTH, height=FIELD_HEIGHT), stdscr)
	pf.spawn_new_piece()

	while True:
		pf.print_field_piece()
		key = stdscr.getch()
		dir = input_key_map.get(key, CMD_QUIT)

		if dir == CMD_QUIT or (x:=pf.move_piece(dir)) == CMD_GAME_OVER:
			break

	stdscr.refresh()


if __name__ == '__main__':

	NO_KEY_PRESS = -1
	input_key_map[NO_KEY_PRESS] = CMD_DOWN
	print(input_key_map)

	curses.wrapper(main)
