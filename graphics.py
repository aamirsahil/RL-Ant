import os
import time

class Graphics:
    def __init__(self, width=10, height=10, **kwargs) -> None:
        self.width = width
        self.height = height
        self.show_home_pher = True
        self.show_target_pher = False
        # grid to draw
        self.grid = [['B' for j in range(self.width)] for i in range(self.height)]
    # draw canvas
    def draw(self):
        os.system('cls')
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[i][j], end='')
            print('\n', end='')
    def setWorld(self, world):
        for i in range(self.height):
            for j in range(self.width):
                self.setCell(world.grid[i][j], i, j)
    def setAgent(self, agent):
        i = agent.pos['x']
        j = agent.pos['y']
        self.grid[i][j] = 'A  '
    def setCell(self, cell, i, j):
        cell_data = cell.getCell()
        if cell_data["is_home"]:
            self.grid[i][j] = 'H  '
        elif cell_data["is_target"]:
            self.grid[i][j] = 'F  '
        elif self.show_home_pher:
            home_pher_level = cell_data['home_pher_level']
            self.grid[i][j] = f'{home_pher_level:.1f}'
        elif self.show_target_pher:
            target_pher_level = cell_data['target_pher_level']
            self.grid[i][j] = f'{target_pher_level:.1f}'
        else:
            self.grid[i][j] = 'B'