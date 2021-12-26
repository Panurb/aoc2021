FLIPPED = {')': '(', ']': '[', '}': '{', '>': '<'}
POINTS = {'(': 1, '[': 2, '{': 3, '<': 4}

with open('input.txt') as f:
    scores = []
    for line in f.readlines():
        chunks = []
        for c in line.strip():
            if c in '([{<':
                chunks.append(c)
            elif chunks[-1] == FLIPPED[c]:
                chunks.pop()
            else:
                break
        else:
            if chunks:
                score = 0
                for c in reversed(chunks):
                    score = 5 * score + POINTS[c]
                scores.append(score)
                
    scores = sorted(scores)
    print(scores[len(scores) // 2])
