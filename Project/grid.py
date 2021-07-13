from square import *


class Grid():
    def __init__(self):
        self.grid = []
        self.number_of_columns = 9
        self.number_of_rows = 9
        self.number_of_squares = 81

    def get_number_of_columns(self):
        return self.number_of_columns

    def get_number_of_rows(self):
        return self.number_of_rows

    def get_number_of_squares(self):
        return self.number_of_squares
    
    def create_grid(self):
        for row in range(10):
            self.grid.append([])
            for column in range(10):
                self.grid[row].append(0)
    
    def draw_grid(self):
        for row in range(10):
            for column in range(10):
                pygame.draw.rect(screen,
                                color,
                                )
        pygame.display.update()