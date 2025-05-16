import random
import numpy as np
from Agent import Agent
import os, time

#random.seed(42)
class Arena:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.full((height, width), ".", dtype=str)
        self.agents = []

    def add_agent(self, agent):
        x, y = agent.position
        if self.grid[y,x] == ".":
            self.grid[y,x] = agent.id
            self.agents.append(agent)
            return True
        return False #schaut, ob überhaupt ein Agent hinzugefügt worden ist

    def tick(self):
        self.grid[:, :] = "."

    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))
        print()

    def place_weapon_randomly(self, symbol):
        while True:
            x = random.randint(0, self.width -1)
            y = random.randint(0, self.height -1)

            if self.grid[y, x] == ".":
                self.grid[y,x] = symbol
                break

    def check_for_combat(self):

        positions = {}
        for agent in self.agents:
            pos = agent.position
            if pos in positions:
                other = positions[pos]
                agent.combat(other)
                if other.hp <= 0:
                    self.agents.remove(other)
                    print(f"{other.id} got killed")
                elif agent.hp <=0:
                    self.agents.remove(agent)
                    print(f"{agent.id} got killed")

                print (f"⚔️  Kampf zwischen Agent {agent.id} und Agent {other.id}!")
                print(f"HP von {other.id}: {other.hp}")
                print(f"HP von {agent.id}: {agent.hp}")


            else:
                positions[pos] = agent



    def move_all_agents(self, steps):
        for _ in range(steps):
            for agent in self.agents:
                x_old, y_old = agent.position
                self.grid[y_old][x_old] = "."

            for agent in self.agents:
                agent.move(self.width, self.height) #es wird eine neue Position gespeichert pro Agent
                if agent.position == #da wo halt die waffe ist, dann nimm sie auf und erhalte punkte dazu

            for agent in self.agents:
                x_new, y_new = agent.position
                self.grid[y_new][x_new] = agent.id
            self.check_for_combat()
            self.print_grid_live()


    def print_grid_live(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_grid()
        time.sleep(0.2)


arena = Arena(5,5)
agent_01 = Agent((2,2), 100, 10, 10, "D")
agent_02 = Agent((4,4), 100, 30, 5, "A")
arena.add_agent(agent_01)
#arena.add_agent(agent_02)
arena.place_weapon_randomly("S")
arena.move_all_agents(10)