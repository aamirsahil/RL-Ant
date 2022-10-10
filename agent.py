from numpy import random
class Agent:
    def __init__(self) -> None:
        # position
        self.pos = {
            "x" : 0,
            "y" : 0
        }
        # 
        # orientaion
        # orientation starts from looking right(0) and turns clockwise
        self.orient = 0
        # senses
        # class sense

        # action
        # class action

        # at every iteration, sense and take action
        pass
    def update(self):
        # sense
        # take action
        # update pos and orient
        pass

class Sense:
    def __init__(self) -> None:
        self.home_likeness = 0 # home likeness of surrounding cell
        self.target_likeness = 0 # target liekness of surrounding cell
        self.has_food = 0 # been to target
        self.delta_time = 0 # time since last creation of pheromone

class Action:
    def __init__(self) -> None:
        pass

    def move_forward(self):
        steps = [
            (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) 
        ]
        step = steps[int(self.orient / 45)]
        self.pos["x"] += step[0]
        self.pos["y"] += step[1]

    # acion pallete
    def move_random(self):
        self.delta_time = (self.delta_time + 1) % 6
        dir = random.choice([0, 1, 2])
        # step made corresponding to direction -> 0=0, 1=45, 2=90, .... 7=315

        # turn right
        if dir == 1:
            self.orient = (self.orient - 45)%360
        # turn left
        if dir == 2:
            self.orient = (self.orient - 45)%360
        # move forward
        self.move_forward()

    def move_to_home(self, surrounding_grid):
        self.delta_time = (self.delta_time + 1) % 6
        # turn to home
        self.orient = surrounding_grid.index(max(surrounding_grid))*45
        # move forward
        self.move_forward()
    def move_to_target(self, surrounding_grid):
        self.delta_time = (self.delta_time + 1) % 6
        # turn to target
        self.orient = surrounding_grid.index(max(surrounding_grid))*45
        # move forward
        self.move_forward()
    def create_home_pheromone(self, grid):
        self.delta_time = 0
        pass
    def create_target_pheromone(self, grid):
        self.delta_time = 0
        pass
