import pygame

from score import ScoreManager
from fitter import PieceFitter
from panels import Field
from panels import ScoreBoard
from config_read import *
from ui_gamescreen_pyg import pygame_GameScreen

from time import sleep

def cur_main(stdscr):
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

		if not pf.frr: # check Field Refresh Request
			key = stdscr.getch()
			dir = input_key_map.get(key, CMD_QUIT)
			if dir == CMD_QUIT:
				break
			pf.move_piece(dir)
		elif pf.move_piece_refresh() == CMD_GAME_OVER:
			break

		tetris_field.print_panel(stdscr)
		if pf.frr: continue
		pf.active_piece.print_piece_in_field(stdscr, tetris_field)
		sb.print_panel(stdscr)

	stdscr.refresh()


if __name__ == '__main__':

	NO_KEY_PRESS = -1
	input_key_map[NO_KEY_PRESS] = CMD_DOWN

	scr = pygame_GameScreen()

	tetris_field = Field(FIELD_WIDTH, FIELD_HEIGHT)
	pf = PieceFitter(tetris_field)
	sb = ScoreBoard(SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT)
	ScoreManager().set_scoreboard(sb)

	pf.spawn_new_piece()
	# scr.print_panel(tetris_field)
	# scr.print_piece_inside_panel(pf.active_piece, tetris_field)
	# pf.active_piece.print_piece_in_field(scr, tetris_field)
	# sb.print_panel(scr)

	running = True
	while running:

		if scr.is_quit_event():
			running = False

		pf.move_piece(CMD_DOWN)

		scr.print_panel(tetris_field)
		scr.print_piece_over_panel(pf.active_piece, tetris_field)
		scr.refresh()
		# sleep(1)

	scr.quit()




