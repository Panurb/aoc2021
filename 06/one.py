fish = []

with open('input.txt') as f:
    for n in f.readlines()[0].split(','):
        fish.append(int(n))
        
#fish = [3,4,3,1,2]
        
for d in range(80):
    print(d, len(fish))
    new = 0
    for i, f in enumerate(fish):
        if f == 0:
            fish[i] = 6
            new += 1
        else:
            fish[i] = f - 1
            
    for _ in range(new):
        fish.append(8)

print(len(fish))
