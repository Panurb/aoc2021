heightmap = []

with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            heightmap.append(list(map(int, line)))
    
risk = 0
for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        if i > 0:
            if heightmap[i - 1][j] <= height:
                continue
        if i < len(heightmap) - 1:
            if heightmap[i + 1][j] <= height:
                continue
        if j > 0:
            if heightmap[i][j - 1] <= height:
                continue
        if j < len(row) - 1:
            if heightmap[i][j + 1] <= height:
                continue
                
        risk += height + 1
        
print(risk)
