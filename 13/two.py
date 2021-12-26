sheet = []
folds = []

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    dots = []
    x_max = 0
    y_max = 0
    for line in lines:
        if not line:
            continue
        if 'fold along' in line:
            dir, val = line.split()[-1].split('=')
            folds.append([dir, int(val)])
        else:
            x, y = map(int, line.split(','))
            dots.append([x, y])
            x_max = max(x_max, x)
            y_max = max(y_max, y)
            
    sheet = [(x_max + 1) * [0] for _ in range(y_max + 1)]
    
    for x, y in dots:
        sheet[y][x] = 1
        
for dir, val in folds:
    print(dir, val)
    if dir == 'x':
        for j, row in enumerate(sheet):
            left = row[0:val]
            right = row[-1:val:-1]
            sheet[j] = left
            for i in range(len(left) - len(right), len(left)):
                sheet[j][i] = max(left[i], right[i])
    else:
        up = sheet[0:val]
        down = sheet[-1:val:-1]
        sheet = up
        diff = len(up) - len(down)
        for j in range(diff, len(up)):
            for i in range(len(sheet[0])):
                sheet[j][i] = max(up[j][i], down[j - diff][i])
        
for row in sheet:
    print(''.join(['.#'[x] for x in row]))
