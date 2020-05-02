import random

from config_read import *

class Piece:

	shapes = {
		'I': [
				list(map(list, I_FACE_1)),
				list(map(list, '  []    \n  []    \n  []    \n  []    '.split('\n')))
			],
		'O': [
			list(map(list, '        \n  [][]  \n  [][]  \n        '.split('\n')))
		],
		'J': [
		  list(map(list, '    []  \n    []  \n  [][]  \n        '.split('\n'))),
		  list(map(list, '        \n  []    \n  [][][]\n        '.split('\n'))),
		  list(map(list, '  [][]  \n  []    \n  []    \n        '.split('\n'))),
		  list(map(list, '        \n  [][][]\n      []\n        '.split('\n')))  
		]
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


