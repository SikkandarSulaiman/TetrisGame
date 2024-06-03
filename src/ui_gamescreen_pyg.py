import pygame
from time import time, sleep

from config_read import *

@singleton
class pygame_GameScreen:

    def __init__(self):
        self.panel_list = []
        pygame.init()
        self.screen = pygame.display.set_mode([1800, 1500])
        self.screen.fill((0, 0, 0))
        self.font = pygame.font.SysFont('Monospace', 44)
        self.events = pygame.event.get()
        self.input_keys = []
        self.screen_quit = False
        self.fcw, self.fch = self.font.render(' ', 0, pygame.Color('White')).get_size()
        # fcw/h -> font char width/height
        self.key_map = {
            CMD_LEFT: False,
            CMD_RIGHT: False,
            CMD_DOWN: False,
            CMD_ROTATE: False,
            CMD_QUIT: False
        }

    def get_events(self):
        self.events = pygame.event.get()
        return self.events

    def filter_quit_event(self):
        for event in self.events:
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                return True
        return False
    
    def quit(self):
        pygame.quit()

    def print_panel(self, panel, offset=None):
        row_off, col_off = panel.row, panel.col
        for col, line in enumerate(panel.map):
            line = ''.join(line)
            word_surface = self.font.render(line, 0, pygame.Color('white'))
            self.screen.blit(word_surface, ((0+row_off)*self.fcw, (col+col_off)*self.fch))

    def print_piece_over_panel(self, piece, panel):
        for row_count, row in enumerate(piece.map):
            prow, pcol, frow, fcol = piece.row, piece.col, panel.row, panel.col
            piece_row = ''.join(row)
            word_surface = self.font.render(piece_row, 0, pygame.Color('white'))
            self.screen.blit(word_surface, ((piece.col + panel.col + 2)*self.fcw, (row_count + piece.row + panel.row - 2)*self.fch))

    def refresh(self):
        pygame.display.flip()
        self.screen.fill((0,0,0))

    def detect_input_keys(self, wait_ms=500):
        updated = False
        time_diff = 0
        last_time = time()
        while (not updated) and (time_diff < wait_ms):
            for event in self.get_events():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        self.key_map[CMD_ROTATE] = True
                    elif event.key == pygame.K_j:
                        self.key_map[CMD_LEFT] = True
                    elif event.key == pygame.K_k:
                        self.key_map[CMD_DOWN] = True
                    elif event.key == pygame.K_l:
                        self.key_map[CMD_RIGHT] = True
                    updated = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.key_map[CMD_QUIT] = True
                    elif event.key == pygame.K_i:
                        self.key_map[CMD_ROTATE] = False
                    elif event.key == pygame.K_j:
                        self.key_map[CMD_LEFT] = False
                    elif event.key == pygame.K_k:
                        self.key_map[CMD_DOWN] = False
                    elif event.key == pygame.K_l:
                        self.key_map[CMD_RIGHT] = False
                    updated = True
                elif event.type == pygame.QUIT:
                    self.key_map[CMD_QUIT] = True
                    updated = True
            time_diff = (time() - last_time)*1000
            # sleep(.001)
        return updated

