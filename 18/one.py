from math import floor, ceil


def add(a, b):
    return f'[{a},{b}]'
    

def split(a, i):
    x = int(a[i:i+2])
    return a[:i] + f'[{floor(x / 2)},{ceil(x / 2)}]' + a[i+2:]
    
    
def explode(a, i, left):
    for j in range(i, len(a)):
        if a[j] == ']':
            end = j
            break
                        
    x, y = map(int, a[i+1:end].split(','))

    right = 0
    for j in range(end, len(a)):
        if a[j].isdigit():
            right = j
            break
            
    if right:
        if a[right+1].isdigit():
            y += int(a[right:right+2])
            a = a[:right] + str(y) + a[right+2:]
        else:
            y += int(a[right])
            a = a[:right] + str(y) + a[right+1:]
            
    a = a[:i] + '0' + a[end+1:]
    
    if left:
        if a[left-1].isdigit():
            x += int(a[left-1:left+1])
            a = a[:left-1] + str(x) + a[left+1:]
        else:
            x += int(a[left])
            a = a[:left] + str(x) + a[left+1:]
            
    return a
    
    
def reduce(a):
    reduced = True
    while reduced:
        reduced = False
        depth = 0
        left = 0
        for i, c in enumerate(a):
            if c == ',':
                continue
            elif c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            else:
                left = i
                
            if depth == 5:
                a = explode(a, i, left)
                reduced = True
                break
        else:
            for i, c in enumerate(a[:-2]):
                if a[i:i+2].isdecimal():
                    a = split(a, i)
                    reduced = True
                    break
    
    return a
    
    
def magnitude(a):
    if type(a) is list:
        return 3 * magnitude(a[0]) + 2 * magnitude(a[1])
    else:
        return a


numbers = []
with open('input.txt') as f:
    for line in f.readlines():
        numbers.append(line.strip().replace(' ', ''))
        
tot = numbers[0]
for n in numbers[1:]:
    tot = add(tot, n)
    tot = reduce(tot)
    print(tot)
print(magnitude(eval(tot)))
