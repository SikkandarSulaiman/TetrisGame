import random

from config_read import *

class Piece:


	shapes = {
		'I': [*[[list(s) for s in i] for i in I_FACES]],
		'J': [*[[list(s) for s in i] for i in J_FACES]],
		'L': [*[[list(s) for s in i] for i in L_FACES]],
		'O': [*[[list(s) for s in i] for i in O_FACES]],
		'S': [*[[list(s) for s in i] for i in S_FACES]],
		'Z': [*[[list(s) for s in i] for i in Z_FACES]],
		'T': [*[[list(s) for s in i] for i in T_FACES]],
	}

	def __init__(self, shape=None, orient=None):
		self.shape_list = self.shapes[random.choice(list(self.shapes.keys()))]
		self.orient = random.randint(0, len(self.shape_list) - 1)
		self.map = self.shape_list[self.orient]

	def rotate(self):
		try:
			self.orient += 1
			self.map = self.shape_list[self.orient]
		except IndexError:
			self.orient = 0
			self.map = self.shape_list[self.orient]

	def rotate_rev(self):
		try:
			self.orient -= 1
			self.map = self.shape_list[self.orient]
		except IndexError:
			self.orient = len(self.shape_list) - 1
			self.map = self.shape_list[self.orient]

	def print_piece(self, win, x, y):
		for i, row in enumerate(self.map, x):
			rc = ''.join(row)
			for y_off, c in enumerate(rc, y):
				if c != CHAR_EMPTY_SPACE: 
					win.addstr(i, y_off, c)
		win.refresh()
