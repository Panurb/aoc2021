import numpy as np
from numba import njit


@njit
def step(cucumbers):
    moving = 0
    h, w = cucumbers.shape

    new_cucumbers = np.zeros_like(cucumbers)
    for i, j in np.ndindex(cucumbers.shape):
        if cucumbers[i, j] == 1:
            if cucumbers[i, (j + 1) % w] == 0:
                new_cucumbers[i, (j + 1) % w] = 1
                moving += 1
            else:
                new_cucumbers[i, j] = 1
        elif cucumbers[i, j] == 2:
            new_cucumbers[i, j] = 2
    cucumbers[:] = new_cucumbers
                
    for i, j in np.ndindex(cucumbers.shape):
        if cucumbers[i, j] == 2:
            if cucumbers[(i + 1) % h, j] == 0:
                new_cucumbers[i, j] = 0
                new_cucumbers[(i + 1) % h, j] = 2
                moving += 1
            else:
                new_cucumbers[i, j] = 2
    cucumbers[:] = new_cucumbers
    
    return moving


with open('input.txt') as f:
    lines = f.readlines()
    shape = [len(lines), len(lines[0]) - 1]
    cucumbers = np.zeros(shape, dtype=int)
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            cucumbers[i, j] = '.>v'.index(c)
            
print(cucumbers)
print()
i = 0
moving = True
while moving:
    moving = step(cucumbers)
    i += 1
    print(i, moving)
print(cucumbers)
print(i)
    