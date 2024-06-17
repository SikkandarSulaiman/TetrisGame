import time

from tetrimino import Piece
from score import ScoreManager
from config_read import *

class PieceFitter:

	def __init__(self, field):
		self.frr = False
		self.field = field
		self.active_piece = None
		self.score_calc = ScoreManager()
		self.move_piece_refresh = None
	
	def spawn_new_piece(self):
		self.active_piece = Piece()
		self.active_piece.row, self.active_piece.col = 0, (self.field.width - TETRIMINO_WIDTH)//2 + 1
		if self.check_piece_fit(self.active_piece.row, self.active_piece.col):
			return True
		return False

	def check_piece_fit(self, prow_start, pcol_start):
		for prow, frow in enumerate(range(prow_start, prow_start + TETRIMINO_HEIGHT)):
			for pcol, fcol in enumerate(range(pcol_start, pcol_start + TETRIMINO_WIDTH)):
				if self.active_piece.map[prow][pcol] != CHAR_EMPTY_SPACE and self.field.map[frow][fcol] != CHAR_EMPTY_SPACE:
					break
			if pcol < TETRIMINO_WIDTH - 1:
				break
		else:
			return True
		return False

	def attach_piece_to_field(self):
		prow_start, pcol_start = self.active_piece.row, self.active_piece.col
		for prow, frow in enumerate(range(prow_start, prow_start + TETRIMINO_HEIGHT)):
			for pcol, fcol in enumerate(range(pcol_start, pcol_start + TETRIMINO_WIDTH)):
				if (pchar := self.active_piece.map[prow][pcol]) != CHAR_EMPTY_SPACE:
					self.field.map[frow][fcol] = pchar

	def move_piece(self, dir):
		if dir == CMD_ROTATE:
			self.active_piece.rotate()
			if not self.check_piece_fit(self.active_piece.row, self.active_piece.col):
				self.active_piece.rotate_rev()
			return None

		prow, pcol = self.active_piece.row, self.active_piece.col
		prow, pcol = {
			CMD_RIGHT: (prow, pcol + 2),
			CMD_LEFT: (prow, pcol - 2),
			CMD_DOWN: (prow + 1, pcol),
		}.get(dir, (prow, pcol))

		if self.check_piece_fit(prow, pcol):
			self.active_piece.row, self.active_piece.col = prow, pcol
		elif dir == CMD_DOWN:
			self.score_calc.dropped_at_speed = 500
			self.attach_piece_to_field()
			self.frr = True
			self.move_piece_refresh = self._move_piece_spawn_new
			if lc := self.field.find_lines():
				self.score_calc.lines_appeared = lc
				self.move_piece_refresh = self._move_piece_indicate_lines

	def _move_piece_indicate_lines(self):
		time.sleep(LINE_DISPLAY_MS / 1000)
		self.field.clear_lines()
		self.frr = True
		self.move_piece_refresh = self._move_piece_spawn_new

	def _move_piece_spawn_new(self):
		self.frr = False
		self.move_piece_refresh = None
		if not self.spawn_new_piece():
			return CMD_GAME_OVER
