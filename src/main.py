import pygame

from score import ScoreManager
from fitter import PieceFitter
from panels import Field
from panels import ScoreBoard
from config_read import *

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

	pygame.init()
	game_screen = pygame.display.set_mode([1500, 1500])

	# Run until the user asks to quit
	running = True
	while running:

		# Did the user click the window close button?
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Fill the background with white
		game_screen.fill((0, 0, 0))

		tetris_field = Field(FIELD_WIDTH, FIELD_HEIGHT)

		font = pygame.font.SysFont('Monospace', 44)
		pos_x, pos_y = 0, 0
		for line in tetris_field.map:
			line = ''.join(line)
			word_surface = font.render(line, 0, pygame.Color('white'))
			text_w, text_h = word_surface.get_size()
			game_screen.blit(word_surface, (0,pos_y))
			pos_y += text_h

		# Flip the display
		pygame.display.flip()

	# Done! Time to quit.
	pygame.quit()

	# curses.wrapper(cur_main)




