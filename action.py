import random as rd

class Action:
    def __init__(self, pos, orient) -> None:
        # x and y steps for each orientation -> starts from 0 looking right and turns clockwise
        self.steps = [
            (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) 
        ]
        self.pos = pos
        self.orient = orient
    # move forward->move along orient# move forward->move along orient
    def moveForward(self, width, height):
        step = self.steps[self.orient[0] // 45]
        self.pos['x'] = (self.pos['x'] + step[0]) % width
        self.pos['y'] = (self.pos['y'] + step[1]) % height
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
    def __init__(self) -> None:
        super().__init__()
    # acion pallete
    # action=0
    def moveRandom(self, **kwarg):
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
        if kwarg['boundary'] == 'reflective':
            self.turnBack()
            self.moveForward()
    # action=1
    def moveToHome(self, surrounding_cells, **kwargs):
        # turn to home
        self.orient[0] = surrounding_cells.index(max(surrounding_cells))*45
        # move forward
        self.moveForward()
    # action=2
    def moveToTarget(self, surrounding_cells, **kwargs):
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
    # action=5
    # action=6