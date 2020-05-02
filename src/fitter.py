import time

from tetrimino import Piece
from fields import Field
from config_read import *

class PieceFitter:

	def __init__(self, field, win):
		self.win = win
		self.field = field
		self.x, self.y = 0, 0
		self.active_piece = None

	def get_piece(self):
		return (self.active_piece, self.x, self.y)
	
	def spawn_new_piece(self):
		self.active_piece = Piece()
		x = self.x = 0
		y = self.y = (self.field.width - TETRIMINO_WIDTH) + 1
		if self.check_piece_fit(x, y):
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
		for px, fx in enumerate(range(self.x, self.x + TETRIMINO_HEIGHT)):
			for py, fy in enumerate(range(self.y, self.y + TETRIMINO_WIDTH)):
				if (pc := self.active_piece.map[px][py]) != CHAR_EMPTY_SPACE:
					self.field.map[fx][fy] = pc

	def print_field(self):
		for i, row in enumerate(self.field.map, FIELD_PLACE_X):
			self.win.addstr(i, FIELD_PLACE_Y, ''.join(row))
		self.win.refresh()

	def print_field_piece(self):
		self.print_field()
		for i, row in enumerate(self.active_piece.map, FIELD_PLACE_X + self.x):
			rc = ''.join(row)
			for y, c in enumerate(rc, FIELD_PLACE_Y + self.y):
				if c != CHAR_EMPTY_SPACE: 
					self.win.addstr(i, y, c)
		self.win.refresh()

	def move_piece(self, dir):
		if dir == CMD_ROTATE:
			self.active_piece.rotate()
			if self.check_piece_fit(self.x, self.y):
				return self.active_piece, self.x, self.y
			self.active_piece.rotate_rev()

		x, y = {
			CMD_RIGHT: (self.x, self.y + 2),
			CMD_LEFT: (self.x, self.y - 2),
			CMD_DOWN: (self.x + 1, self.y),
		}.get(dir, (self.x, self.y))

		if self.check_piece_fit(x, y):
			self.x, self.y = x, y
		elif dir == CMD_DOWN:
			self.place_piece_in_field()
			if self.field.find_lines():
				self.print_field()
				time.sleep(LINE_DISPLAY_MS / 1000)
				self.field.clear_lines()
			if not self.spawn_new_piece():
				return CMD_GAME_OVER
