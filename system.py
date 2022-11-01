from world import World
from agent import Agent

import random as rd

class System:
    def __init__(self, total_time=1000, agent_no=10, **kwargs) -> None:
        self.time = 0
        self.total_time = total_time
        self.world = World(width=kwargs['width'], height=kwargs['height'], boundary=kwargs['boundary'])

        # create 'agent_no' number of agents
        self.agent_no = agent_no
        self.agents = [Agent() for i in range(self.agent_no)]
    def run(self):
        self.load()
        # main loop
        while self.time < self.total_time:
            # updates all agents
            for agent in self.agents:
                # set the sensory state of the agent
                agent.update(self.world)
            # agents dont move sequentially
            rd.shuffle(self.agents)
            # evoporation and dispersion
            self.world.update()
            # time progresses
            self.time += 1
            
    # initial setup
    def load(self, **kwargs):
        self.world.load(file=kwargs['file'])
        home_cells = self.world.getHomeCells()
        for agent in self.agents:
            agent.load(home_cells=home_cells)
