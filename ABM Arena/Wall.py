

class Wall:
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def get_wall(self):
        x,y = self.position
        if self.orientation == "horizontal":
            return[(x,y), (x+1,y), (x+2,y)]
        if self.orientation == "vertical":
            return [(x, y), (x, y + 1), (x, y + 2)]
        if self.orientation == "diag_down":
            return [(x, y), (x + 1, y + 1), (x + 2, y + 2)]
        if self.orientation == "diag_up":
            return [(x, y), (x + 1, y - 1), (x + 2, y - 2)]
