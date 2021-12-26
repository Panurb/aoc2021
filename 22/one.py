import numpy as np


STATES = {'off': 0, 'on': 1}


cubes = np.zeros([101, 101, 101], dtype=int)
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        state, coords = line.split()
        x, y, z = coords.split(',')
        x1, x2 = map(int, x.split('=')[-1].split('..'))
        y1, y2 = map(int, y.split('=')[-1].split('..'))
        z1, z2 = map(int, z.split('=')[-1].split('..'))
        for coord in [x1, x2, y1, y2, z1, z2]:
            if abs(coord) > 50:
                break
        else:
            cubes[x1+50:x2+51, y1+50:y2+51, z1+50:z2+51] = STATES[state]
        
print(np.sum(cubes))
