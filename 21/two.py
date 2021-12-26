ROLLS = []
for roll_1 in range(1, 4):
        for roll_2 in range(1, 4):
            for roll_3 in range(1, 4):
                ROLLS.append(roll_1 + roll_2 + roll_3)
#ROLLS = [ROLLS.count(x) for x in range(3, 10)]


wins = dict()


def turn(players, scores, player):
    global wins

    state = (players[0], players[1], scores[0], scores[1], player)
    
    if state in wins:
        return wins[state]

    w = [0, 0]
    for roll in ROLLS:
        players[player] = (players[player] + roll) % 10
        scores[player] += players[player] + 1
        
        if scores[player] >= 21:
            w[player] += 1
        else:
            t = turn(players, scores, (player + 1) % 2)
            w[0] += t[0]
            w[1] += t[1]
        
        scores[player] -= players[player] + 1
        players[player] = (players[player] - roll) % 10
        
    wins[state] = w
    return w


players = [0, 0]
scores = [0, 0]

with open('input.txt') as f:
    for i, line in enumerate(f.readlines()):
        players[i] = int(line.split(':')[-1].strip()) - 1

print(max(turn(players, scores, 0)))
