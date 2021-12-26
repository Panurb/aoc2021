rolls = 0
def roll():
    global rolls
    rolls += 1
    return (rolls - 1) % 100 + 1


players = []
scores = []

with open('input.txt') as f:
    for line in f.readlines():
        players.append(int(line.split(':')[-1].strip()))
        scores.append(0)

    
turn = 0
while True:
    move = sum(roll() for _ in range(3))
    players[turn] = (players[turn] + move - 1) % 10 + 1
    scores[turn] = scores[turn] + players[turn]
    if scores[turn] >= 1000:
        break
    turn = (turn + 1) % 2

print(min(scores) * rolls)
