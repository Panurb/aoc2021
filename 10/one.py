FLIPPED = {')': '(', ']': '[', '}': '{', '>': '<'}
POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}

with open('input.txt') as f:
    points = 0
    for line in f.readlines():
        chunks = []
        for c in line.strip():
            if c in '([{<':
                chunks.append(c)
            elif chunks[-1] == FLIPPED[c]:
                chunks.pop()
            else:
                points += POINTS[c]
                break
                
    print(points)
