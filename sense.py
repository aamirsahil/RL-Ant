class SenseOne:
    def __init__(self) -> None:
        self.home_likeness = 1 # home likeness of current cell
        self.target_likeness = 0 # target liekness of current cell
        self.has_food = False # been to target
        self.delta_time = 0 # time since last creation of pheromone
    def senseWorld(self, current_cell=None):
        self.delta_time = (self.delta_time + 1) % 4
        self.home_likeness = current_cell.home_pher_level
        self.target_likeness = current_cell.target_pher_level
        pass