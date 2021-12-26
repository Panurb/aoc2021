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
    if i < 5 * len(chitons) - 1:
        n.append([i + 1, j])
    if j < 5 * len(chitons[0]) - 1:
        n.append([i, j + 1])
    return n
    
n = len(chitons)
m = len(chitons[0])
end = [5 * n - 1, 5 * m - 1]
r = 25 * sum(map(sum, chitons))
min_risks = [5 * m * [r] for _ in range(5 * n)]
min_risks[0][0] = 0

new = True
while new:
    new = False
    for i in range(5 * n):
        for j in range(5 * m):
            risk = min_risks[i][j]
            for x, y in neighbors(i, j):
                r = chitons[x % n][y % m] + (x // n) + (y // m)
                r = (r - 1) % 9 + 1
                
                if min_risks[x][y] > risk + r:
                    min_risks[x][y] = risk + r
                    new = True

print(min_risks[-1][-1])
