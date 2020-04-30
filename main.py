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
		self.map = list(map(list, '    \n*   \n*** \n    '.split('\n')))


class Field:

	def __init__(self, **kwargs):
		try:
			self.create_field(kwargs['width'], kwargs['height'])
		except KeyError:
			pass

	def create_field(self, width, height):
		self.map = [list('#'+' '*(width-2)+'#') for i in range(height-1)]
		self.map.append(list('#'*width))
		self.height = height
		self.width = width


class PieceFitter:

	def __init__(self, field):
		self.field = field
		self.cur_x = 0
		self.cur_y = 0
		self.prev_x = 0
		self.prev_y = 0
		self.active_piece = None

	def set_active_piece(self, piece):
		self.active_piece = piece

	def get_active_piece(self):
		return self.active_piece
	
	def spawn_new_piece(self):
		self.active_piece = Piece()
		x = self.cur_x = self.prev_x = 0
		y = self.cur_y = self.prev_y = (self.field.width - 4)//2
		if self.check_piece_fit(x, y):
			self.place_piece_in_field()
		else:
			pass
			# Game over

	def check_piece_fit(self, x, y):
		for px, fx in enumerate(range(x,x+4)):
			for py, fy in enumerate(range(y,y+4)):
				if self.active_piece.map[px][py] != ' ' and self.field.map[fx][fy] != ' ':
					print(f'breaking fx {fx} fy {fy}')
					print(f'breaking px {px} py {py}')
					break
			if py < 3:
				print(f'broke {fx} {fy}')
				break
		else:
			return True
		return False

	def place_piece_in_field(self):
		for px, fx in enumerate(range(self.cur_x, self.cur_x+4)):
			for py, fy in enumerate(range(self.cur_y, self.cur_y+4)):
				if (pc := self.active_piece.map[px][py]) == '*':
					self.field.map[fx][fy] = pc

	def remove_piece_from_field(self):
		for px, fx in enumerate(range(self.prev_x,self.prev_x+4)):
			for py, fy in enumerate(range(self.prev_y,self.prev_y+4)):
				if self.active_piece.map[px][py] == '*':
					self.field.map[fx][fy] = ' '

	def move_piece_right(self):
		x = self.cur_x + 1
		if self.check_piece_fit(x, self.cur_y):
			self.cur_x = x
			self.remove_piece_from_field()
			self.place_piece_in_field()
			self.prev_x = x



if __name__ == '__main__':
	f = Field(width=20, height=80)
	pf = PieceFitter(f)
	pf.spawn_new_piece()

	for i in f.map:
		print(i)

	pf.move_piece_right()

	for i in f.map:
		print(i)

