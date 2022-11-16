import numpy as np
from random import randint, choice

# Saída / Ouro / Poço / Wumpus / Brisa / Fedor

class mundo:
    def __init__(self,n):
        self.generateWorld(n)

    def generateWorld(self, n):
        world = np.zeros((n,n),dtype=int)
        if(randint(0,1)):
            world[randint(0,n-1)][choice([0,n-1])] = 32
        else:
            world[choice([0,n-1])][randint(0,n-1)] = 32
        for i in range(int((n * n) * 0.2)):
            x = randint(0,n-1)
            y = randint(0,n-1)
            while(world[x][y] > 0):
                x = randint(0,n-1)
                y = randint(0,n-1)
            world[x][y] = 8
            breeze = np.concatenate((
                np.stack((np.array([x-1, x+1]), np.repeat(y,2)), axis=1),
                np.stack((np.repeat(x,2), np.array([y-1, y+1])), axis=1)
            ))
            breeze = [list(filter(lambda x : x >= 0 and x < n, b)) for b in breeze]
            for b in list(filter(lambda x : len(x) == 2, breeze)):
                if(b[0] >= 0 and b[0] < n and b[1] >= 0 and b[1] < n):
#                    print(f"world[{b[0]}][{b[1]}] = world")
                    if(world[b[0]][b[1]] <= 4):
                        world[b[0]][b[1]] = 2
        print(world)

if __name__ == "__main__":
    w = mundo(4)
