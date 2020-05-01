import time

from tetrimino import Piece
from fields import Field

class PieceFitter:

	def __init__(self, field, win):
		self.win = win
		self.field = field
		self.field_x, self.field_y = 3, 23
		self.x = 0
		self.y = 0
		self.active_piece = None

	def get_piece(self):
		return (self.active_piece, self.x, self.y)
	
	def spawn_new_piece(self):
		self.active_piece = Piece()
		x = self.x = 0
		y = self.y = (self.field.width - 4)+1
		if self.check_piece_fit(x, y):
			return True
		return False

	def check_piece_fit(self, x, y):
		for px, fx in enumerate(range(x,x+4)):
			for py, fy in enumerate(range(y,y+4*2)):
				if self.active_piece.map[px][py] != ' ' and self.field.map[fx][fy] != ' ':
					break
			if py < 3*2+1:
				break
		else:
			return True
		return False

	def place_piece_in_field(self):
		for px, fx in enumerate(range(self.x, self.x+4)):
			for py, fy in enumerate(range(self.y, self.y+4*2)):
				if (pc := self.active_piece.map[px][py]) != ' ':
					self.field.map[fx][fy] = pc

	def print_field(self):
		for i, row in enumerate(self.field.map, self.field_x):
			self.win.addstr(i, self.field_y, ''.join(row))
		self.win.refresh()

	def print_field_piece(self):
		self.print_field()
		for i, row in enumerate(self.active_piece.map, self.field_x + self.x):
			rc = ''.join(row)
			for y, c in enumerate(rc, self.field_y + self.y):
				if c != ' ': 
					self.win.addstr(i, y, c)
		self.win.refresh()

	def move_piece(self, dir):
		if dir == 'rotate':
			self.active_piece.rotate()
			if self.check_piece_fit(self.x, self.y):
				return self.active_piece, self.x, self.y
			self.active_piece.rotate_rev()
			return None

		x, y = {
			'right': (self.x, self.y+2),
			'left': (self.x, self.y-2),
			'down': (self.x+1, self.y),
		}.get(dir, (self.x, self.y))

		if self.check_piece_fit(x, y):
			self.x, self.y = x, y
		elif dir=='down':
			self.place_piece_in_field()
			if self.field.find_lines():
				self.print_field()
				time.sleep(0.5)
				self.field.clear_lines()
			if not self.spawn_new_piece():
				return 'Game over'
