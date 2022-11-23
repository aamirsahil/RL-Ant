from cell import Cell

import json
import sys

# World class that keep track of world state
class World():
    def __init__(self, width=10, height=10, boundary='periodic', **kwargs) -> None:
        # height and width of the world
        self.width = width
        self.height = height
        # boundary condition
        self.boundary = boundary
        # create the lattice cells
        self.grid = [[Cell() for j in range(self.width)] for i in range(self.height)]
        # to find surroundig cells
        self.steps = [
            (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) 
        ]
        # evoporation and dispersion data
        self.evoporate = kwargs["evoporate"]
        self.evoporation_rate = kwargs["evoporation_rate"]
        self.disperse = kwargs["disperse"]
        self.disperse_rate = kwargs["dispersion_rate"]

    # initialize starting world state
    def load(self, file='./food.txt'):
        file_name = file
        with open(file_name) as f:
            data = f.read()
        map_data = json.loads(data)
        map_array = self.convertMapData(**map_data)
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j].setCell(**map_array[i][j])
    # update world cells
    def update(self):
        for i in range(self.height):
            for j in range(self.width):
                # evoporate the pheromone
                if self.evoporate:
                    self.grid[i][j].evoporate(evoporation_rate=self.evoporation_rate)
                # disperse pheromone
                pos = {
                    'x' : j,
                    'y' : i,
                }
                # dispersing home pheremone
                if self.disperse:
                    surrounding_cell = self.getSurroundingCell(pos=pos, type="home")
                    self.grid[i][j].disperse(surrounding_cell, type="home", dispersion_rate=self.disperse_rate)

    # convert map_data to array
    def convertMapData(self, home=None, target=None):
        map_array = []
        for i in range(self.height):
            map_array.append([])
            for j in range(self.width):
                inside_home = (home['x0'] <= j) and (j < (home['x0']+home['width'])) and \
                    (home['y0'] <= i) and (i < (home['y0']+home['height']))
                inside_target = (target['x0'] <= j) and (j < (target['x0']+target['width'])) and \
                    (target['y0'] <= i) and (i < (target['y0']+target['height']))
                map_value = {
                        "is_home" : False,
                        "is_target" : False,
                        "home_pher_level" : 0.0,
                        "target_pher_level" : 0.0,
                    }
                if inside_home:
                    map_value["is_home"] = True
                if inside_target:
                    map_value["is_target"] = True
                map_array[-1].append(map_value)
        return map_array
    # check if the food target file is allowed
    def checkFile(self, init_data=None):
        x1 = init_data['home']['x0']
        w1 = init_data['home']['width']
        x2 = init_data['target']['x0']
        w2 = init_data['target']['width']
        y1 = init_data['home']['x0']
        h1 = init_data['home']['width']
        y2 = init_data['target']['x0']
        h2 = init_data['target']['width']
        x_intersect = not (x1<x2 and (x1 + w1)<x2 and (x2 + w2 - self.width)<x1)
        y_intersect = not (y1<y2 and (y1 + h1)<y2 and (h2 + h2 - self.width)<y1)
        if x_intersect or y_intersect:
            terminate = True
        else:
            terminate = False
        return terminate
    # get home cells
    def getHomeCells(self):
        home_cells = []
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j].is_home:
                    home_cells.append((i,j))
        return home_cells
    # get target cells
    def getTargetCells(self):
        target_cells = []
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j].is_target:
                    target_cells.append((i,j))
        return target_cells
    # get info about cells surrounding selected cell
    def getSurroundingCell(self, pos=None, type=None):
        surrounding_cells = []
        for step in self.steps:
            x, y = self.getIndex(pos=pos, step=step)
            if x==None and y==None:
                continue
            if type == "home":
                surrounding_cells.append(self.grid[x][y].home_pher_level)
            elif type == "target":
                surrounding_cells.append(self.grid[x][y].target_pher_level)
        return surrounding_cells
    def getIndex(self, pos=None, step=None):
        x = pos['x'] + step[0]
        y = pos['y'] + step[1]
        if self.boundary == "periodic":
            x %= self.width
            y %= self.height
        elif self.boundary == "reflective":
            inside_x = (x < self.width and x >= 0)
            inside_y = (y < self.height and y >= 0)
            if not inside_x or not inside_y:
                return None, None # so that these cells will never be max
        return x, y
    # apply boundary condition
    def checkBoundary(self, agent):
        inside_x = agent.pos['x'] < self.width and agent.pos['x'] >= 0
        inside_y = agent.pos['y'] < self.height and agent.pos['y'] >= 0
        if not inside_x or not inside_y:
            if self.boundary == "periodic":
                agent.pos['x'] %= self.width
                agent.pos['y'] %= self.height
            if self.boundary == "reflective":
                agent.action.turnBack()
                agent.action.moveForward()
    # get info about current cell
    def getCurrentCell(self, pos):
        x = pos['x']
        y = pos['y']
        current_cell = self.grid[x][y]
        return current_cell