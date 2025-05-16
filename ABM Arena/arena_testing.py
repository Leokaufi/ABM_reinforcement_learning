import numpy as np

def mak(width, height):

    grid = np.full((height, width), ".", dtype=str)

    for row in grid:
        print("".join(row))
    print()

mak(2,4)