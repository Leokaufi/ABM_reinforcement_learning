import random

#random.seed(42)

class Agent:
    def __init__(self, position, energy, hp, attack, defense, id):
        self.position = position
        self.energy = energy
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.id = id

    def move(self, arena_width, arena_height):

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = random.choice(directions)

        new_x = self.position[0] + dx
        new_y = self.position[1] + dy

        if 0 <= new_x < arena_width and 0 <= new_y < arena_height:
            self.position = (new_x, new_y)

    def attack_other_agent(self, other):
        other.hp -= self.attack
        return other.hp
