from action import StudyOne as Action
from sense import SenseOne as Sense
from AI import QLearn as AI

import random as rd

class Agent:
    def __init__(self) -> None:
        # position
        self.pos = {
            "x" : 0,
            "y" : 0
        }
        # orientation starts from looking right(0) and turns anti-clockwise
        self.orient = 0
        # senses
        self.sense = Sense()
        # action
        self.action = Action()
        # AI
        self.ai = AI()
    def load(self):
        pass
    def update(self, world=None):
        # set the sensory state of the agent
        self.sense.senseWorld(self)
        # choose action
        action = self.ai.decide()
        # select action based on the current sensory state
        self.action.takeAction(action, world)
    def takeAction(self, action=0, world=None):
        action = rd.randint(0, 4)
        if action == 0:
            self.action.moveRandom(self)
        elif action == 1:
            # home pheromone level of surrounding cells
            surrounding_cells = world.calcSurroundingCells(agent_pos=self.pos, type='Home')
            self.action.moveToHome(self, surrounding_cells=surrounding_cells)
        elif action == 2:
            # target pheromone level of surrounding cells
            surrounding_cells = world.calcSurroundingCells(agent_pos=self.pos, type='Target')
            self.action.moveToTarget(self, surrounding_cells=surrounding_cells)
        elif action == 3:
            # get instance of current cell
            current_cell = world.getCurrentCell(agent_pos=self.pos)
            self.action.createHomePher(self, current_cell=current_cell)
        elif action == 4:
            # get instance of current cell
            current_cell = world.getCurrentCell(agent_pos=self.pos)
            self.action.createTargetPher(self, current_cell=current_cell)