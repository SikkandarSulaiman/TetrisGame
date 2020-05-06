import itertools

from score import ScoreManager
from config_read import *

class Panel:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def print_panel(self, win):
		for i, row in enumerate(self.map, self.x):
			win.addstr(i, self.y, ''.join(row))
		win.refresh()

	def place_text_in_line(self, text, line_num, align='center'):
		line = self.map[line_num]
		if align == 'left':
			pass
		elif align == 'center':
			for i, c in enumerate(text, (self.width - len(text))//2):
				line[i] = c
		elif align == 'right':
			pass
		self.map[line_num] = line



class Field(Panel):

	def __init__(self, width, height):
		super(Field, self).__init__(width, height)
		self.x = FIELD_PLACE_X
		self.y = FIELD_PLACE_Y
		self.create_panel()

	def create_panel(self):
		self.map = [list(CHAR_PANEL_WALL + CHAR_EMPTY_SPACE * (self.width - 2) + CHAR_PANEL_WALL) for i in range(self.height - 1)]
		self.map.append(list(CHAR_PANEL_WALL * self.width))

	def find_lines(self):
		line_count = 0
		for i, row in enumerate(self.map[:-1]):
			if ' ' not in (line:=''.join(row)):
				if line_count == 0:
					line_start = i
				line_count += 1
				self.map[i] = list(line.replace(CHAR_TET_BLOCK, CHAR_LINE*2))
		if line_count == 4:
			[self.place_text_in_line(MAGIC_WORD, line_start+i) for i in range(line_count)]
		return line_count

	def clear_lines(self):
		lines_removed_map = list(itertools.filterfalse(lambda r: '=' in ''.join(r), self.map[:-1]))
		lines_removed_map.append(self.map[-1])
		line_count = self.height-len(lines_removed_map)
		if line_count > 0:
			self.map = [list(CHAR_PANEL_WALL + CHAR_EMPTY_SPACE * (self.width - 2) + CHAR_PANEL_WALL) for i in range(line_count)]
			self.map.extend(lines_removed_map)

		
class ScoreBoard(Panel):

	def __init__(self, width, height):
		super(ScoreBoard, self).__init__(width, height)
		self.x = SCOREBOARD_PLACE_X
		self.y = SCOREBOARD_PLACE_Y
		self.create_panel()

	def create_panel(self):
		self.map = [list(CHAR_PANEL_WALL * self.width)]
		self.map.extend([list(CHAR_PANEL_WALL + CHAR_EMPTY_SPACE * (self.width - 2) + CHAR_PANEL_WALL) for i in range(self.height - 1)])
		self.map.append(list(CHAR_PANEL_WALL * self.width))
		self.place_text_in_line(SCOREBOARD_TEXT, self.height//2-1)

	def update_score(self, score):
		self.place_text_in_line(str(score), self.height//2+1)
		