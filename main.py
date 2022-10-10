import matplotlib.pyplot as plt
from agent import Agent

def main():
    agent = Agent()
    x, y = [], []
    for i in range(1000):
        x.append(agent.pos["x"])
        y.append(agent.pos["y"])
        agent.move_random()
    plt.plot(x, y)
    plt.show()
if __name__ == "__main__":
    main()