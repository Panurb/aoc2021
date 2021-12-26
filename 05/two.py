import numpy as np

    
with open('input.txt') as f:
    lines = f.readlines()

    x_max = 0
    y_max = 0
    for line in lines:
        start, end = line.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        
        x_max = max(x_max, max(x1, x2))
        y_max = max(y_max, max(y1, y2))
            
    points = np.zeros([x_max + 1, y_max + 1])
    
    for line in lines:
        start, end = line.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        
        if x1 == x2:
            points[x1, min(y1, y2):max(y1, y2)+1] += 1
        elif y1 == y2:
            points[min(x1, x2):max(x1, x2)+1, y1] += 1
        else:
            if x2 > x1:
                xs = range(x1, x2 + 1)
            else:
                xs = range(x1, x2 - 1, -1)
            if y2 > y1:
                ys = range(y1, y2 + 1)
            else:
                ys = range(y1, y2 - 1, -1)
                
            for i in range(len(xs)):
                points[xs[i], ys[i]] += 1
            
    print(points.T)
    print(sum(1 for x in points.flatten() if x >= 2))
