octopuses = []

with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            octopuses.append([int(x) for x in line])
            
octopuses.insert(0, len(octopuses[0]) * [0])
octopuses.append(len(octopuses[0]) * [0])
for row in octopuses:
    row.insert(0, 0)
    row.append(0)
          
step = 0
flash = False
while not flash:
    step += 1
    for i in range(1, len(octopuses) - 1):
        for j in range(1, len(octopuses[i]) - 1):
            octopuses[i][j] = octopuses[i][j] + 1
            
    new = True
    while new:
        new = False
        for i in range(1, len(octopuses) - 1):
            for j in range(1, len(octopuses[i]) - 1):
                if octopuses[i][j] > 9:
                    octopuses[i][j] = 0
                    new = True
                    
                    for ii in range(i - 1, i + 2):
                        for jj in range(j - 1, j + 2):
                            if octopuses[ii][jj] > 0:
                                octopuses[ii][jj] += 1
                                
    flash = True
    for i in range(1, len(octopuses) - 1):
        for j in range(1, len(octopuses[i]) - 1):
            if octopuses[i][j] != 0:
                flash = False
                    

for row in octopuses[1:-1]:
    print(row[1:-1])
print(step)
