import random
from Arena import Arena
from Agent import Agent

random.seed(42)

agent = Agent(position=(2,3), energy=100, id="A1")
print(agent.position)
agent.move(arena_width=5, arena_height=7)
print(agent.position)