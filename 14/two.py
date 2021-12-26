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
            
pairs = dict()
overlaps = dict()
for pair in rules.keys():
    pairs[pair] = 0
    for c in pair:
        if c not in overlaps:
            overlaps[c] = 0

for i in range(len(polymer) - 1):
    pair = polymer[i:i+2]
    pairs[pair] += 1

            
for i in range(40):
    new = dict()
    for pair in pairs:
        if pair in rules.keys():
            out = pair[0] + rules[pair]
            n = pairs[pair]
            if out in new:
                new[out] += n
            else:
                new[out] = n
                
            out = rules[pair] + pair[1]
            if out in new:
                new[out] += n
            else:
                new[out] = n
                
            if pair in new:
                new[pair] -= n
            else:
                new[pair] = -n
                
            overlaps[rules[pair]] += n
            
    for pair in new:
        pairs[pair] += new[pair]
        
counts = dict()
for pair in pairs:
    for c in pair:
        if c in counts:
            counts[c] += pairs[pair]
        else:
            counts[c] = pairs[pair]

quants = sorted([counts[c] - overlaps[c] for c in counts.keys()])
print(quants)
print(quants[-1] - quants[0] + 2)
#7155869758392, too low
