fish = 9 * [0]

with open('input.txt') as f:
    for n in f.readlines()[0].split(','):
        fish[int(n)] = fish[int(n)] + 1
        
for d in range(256):
    new = fish[0]
    for i in range(len(fish) - 1):
        fish[i] = fish[i + 1]
            
    fish[8] = new
    fish[6] = fish[6] + new

print(sum(fish))
