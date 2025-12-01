import pygame
from sudoku_generator import SudokuGenerator

class Cell:
    def __init__(self, value, row, col, screen):
        '''Constructor for the Cell class'''
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketeched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        '''Setter for this cell’s value'''
        self.value = value

    def set_sketched_value(self, value):
        '''Setter for this cell’s sketched value'''
        self.sketched_value = value

    def draw(self):
        '''Draws this cell, along with the value inside it.
	    If this cell has a nonzero value, that value is displayed.
	    Otherwise, no value is displayed in the cell.
	    The cell is outlined red if it is currently selected.'''
        cell_size = 50
        x = self.col * cell_size
        y = self.row * cell_size

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0 , 0), (x, y, cell_size, cell_size), 3)

        if self.value != 0:
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            self.screen.blit(text, text_rect)

        elif self.sketched_value != 0:
            font = pygame.font.Font(None, 25)
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))



