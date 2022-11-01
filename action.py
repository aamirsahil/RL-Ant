import random as rd

class Action:
    def __init__(self) -> None:
        # x and y steps for each orientation -> starts from 0 looking right and turns clockwise
        self.steps = [
            (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) 
        ]
    # move forward->move along orient# move forward->move along orient
    def moveForward(self, agent, width, height):
        step = self.steps[agent.orient // 45]
        agent.pos['x'] = (agent.pos['x'] + step[0]) % width
        agent.pos['y'] = (agent.pos['y'] + step[1]) % height
    # turn left->oriemt increases(anti-clockwise turn)
    def turnLeft(self, agent):
        agent.orient = (agent.orient + 45) % 360
    # turn right->orient decreases(clockwise turn)
    def turnRight(self, agent):
        agent.orient = (agent.orient - 45) % 360
    def turnBack(self, agent):
        agent.orient = (agent.orient + 180) % 360

# action set for study one
class StudyOne(Action):
    def __init__(self) -> None:
        super().__init__()
    # acion pallete
    # action=0
    def moveRandom(self, agent, **kwarg):
        dir = rd.randint(0, 2)
        # step made corresponding to direction -> 0=0, 1=45, 2=90, .... 7=315
        # if dir=1 turn right
        if dir == 1:
            self.turnRight(agent)
        # if dir=2 turn left
        elif dir == 2:
            self.turnLeft(agent)
        # move forward
        self.moveForward(agent)
        if kwarg['boundary'] == 'reflective':
            self.turnBack(agent)
            self.moveForward(agent)
    # action=1
    def moveToHome(self, agent, surrounding_cells, **kwargs):
        # turn to home
        agent.orient = surrounding_cells.index(max(surrounding_cells))*45
        # move forward
        self.moveForward(agent)
    # action=2
    def moveToTarget(self, agent, surrounding_cells, **kwargs):
        # turn to target
        agent.orient = surrounding_cells.index(max(surrounding_cells))*45
        # move forward
        self.moveForward(agent)
    # action=3
    def createHomePher(self, current_cell):
        current_cell.addHomePher(pher_unit=1)
    # action=4
    def createTargetPher(self, current_cell):
        current_cell.addTargetPher(pher_unit=1)
    # action=5
    # action=6