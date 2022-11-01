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

    # initialize starting world state
    def load(self, file='./food.txt', **kwargs):
        file_name = file
        lines=open(file_name).readlines() # reads the food.txt file
        lines=[x.strip('\n') for x in lines] # remove '\n' from each line
        fh=len(lines)
        fw=max([len(x) for x in lines])
        if fh>self.height:
            fh=self.height
            starty=0
        else:
            starty=(self.height-fh)/2
        if fw>self.width:
            fw=self.width
            startx=0
        else:
            startx=(self.width-fw)/2
        for j in range(fh):
            line=lines[j]
            for i in range(min(fw,len(line))):
                self.grid[int(startx+i)][int(starty+j)].load(line=line[i])
    # get home cells
    def getHomeCells(self):
        home_cells = []
        for i in range(self.width):
            for j in range(self.height):
                if self.grid[i][j].is_home:
                    home_cells.append((i,j))
        return home_cells
    # get info about cell surrounding the agent
    def getSurroundingCell(self, agent_pos, type):
        if type == 'Home':
            pass
        if type == 'Target':
            pass
    # get info about current cell
    def getCurrentCell(self, agent_pos):
        x_index = agent_pos['x']
        y_index = (self.height-1) - agent_pos['y']
        current_cell = self.grid[x_index][y_index]
        return current_cell
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
    def disperse(self, surrounding_cell, dispersion_rate=0.4):
        self.disperseHomePher(surrounding_cell['home'], dispersion_rate)
        self.disperseTargetPher(surrounding_cell['target'], dispersion_rate)
    # disperse home pheromone
    def disperseHomePher(self, surrounding_cell, dispersion_rate):
        avg_home_pher_level_env = sum(surrounding_cell)/len(surrounding_cell)
        home_pher_difference = avg_home_pher_level_env - self.home_pher_level
        self.home_pher_level += home_pher_difference*dispersion_rate
    # disperse target pheromone
    def disperseTargetPher(self, surrounding_cell, dispersion_rate):
        avg_target_pher_level_env = sum(surrounding_cell)/len(surrounding_cell)
        target_pher_difference = avg_target_pher_level_env - self.target_pher_level
        self.target_pher_level += target_pher_difference*dispersion_rate

    # set cells as either home or target
    def load(self, **kwarg):
        if kwarg['line'] == 'H':
            self.setCell(is_home=True, is_target=False, home_pher_level=0, target_pher_level=0)
        elif kwarg['line'] == 'F':
            self.setCell(is_home=False, is_target=True, home_pher_level=0, target_pher_level=0)
        else:
            self.setCell(home_pher_level=0, target_pher_level=0)
    def setCell(self, is_home=False, is_target=False, **kwarg):
        self.is_home = is_home
        self.is_target = is_target
        self.home_pher_level = kwarg['home_pher_level']
        self.target_pher_level = kwarg['target_pher_level']