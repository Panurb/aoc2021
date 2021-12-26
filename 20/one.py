import numpy as np


algorithm = []
size = 200
image = np.zeros([size, size], dtype=int)
with open('input.txt') as f:
    line = f.readline().strip()
    algorithm = list(map(lambda x: '.#'.index(x), line))
    i = 0
    for line in f.readlines():
        line = line.strip()
        if line:
            line = list(map(lambda x: '.#'.index(x), line))
            image[5+i, 5:5+len(line)] = line
            i += 1
        
for _ in range(2):
    new_image = np.ones_like(image) * algorithm[image[0, 0]]
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            square = image[i-1:i+2, j-1:j+2].flatten()
            n = int(''.join([str(x) for x in square]), 2)
            new_image[i, j] = algorithm[n]
    image[:] = new_image
print(new_image)

print(np.sum(image))
# 7064
