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
        self.weapons = {}

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

    def place_object_randomly(self):
        object_list = ["S", "D", "B"]

        for weapon in object_list:
            while True:

                x = random.randint(0, self.width -1)
                y = random.randint(0, self.height -1)

                if self.grid[y,x] == "." and (x,y) not in self.weapons:
                    self.grid[y,x] = weapon
                    self.weapons[(x,y)] = weapon
                    break

        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.grid[y,x] == ".":
                self.grid[y,x] = "#"
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

            #refreshing the grid
            for agent in self.agents:
                x_old, y_old = agent.position
                self.grid[y_old][x_old] = "."

            #moving the agents
            for agent in self.agents:
                x_old, y_old = agent.position
                agent.move(self.width, self.height) #es wird eine neue Position gespeichert pro Agent
                x_new, y_new = agent.position

                if self.grid[y_new, x_new] == "#":
                    agent.position = (x_old, y_old)
                    continue #macht das nicht einen Fehler ChatGPT?

                if agent.position in self.weapons: #if agent meets the weapon
                    if self.weapons[agent.position] == "S":
                        agent.attack += 10
                        print(f"{agent.id} hat 10 Attacke dazu")
                    elif self.weapons[agent.position] == "B":
                        agent.bow = True
                        print(f"{agent.id} hat bogen")
                    elif self.weapons[agent.position] == "D":
                        agent.defense += 10
                        print(f"{agent.id} hat 10 Verteidigung dazu")

                    del self.weapons[agent.position]
                    self.grid[agent.position[1], agent.position[0]] = "."

            for agent in self.agents:
                x_new, y_new = agent.position
                self.grid[y_new][x_new] = agent.id

                self.check_for_combat()
                #self.print_grid_live()


    def print_grid_live(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_grid()
        time.sleep(0.2)


arena = Arena(8,8)
agent_01 = Agent((2,2), 100, 10, 10, "T") #T for Tank
agent_02 = Agent((4,4), 100, 30, 5, "A") #A for Attacker

arena.add_agent(agent_01)
arena.add_agent(agent_02)

arena.place_object_randomly()

arena.move_all_agents(1000)
print(f"Überlebender: {arena.agents[0].id}")
