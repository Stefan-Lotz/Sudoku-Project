import pygame
from sudoku_generator import SudokuGenerator
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        '''Constructor for the Board class.
	    screen is a window from PyGame.
	    difficulty is a variable to indicate if the user chose easy medium, or hard.'''
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        if difficulty == "easy":
            removed_cells = 30
        elif difficulty == "medium":
            removed_cells = 40
        else:
            removed_cells = 50

        sudoku_gen = SudokuGenerator(9, removed_cells)
        sudoku_gen.fill_values()
        self.solution = [row[:] for row in sudoku_gen.get_board()]
        sudoku_gen.remove_cells()
        self.board = sudoku_gen.get_board()
        self.original_board = [row[:] for row in self.board]

        self.cells = [[Cell(self.board[i][j], i, j,screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None

    def draw(self):
        '''Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board'''
        cell_size = 50

        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

        for i in range(10):
            if i % 3 == 0:
                line_width = 4
            else:
                line_width = 1

        pygame.draw.line(self.screen, (0, 0, 0),
                         (0, i * cell_size, 0),
                         (i * cell_size, self.height), line_width)

    def select(self, row, col):
        '''Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value.'''
        if self.selected_cell:
            old_row, old_col = self.selected_cell
            self.cells[old_row][old_col].selected = False

    def click(self, x, y):
        '''If a tuple of (x,y) coordinates is within the displayed board,
        this function returns a tuple of the (row, col) of the cell which was clicked.
        Otherwise, this function returns None.'''
        if 0 <= x < self.width and 0 <= y < self.height:
            cell_size = 50
            row = y // cell_size
            col = x // cell_size
            return (row, col)
        return None

    def celar(self):
        '''Clears the value cell.
        Note that the user can only remove the cell values and
        sketched values that are filled by themselves.'''
        if self.selected_cell:
            row, col = self.selected_cell
            if self.original_board[row][col] == 0:
                self.cells[row][col].set_cell_value()
                self.cells[row][col].set_sketched_value(0)

    def sketch(self, value):
        '''Sets the sketched value of the current selected cell equal to the user entered value.
        It will be displayed at the top left corner of the cell using the draw() function.'''
        if self.selected_cell:
            row, col = self.selected_cell
            if self.original_board[row][col] == 0:
                self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):
        '''Sets the value of the current selected cell equal to the user entered value.
        Called when the user presses the Enter key'''
        if self.selected_cell:
            row, col = self.selected_cell
            if self.original_board[row][col] == 0:
                self.cells[row][col].set_cell_value(value)
                self.cells[row][col].set_sketched_value(0)

    def reset_to_original(self):
        '''Resets all cells in the board to their original values
        (0 if cleared, otherwise the corresponding digit).'''
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.original_board[i])
                self.cells[i][j].set_sketched_value(0)

    def is_full(self):
        '''Returns a Boolean value indicating whether the board is full or not.'''
        for i in range(9):
            for j in range(9):
                return False
        return True

    def update_board(self):
        '''Updates the underlying 2D board with the values in all cells.'''
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value

    def find_empty(self):
        '''Finds an empty cell and returns its row and col as a tuple (x,y).'''
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return (i, j)
        return None

    def check_board(self):
        '''Check whether the Sudoku board is solved correctly.'''
        self.update_board()
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.solution[i][j]:
                    return False
            return True



