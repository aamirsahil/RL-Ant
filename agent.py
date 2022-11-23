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
        # orientation starts from looking right(0) and turns anti-clockwise(defined as a list to make it mutable)
        self.orient = [0]
        # senses
        self.sense = Sense()
        # action
        action_data = {
            'pos' : self.pos,
            'orient' : self.orient,
        }
        self.action = Action(**action_data)
        # AI
        ai_data = {
            "epsilon" : 0.1,
            "alpha" : 0.2,
            "lambd" : 0.5,
            "epsilon_decay" : 0.01,
            "decay_till" : 0,
        }
        self.ai = AI(**ai_data)
        # 
        self.collected_food = 0
    def load(self, home_cells=None):
        # load init position
        starting_loc = rd.choice(home_cells)
        self.pos['x'] = starting_loc[0]
        self.pos['y'] = starting_loc[1]
        # load Q table
        q_data = {
            "states" : self.sense.getAllState(),
            "actions" : self.action.actions,
        }
        self.ai.load(**q_data)
    def do(self, world=None):
        # choose action
        curr_state = self.sense.getState()
        action = self.ai.decide(curr_state)
        # print(action)
        # select action based on the current sensory state
        self.action.do(action, world)
        return action
    def update(self, world, action):
        current_cell = world.getCurrentCell(self.pos)
        self.getReward(current_cell)
        self.sense.setState(current_cell, action)
    def learn(self, world=None):
        new_state = self.sense.getState()
        self.ai.learn(new_state)
    def getReward(self, current_cell):
        self.ai.reward = -1
        if current_cell.is_home == 1 and self.sense.has_food == 1:
            self.ai.reward = 10
            self.collected_food += 1