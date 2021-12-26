crabs = []

max_pos = 0
with open('input.txt') as f:
    for n in f.readlines()[0].split(','):
        crabs.append(int(n))
        max_pos = max(max_pos, int(n))

min_cost = len(crabs) * max_pos
for pos in range(max_pos):
    cost = 0
    for crab in crabs:
        cost += abs(crab - pos)
    min_cost = min(min_cost, cost)

print(min_cost)
