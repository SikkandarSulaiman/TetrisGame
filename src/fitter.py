import time

from tetrimino import Piece
from panels import Field
from score import ScoreManager
from config_read import *

class PieceFitter:

	def __init__(self, field):
		self.field = field
		self.active_piece = None
		self.score_calc = ScoreManager()
	
	def spawn_new_piece(self):
		self.active_piece = Piece()
		self.active_piece.x, self.active_piece.y = 0, (self.field.width - TETRIMINO_WIDTH)//2 + 1
		if self.check_piece_fit(self.active_piece.x, self.active_piece.y):
			return True
		return False

	def check_piece_fit(self, x, y):
		for px, fx in enumerate(range(x, x + TETRIMINO_HEIGHT)):
			for py, fy in enumerate(range(y, y + TETRIMINO_WIDTH)):
				if self.active_piece.map[px][py] != CHAR_EMPTY_SPACE and self.field.map[fx][fy] != CHAR_EMPTY_SPACE:
					break
			if py < TETRIMINO_WIDTH - 1:
				break
		else:
			return True
		return False

	def place_piece_in_field(self):
		x, y = self.active_piece.x, self.active_piece.y
		for px, fx in enumerate(range(x, x + TETRIMINO_HEIGHT)):
			for py, fy in enumerate(range(y, y + TETRIMINO_WIDTH)):
				pc = self.active_piece.map[px][py]
				if pc != CHAR_EMPTY_SPACE:
					self.field.map[fx][fy] = pc

	def move_piece(self, dir):

		if dir == CMD_ROTATE:
			self.active_piece.rotate()
			if not self.check_piece_fit(self.active_piece.x, self.active_piece.y):
				self.active_piece.rotate_rev()
			return None

		px, py = self.active_piece.x, self.active_piece.y

		px, py = {
			CMD_RIGHT: (px, py + 2),
			CMD_LEFT: (px, py - 2),
			CMD_DOWN: (px + 1, py),
		}.get(dir, (px, py))

		if self.check_piece_fit(px, py):
			self.active_piece.x, self.active_piece.y = px, py
		elif dir == CMD_DOWN:
			self.score_calc.dropped_at_speed = 500
			self.place_piece_in_field()
			lc = self.field.find_lines()
			if lc:
				self.score_calc.lines_appeared = lc
				# self.field.print_panel(self.win)
				time.sleep(LINE_DISPLAY_MS / 1000)
				self.field.clear_lines()
			if not self.spawn_new_piece():
				return CMD_GAME_OVER
