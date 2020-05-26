import json

import curses

from score import ScoreManager
from fitter import PieceFitter
from panels import Field
from panels import ScoreBoard
from config_read import *

def main(stdscr):
	stdscr.clear()
	stdscr.nodelay(1)
	stdscr.timeout(INITIAL_SPEED_MS)
	curses.curs_set(0)
	
	tetris_field = Field(FIELD_WIDTH, FIELD_HEIGHT)
	pf = PieceFitter(tetris_field)
	sb = ScoreBoard(SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT)
	ScoreManager().set_scoreboard(sb)

	pf.spawn_new_piece()
	
	tetris_field.print_panel(stdscr)
	pf.active_piece.print_piece_in_field(stdscr, tetris_field)
	sb.print_panel(stdscr)

	while True:
		key = stdscr.getch()
		dir = input_key_map.get(key, CMD_QUIT)

		if dir == CMD_QUIT or pf.move_piece(dir) == CMD_GAME_OVER:
			break
		tetris_field.print_panel(stdscr)
		pf.active_piece.print_piece_in_field(stdscr, tetris_field)
		sb.print_panel(stdscr)

	stdscr.refresh()


if __name__ == '__main__':

	NO_KEY_PRESS = -1
	input_key_map[NO_KEY_PRESS] = CMD_DOWN

	curses.wrapper(main)
