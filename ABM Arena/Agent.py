import random

#random.seed(42)

class Agent:
    def __init__(self, position, hp, attack, defense, id):
        self.position = position
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


    def combat(self, other):
        other.hp -= self.attack - other.defense
        self.hp -= other.attack - self.defense
        return other.hp, self.hp
