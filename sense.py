import numpy as np

# sense class for study 1
class SenseOne:
    def __init__(self) -> None:
        # home likeness of current cell -> [0,1] with 4 state | home cells are always 1
        self.home_likeness = 1
        # target liekness of current cell -> [0,1] with 4 state | target cells are always 1
        self.target_likeness = 0
        self.has_food = 0 # been to target
        self.delta_time = 0 # time since last creation of pheromone -> [0,5]
        # sensory unit
        self.sensory_unit = 1/3
    # get current state of the agent
    def getState(self):
        state = (self.home_likeness, self.target_likeness, self.has_food, self.delta_time)
        return state
    # set current state of the agent
    def setState(self, current_cell=None, action=1):
        self.home_likeness = self.senseHomePher(current_cell.home_pher_level, current_cell.is_home)
        self.target_likeness = self.senseTargetPher(current_cell.target_pher_level, current_cell.is_target)
        if self.has_food == 0 and current_cell.is_target:
            self.has_food = 1
        elif self.has_food == 1 and current_cell.is_home:
            self.has_food = 0
        self.delta_time = (self.delta_time + 1) % 6
        if action == 1 or action == 2:
            self.delta_time = 0
    # get state space of agent
    def getAllState(self):
        states = []
        home_likeness = np.around(np.linspace(0, 1, 4),2)
        target_likeness = np.around(np.linspace(0, 1, 4),2)
        has_food = range(2)
        delta_time = range(6)
        for state1 in home_likeness:
            for state2 in target_likeness:
                for state3 in has_food:
                    for state4 in delta_time:
                        states.append((state1, state2, state3, state4))
        return states
    def senseWorld(self, current_cell=None):
        self.home_likeness = self.senseHomePher(current_cell.home_pher_level, current_cell.is_home)
        self.target_likeness = self.senseTargetPher(current_cell.target_pher_level, current_cell.is_target)
    def senseHomePher(self, pher_level, is_home):
        home_likeness = round(int(pher_level/self.sensory_unit)*self.sensory_unit, 2)
        if home_likeness > 1 or is_home:
            home_likeness = 1
        return home_likeness
    def senseTargetPher(self, pher_level, is_target):
        target_likeness = round(int(pher_level/self.sensory_unit)*self.sensory_unit, 2)
        if target_likeness > 1 or is_target:
            target_likeness = 1
        return target_likeness