class Cave:
    def __init__(self, name):
        self.neighbors = set()
        self.name = name
        self.small = name[0].islower()
        self.visits = 0
        
        
def count_paths(caves, cave, end, paths):
    if cave is end:
        return paths + 1
        
    cave.visits += 1
    twice = False
    for c in caves.values():
        if c.small and c.visits == 2:
            twice = True
            break
            
    for n in cave.neighbors:
        if n.name == 'start':
            continue
        if n.small:
            if twice:
                if n.visits > 0:
                    continue
            else:
                if n.visits > 1:
                    continue

        paths = count_paths(caves, n, end, paths)
        
    cave.visits -= 1
    return paths


caves = dict()
with open('input.txt') as f:
    for line in f.readlines():
        start, end = line.strip().split('-')
        if start not in caves:
            caves[start] = Cave(start)
        if end not in caves:
            caves[end] = Cave(end)
        
        caves[start].neighbors.add(caves[end])
        caves[end].neighbors.add(caves[start])

print(count_paths(caves, caves['start'], caves['end'], 0))
