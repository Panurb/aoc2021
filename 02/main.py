with open('input.txt') as f:
    horiz = 0
    depth = 0
    lines = f.readlines()
    for line in lines:
        ins, num = line.split()
        if ins == 'forward':
            horiz += int(num)
        elif ins == 'down':
            depth += int(num)
        else:
            depth -= int(num)

    print(horiz * depth)
    
    
with open('input.txt') as f:
    horiz = 0
    depth = 0
    aim = 0
    lines = f.readlines()
    for line in lines:
        ins, num = line.split()
        num = int(num)
        if ins == 'forward':
            horiz += num
            depth += aim * num
        elif ins == 'down':
            aim += num
        else:
            aim -= num

    print(horiz * depth)
