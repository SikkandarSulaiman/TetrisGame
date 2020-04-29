import curses
import curses.panel as panel

def main(stdscr):
    stdscr.clear()

    stdscr.addstr(f'Hello, World!')

    stdscr.refresh()
    stdscr.getkey()

# curses.wrapper(main)




class Piece:

	def __init__(self):
		self.map = '    \n*   \n*** \n    '


class Field:

	def __init__(self, **kwargs):
		try:
			self.createField(kwargs['width'], kwargs['height'])
		except KeyError:
			pass

	def create_field(self, width, height):
		self.map = ['#'+' '*(width-2)+'#' for i in range(height-1)]
		self.map.append('#'*width)
		self.height = height
		self.width = width


class PieceFitter:

	def __init__(self, field):
		self.field = field
		self.prev_x = (field.width - 4)/2
		self.prev_y = 0
		self.active_piece = None

	def set_active_piece(self, piece):
		self.active_piece = piece

	def get_active_piece(self):
		return self.active_piece
	
	def spawn_new_piece(self):
		pass

	def place_piece_in_field(self, x, y):
		pass

	def remove_piece_from_field(self):
		pass


	
	# for f_row_i, f_row in enumerate(field[y:y+piece_H]):
	# 	for f_col_i, f_col_e in enumerate(f_row[x:x+piece_W]):






for i in Field(width=20, height=80).map:
	print(i)

