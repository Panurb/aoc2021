import math

heightmap = []

with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            heightmap.append(list(map(int, line)))
            
padding = (len(heightmap[0]) - 2) * [9]
heightmap.insert(0, padding)
heightmap.append(padding)
for row in heightmap:
    row.insert(0, 9)
    row.append(9)
    
basins = [len(heightmap[0]) * [0] for _ in range(len(heightmap))]
    
basin = 1
for i in range(1, len(heightmap) - 1):
    for j in range(1, len(heightmap[0]) - 1):
        height = heightmap[i][j]
        if heightmap[i - 1][j] <= height:
            continue
        if heightmap[i + 1][j] <= height:
            continue
        if heightmap[i][j - 1] <= height:
            continue
        if heightmap[i][j + 1] <= height:
            continue
            
        basins[i][j] = basin
        basin += 1

while True:
    new = False
    for i in range(1, len(heightmap) - 1):
        for j in range(1, len(heightmap[0]) - 1):
            if heightmap[i][j] == 9:
                continue
            if basins[i][j]:
                continue

            if basins[i - 1][j]:
                basins[i][j] = basins[i - 1][j]
                new = True
            elif basins[i + 1][j]:
                basins[i][j] = basins[i + 1][j]
                new = True
            elif basins[i][j - 1]:
                basins[i][j] = basins[i][j - 1]
                new = True
            elif basins[i][j + 1]:
                basins[i][j] = basins[i][j + 1]
                new = True

    if not new:
        break

sizes = []
for b in range(1, basin):
    size = sum([1 for row in basins for x in row if x == b])
    sizes.append(size)
sizes.sort()
    
print(sizes[-1] * sizes[-2] * sizes[-3])
# 432630
