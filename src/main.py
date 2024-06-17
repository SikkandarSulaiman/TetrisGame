import time
import random
import pygame

from score import ScoreManager
from fitter import PieceFitter
from panels import Field
from panels import ScoreBoard
from config_read import *
from ui_gamescreen_pyg import pygame_GameScreen

if __name__ == '__main__':

	scr = pygame_GameScreen()

	tetris_field = Field(FIELD_WIDTH, FIELD_HEIGHT)
	pf = PieceFitter(tetris_field)
	# sb = ScoreBoard(SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT)
	# ScoreManager().set_scoreboard(sb)

	pf.spawn_new_piece()
	scr.print_panel(tetris_field)
	# sb.print_panel(scr)

	loop_end_time = 0
	last_cmddown_time = 0
	running = True
	while running:

		# Record loop duration
		loop_start_time = time.time()
		last_cmddown_time += (loop_end_time)

		# Read input
		key_detected = scr.detect_input_keys(INITIAL_SPEED_MS)

		# Process input
		if not pf.frr: # check Field Refresh Request
			if last_cmddown_time >= INITIAL_SPEED_MS:
				pf.move_piece(CMD_DOWN)
				last_cmddown_time = 0
			for k,v in scr.key_map.items():
				if v:
					if k == CMD_QUIT:
						running = False
						break
					else:
						pf.move_piece(k)
		elif pf.move_piece_refresh() == CMD_GAME_OVER:
			print('GAME OVER DETECTED')
			break

		# Update output
		scr.print_panel(tetris_field)
		if pf.frr: continue
		scr.print_piece_over_panel(pf.active_piece, tetris_field)
		scr.refresh()
		
		# update loop duration
		loop_end_time = (time.time() - loop_start_time)*1000

	scr.quit()




