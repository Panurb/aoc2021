polymer = ''
rules = dict()

with open('input.txt') as f:
    lines = f.readlines()
    polymer = lines[0].strip()
    for line in lines[2:]:
        line = line.strip()
        if line:
            start, end = line.split(' -> ')
            rules[start] = end
            
for _ in range(10):
    new = ''
    for i in range(len(polymer)):
        pair = polymer[i:i+2]
        if pair in rules.keys():
            new += pair[0] + rules[pair]
        else:
            new += pair[0]
    polymer = new
            
counts = dict()
for c in polymer:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 0
quants = sorted(counts.values())
print(quants)
print(quants[-1] - quants[0])
