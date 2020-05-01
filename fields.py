import itertools

class Field:

	def __init__(self, **kwargs):
		
		try:
			self.create_field(kwargs['width'], kwargs['height'])
		except KeyError:
			pass

	def create_field(self, width, height):
		self.map = [list('#'+' '*(2*width-2)+'#') for i in range(height-1)]
		self.map.append(list('#'*width*2))
		self.height = height
		self.width = width

	def find_lines(self):
		line_count = 0
		for i, row in enumerate(self.map[:-1]):
			if ' ' not in (line:=''.join(row)):
				if line_count == 0:
					line_start = i
				line_count += 1
				self.map[i] = list(line.replace('[]', '=='))
		if line_count == 4:
			self.map[line_start + 1] = '#'+'='*(self.width-3-1)+'TETRIS'+'='*(self.width-3-1)+'#'
		return line_count

	def clear_lines(self):
		lines_removed_map = list(itertools.filterfalse(lambda r: '=' in ''.join(r), self.map[:-1]))
		lines_removed_map.append(self.map[-1])
		line_count = self.height-len(lines_removed_map)
		if line_count > 0:
			self.map = [list('#'+' '*(2*self.width-2)+'#') for i in range(line_count)]
			self.map.extend(lines_removed_map)

