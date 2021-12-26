from functools import cache


def check_win(level):
    for c in range(1, 5):
        room = 3 + 2 * (c - 1)
        if level[2][room] != c:
            return False
        if level[3][room] != c:
            return False
            
    return True
    
    
def level_to_str(level):
    level_str = ''
    for row in level:
        level_str += ''.join(map(str, row))
    return level_str
    
    
def str_to_level(level_str):
    level = []
    for i in range(5):
        row = list(map(int, level_str[13*i:13*i+13]))
        level.append(row)
    return level


@cache
def move(level_str, cost):
    level = str_to_level(level_str)

    if check_win(level):
        return cost

    min_cost = 99999999999
    for i in range(1, 4):
        row = level[i]
        for j in range(1, 12):
            c = level[i][j]
            
            if 1 <= c <= 4:
                room = 3 + 2 * (c - 1)
                
                if j == room and level[3][room] == c:
                    continue
                
                moves = []
                if i == 2 or (i == 3 and level[2][j] == 0):
                    if level[1][j] == 0:
                        k = j + 1
                        while level[1][k] == 0:
                            moves.append((1, k))
                            k += 1
                            
                        k = j - 1
                        while level[1][k] == 0:
                            moves.append((1, k))
                            k -= 1
                elif i == 1:
                    if level[2][room] != 0:
                        continue
                        
                    if sum(row[min(j, room):max(j, room)+1]) != c:
                        continue
                        
                    if level[3][room] == 0:
                        moves.append((3, room))
                    elif level[3][room] == c:
                        moves.append((2, room))
                        
                for x, y in moves:
                    level[i][j] = 0
                    level[x][y] = c
                    
                    level_str = level_to_str(level)
                    co = move(level_str, cost + 10**(c-1) * (abs(x - i) + abs(y - j)))
                    min_cost = min(min_cost, co)
                    
                    level[i][j] = c
                    level[x][y] = 0
                    
    return min_cost
                

level = []
with open('example.txt') as f:
    for line in f.readlines():
        row = []
        for c in line[:-1]:
            if c in '. ':
                row.append(0)
            else:
                row.append(' ABCD#'.index(c))
        level.append(row)
        
level = str_to_level(level_to_str(level))
for row in level:
    print(row)

print(move(level_to_str(level), 0))
