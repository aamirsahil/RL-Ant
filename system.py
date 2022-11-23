from world import World
from agent import Agent
from graphics import Graphics
# from UI import UI

import random as rd

class System:
    def __init__(self, total_time=10, agent_no=10, world_data=None) -> None:
        self.time = 0
        self.total_time = total_time
        # world of grid cells
        self.world = World(**world_data)
        # 'agent_no' of agents
        self.agent_no = agent_no
        self.agents = [Agent() for i in range(self.agent_no)]
        # UI element
        # self.ui = UI()
        # create drawing element
        self.graphics = Graphics(**world_data)
    # load system
    def load(self):
        # load ui
        # self.ui.load()
        # load world
        self.world.load()
        # load agents
        home_cells = self.world.getHomeCells()
        for agent in self.agents:
            agent.load(home_cells=home_cells)
        # load graphics
        # self.graphics.load()
    # run simulation
    def run(self):
        # main loop
        while self.time < self.total_time:
            # draw 
            self.graphics.setWorld(self.world)
            for agent in self.agents:
                self.graphics.setAgent(agent)
            self.graphics.draw()
            # updates all agents
            for agent in self.agents:
                action = agent.do(self.world)
                self.world.checkBoundary(agent)
                agent.update(self.world, action)
                agent.learn(self.world)
            # agents dont move sequentially
            rd.shuffle(self.agents)
            # evoporation and dispersion
            self.world.update()
            # time progresses
            self.time += 1
        for agent in self.agents:
            print(agent.collected_food)