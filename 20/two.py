import numpy as np
from numba import njit

        
@njit
def enhance(image, algorithm):
    for k in range(50):
        print(k)
        new_image = np.ones_like(image) * algorithm[image[0, 0]]
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                square = image[i-1:i+2, j-1:j+2].flatten()
                n = 0
                for k in range(9):
                    n += square[k] * 2**(8 - k)
                new_image[i, j] = algorithm[n]
        image[:] = new_image
    return image
    
    
algorithm = []
size = 1000
image = np.zeros([size, size], dtype=int)
with open('input.txt') as f:
    line = f.readline().strip()
    algorithm = np.array(list(map(lambda x: '.#'.index(x), line)), dtype=int)
    i = 0
    for line in f.readlines():
        line = line.strip()
        if line:
            line = list(map(lambda x: '.#'.index(x), line))
            s = size // 2
            image[s+i, s-len(line)//2:s+len(line)//2] = line
            i += 1

print(np.sum(enhance(image, algorithm)))
