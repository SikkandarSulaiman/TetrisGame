from config_read import singleton

@singleton
class ScoreManager:

	def __init__(self):
		self._score = 0
		self._dropped_at_speed = 0
		self._lines_appeared = 0

	@property
	def score(self):
		return self._score

	@property
	def dropped_at_speed(self):
		pass
	
	@dropped_at_speed.setter
	def dropped_at_speed(self, speed):
		self._score += ((1000-speed)//100)

	@property
	def lines_appeared(self):
		pass

	@lines_appeared.setter
	def lines_appeared(self, line_count):
		self._score += (2**line_count*10)
		self._lines_appeared += line_count
