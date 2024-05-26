import pygame

from config_read import *

@singleton
class pygame_GameScreen:

    def __init__(self):
        self. panel_list = []
        pygame.init()
        self.screen = pygame.display.set_mode([1800, 1500])
        self.screen.fill((0, 0, 0))
        self.font = pygame.font.SysFont('Monospace', 44)
        self.fcw, self.fch = self.font.render(' ', 0, pygame.Color('White')).get_size()
        # fcw/h -> font char width/height

    def is_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    def quit(self):
        pygame.quit()

    def print_panel(self, panel, offset=None):
        x_off, y_off = panel.x, panel.y
        for y, line in enumerate(panel.map):
            line = ''.join(line)
            word_surface = self.font.render(line, 0, pygame.Color('white'))
            _, text_h = word_surface.get_size()
            self.screen.blit(word_surface, ((0+x_off)*self.fcw, (y+y_off)*self.fch))
    
    def print_piece_over_panel(self, piece, panel):
        for y, row in enumerate(piece.map):
            piece_row = ''.join(row)
            word_surface = self.font.render(piece_row, 0, pygame.Color('white'))
            self.screen.blit(word_surface, ((piece.x + panel.x)*self.fcw, (y + piece.y + panel.y)*self.fch))
            self.refresh()

    def refresh(self):
        pygame.display.flip()
