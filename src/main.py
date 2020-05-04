import json

import curses

from fitter import PieceFitter
from panels import Field
from panels import ScoreBoard
from config_read import *

def main(stdscr):
	stdscr.clear()
	stdscr.nodelay(1)
	stdscr.timeout(INITIAL_SPEED_MS)
	curses.curs_set(0)
	
	pf = PieceFitter(Field(FIELD_WIDTH, FIELD_HEIGHT), stdscr)
	sb = ScoreBoard(SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT)
	sb.print_panel(stdscr)
	pf.spawn_new_piece()
	pf.print_field_piece()

	while True:
		key = stdscr.getch()
		dir = input_key_map.get(key, CMD_QUIT)

		if dir == CMD_QUIT or (x:=pf.move_piece(dir)) == CMD_GAME_OVER:
			break
		pf.print_field_piece()
		sb.update_score(stdscr)

	stdscr.refresh()


if __name__ == '__main__':

	NO_KEY_PRESS = -1
	input_key_map[NO_KEY_PRESS] = CMD_DOWN
	print(input_key_map)

	curses.wrapper(main)
