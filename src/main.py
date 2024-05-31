import random
import pygame

from score import ScoreManager
from fitter import PieceFitter
from panels import Field
from panels import ScoreBoard
from config_read import *
from ui_gamescreen_pyg import pygame_GameScreen

from time import time, sleep

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
	scr.print_panel(tetris_field)
	# sb.print_panel(scr)

	last_time = time()
	running = True
	while running:

		cur_time = time()
		time_diff_in_ms = (cur_time-last_time)*1000
		if time_diff_in_ms < 50:
			continue
		last_time = time()

		if scr.is_quit_event():
			running = False

		if not pf.frr: # check Field Refresh Request
			pf.move_piece(random.choice([CMD_DOWN]))
		elif pf.move_piece_refresh() == CMD_GAME_OVER:
			print('GAME OVER DETECTED')
			break

		scr.print_panel(tetris_field)
		if pf.frr: continue
		scr.print_piece_over_panel(pf.active_piece, tetris_field)
		scr.refresh()

	scr.quit()




