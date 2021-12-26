from functools import cache


def check_win(level):
    for c in range(1, 5):
        room = 3 + 2 * (c - 1)
        for i in range(2, 6):
            if level[i][room] != c:
                return False
            
    return True

    
path = []


@cache
def move(level, cost):
    global path

    if check_win(level):
        return cost
        
    level = list(map(list, level))

    min_cost = 99999999999
    for i in range(1, 6):
        row = level[i]
        for j in range(1, 12):
            c = level[i][j]
            
            if 1 <= c <= 4:
                room = 3 + 2 * (c - 1)
                
                if j == room:
                    for k in range(i, 6):
                        if level[k][room] != c:
                            break
                    else: 
                        continue
                
                moves = []
                if i == 1:
                    if level[2][room] != 0:
                        continue
                        
                    if sum(row[min(j, room):max(j, room)+1]) != c:
                        continue
                        
                    l = 0
                    for k in range(2, 6):
                        if level[k][room] == 0:
                            l = k
                        elif level[k][room] != c:
                            break
                    else:
                        moves.append((l, room))
                else:
                    for k in range(1, i):
                        if level[k][j] != 0:
                            break
                    else:
                        k = j + 1
                        while level[1][k] == 0:
                            if k not in [3, 5, 7, 9]:
                                moves.append((1, k))
                            k += 1
                            
                        k = j - 1
                        while level[1][k] == 0:
                            if k not in [3, 5, 7, 9]:
                                moves.append((1, k))
                            k -= 1
                        
                for x, y in moves:
                    level[i][j] = 0
                    level[x][y] = c
                    
                    path.append((' ABCD'[c], x, y))
                    level_tuple = tuple(map(tuple, level))
                    co = move(level_tuple, cost + 10**(c-1) * (abs(x - i) + abs(y - j)))
                    min_cost = min(min_cost, co)
                    path.pop()
                    
                    level[i][j] = c
                    level[x][y] = 0
                    
    return min_cost
                

level = []
with open('input.txt') as f:
    lines = f.readlines()
    lines.insert(3, '  #D#B#A#C#  \n')
    lines.insert(3, '  #D#C#B#A#  \n')
    for line in lines:
        row = []
        for c in line[:-1]:
            if c in '. ':
                row.append(0)
            else:
                row.append(' ABCD#'.index(c))
        row += (13 - len(row)) * [0]
        level.append(row)
        
for row in level:
    print(row)

level = tuple(map(tuple, level))
print(move(level, 0))
