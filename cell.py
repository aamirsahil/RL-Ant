# Cell class to repersent each cell in the lattice
class Cell:
    def __init__(self) -> None:
        self.is_home = False
        self.is_target = False
        self.home_pher_level = 0
        self.target_pher_level = 0

    # update home pheromone level in the environment
    def addHomePher(self, pher_unit=0.2):
        self.home_pher_level += pher_unit

    # update target pheromone level in the environment
    def addTargetPher(self, pher_unit=0.2):
        self.target_pher_level += pher_unit
        
    # evoporates the pheromone in the environment as time goes by
    def evoporate(self, evoporation_rate=0.99):
        self.home_pher_level *= evoporation_rate
        self.target_pher_level *= evoporation_rate
        
    # disperse the pheromone to surrounding cell depending on differnce
    # in concentration
    def disperse(self, surrounding_cell, type="home", dispersion_rate=0.04):
        avg_pher_level_env = sum(surrounding_cell)/len(surrounding_cell)
        if type == "home":
            pher_difference = avg_pher_level_env - self.home_pher_level
            self.home_pher_level += pher_difference*dispersion_rate
        elif type == "target":
            pher_difference = avg_pher_level_env - self.target_pher_level
            self.target_pher_level += pher_difference*dispersion_rate

    # set cells as either home or target
    def load(self, **kwarg):
        if kwarg['line'] == 'H':
            self.setCell(is_home=True, is_target=False, home_pher_level=0, target_pher_level=0)
        elif kwarg['line'] == 'F':
            self.setCell(is_home=False, is_target=True, home_pher_level=0, target_pher_level=0)
        else:
            self.setCell(home_pher_level=0, target_pher_level=0)
    def setCell(self, is_home=False, is_target=False, home_pher_level=0.0, target_pher_level=0.0):
        self.is_home = is_home
        self.is_target = is_target
        self.home_pher_level = home_pher_level
        self.target_pher_level = target_pher_level
    def getCell(self):
        cell_data = {
            "is_home" : self.is_home,
            "is_target" : self.is_target,
            "home_pher_level" : self.home_pher_level,
            "target_pher_level" : self.target_pher_level,
        }
        return cell_data