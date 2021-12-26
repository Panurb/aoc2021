def intersect(X1, X2, Y1, Y2, Z1, Z2, x1, x2, y1, y2, z1, z2):
    if x1 <= X2 and x2 >= X1:
        if y1 <= Y2 and y2 >= Y1:
            if z1 <= Z2 and z2 >= Z1:
                return True
                
    return False
    
    
def volume(x1, x2, y1, y2, z1, z2):
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


count = 0
cuboids = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        state, coords = line.split()
        X, Y, Z = coords.split(',')
        X1, X2 = map(int, X.split('=')[-1].split('..'))
        Y1, Y2 = map(int, Y.split('=')[-1].split('..'))
        Z1, Z2 = map(int, Z.split('=')[-1].split('..'))
        
        for cub in reversed(cuboids):
            if intersect(X1, X2, Y1, Y2, Z1, Z2, *cub):
                x1, x2, y1, y2, z1, z2 = cub
            
                xs = [x for x in [x1, X1 - 1, X1, X2, X2 + 1, x2] if x1 <= x <= x2]
                ys = [y for y in [y1, Y1 - 1, Y1, Y2, Y2 + 1, y2] if y1 <= y <= y2]
                zs = [z for z in [z1, Z1 - 1, Z1, Z2, Z2 + 1, z2] if z1 <= z <= z2]
                if len(xs) == 3:
                    xs = [xs[0], xs[1], xs[1] + 1, xs[2]]
                if len(ys) == 3:
                    ys = [ys[0], ys[1], ys[1] + 1, ys[2]]
                if len(zs) == 3:
                    zs = [zs[0], zs[1], zs[1] + 1, zs[2]]
                
                for i in range(0, len(xs) - 1, 2):
                    for j in range(0, len(ys) - 1, 2):
                        for k in range(0, len(zs) - 1, 2):
                            c = (xs[i], xs[i + 1], ys[j], ys[j + 1], zs[k], zs[k + 1])
                            vol = volume(*c)
                            if vol > 0 and not intersect(X1, X2, Y1, Y2, Z1, Z2, *c):
                                cuboids.append(c)
                                count += vol

                count -= volume(*cub)
                cuboids.remove(cub)

        if state == 'on':
            cuboids.append((X1, X2, Y1, Y2, Z1, Z2))
            count += volume(X1, X2, Y1, Y2, Z1, Z2)

for a in cuboids:
    for b in cuboids:
        if a != b and intersect(*a, *b):
            print('error')
            
print(count)
