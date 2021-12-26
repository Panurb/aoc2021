chitons = []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line:
            chitons.append(list(map(int, line)))
    
def neighbors(i, j):
    n = []
    if i > 0:
        n.append([i - 1, j])
    if j > 0:
        n.append([i, j - 1])
    if i < len(chitons) - 1:
        n.append([i + 1, j])
    if j < len(chitons[0]) - 1:
        n.append([i, j + 1])
    return n
    
end = [len(chitons) - 1, len(chitons[0]) - 1]
r = sum(map(sum, chitons))
min_risks = [len(chitons[0]) * [r] for _ in chitons]
min_risks[0][0] = 0

new = True
while new:
    new = False
    for i, row in enumerate(chitons):
        for j, _ in enumerate(row):
            risk = min_risks[i][j]
            for x, y in neighbors(i, j):
                r = chitons[x][y]
                
                if min_risks[x][y] > risk + r:
                    min_risks[x][y] = risk + r
                    new = True
    

print(min_risks[-1][-1])
# 595
