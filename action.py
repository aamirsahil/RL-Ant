import random as rd

class Action:
    def __init__(self, pos=None, orient=None) -> None:
        # x and y steps for each orientation -> starts from 0 looking right and turns clockwise
        self.steps = [
            (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) 
        ]
        self.pos = pos
        self.orient = orient
        # action list
        self.actions = range(5)
    # move forward->move along orient# move forward->move along orient
    def moveForward(self):
        step = self.steps[self.orient[0] // 45]
        self.pos['x'] += step[0]
        self.pos['y'] += step[1]
    # turn left->oriemt increases(anti-clockwise turn)
    def turnLeft(self):
        self.orient[0] = (self.orient[0] + 45) % 360
    # turn right->orient decreases(clockwise turn)
    def turnRight(self):
        self.orient[0] = (self.orient[0] - 45) % 360
    def turnBack(self):
        self.orient[0] = (self.orient[0] + 180) % 360

# action set for study one
class StudyOne(Action):
    def __init__(self, pos, orient) -> None:
        super().__init__(pos, orient)
    # take action depending on action decision
    def do(self, action, world):
        if action == 0:
            self.moveRandom()
        elif action == 1:
            # home pheromone level of surrounding cells
            surrounding_cells = world.getSurroundingCell(pos=self.pos, type='home')
            self.moveToHome(surrounding_cells=surrounding_cells)
        elif action == 2:
            # target pheromone level of surrounding cells
            surrounding_cells = world.getSurroundingCell(pos=self.pos, type='target')
            self.moveToTarget(surrounding_cells=surrounding_cells)
        elif action == 3:
            # get instance of current cell
            current_cell = world.getCurrentCell(pos=self.pos)
            self.createHomePher(current_cell=current_cell)
        elif action == 4:
            # get instance of current cell
            current_cell = world.getCurrentCell(pos=self.pos)
            self.createTargetPher(current_cell=current_cell)
    # acion pallete
    # action=0
    def moveRandom(self):
        dir = rd.randint(0, 2)
        # step made corresponding to direction -> 0=0, 1=45, 2=90, .... 7=315
        # if dir=1 turn right
        if dir == 1:
            self.turnRight()
        # if dir=2 turn left
        elif dir == 2:
            self.turnLeft()
        # move forward
        self.moveForward()
    # action=1
    def moveToHome(self, surrounding_cells):
        # turn to home
        self.orient[0] = surrounding_cells.index(max(surrounding_cells))*45
        # move forward
        self.moveForward()
    # action=2
    def moveToTarget(self, surrounding_cells):
        # turn to target
        self.orient[0] = surrounding_cells.index(max(surrounding_cells))*45
        # move forward
        self.moveForward()
    # action=3
    def createHomePher(self, current_cell):
        current_cell.addHomePher(pher_unit=1)
    # action=4
    def createTargetPher(self, current_cell):
        current_cell.addTargetPher(pher_unit=1)