import numpy as np
from numba import njit


I = np.eye(3, dtype=float)
X = np.array([[1, 0,  0], 
              [0, 0, -1], 
              [0, 1,  0]], dtype=float)
Y = np.array([[0,  0, 1], 
              [0,  1, 0], 
              [-1, 0, 0]], dtype=float)
Z = np.array([[0, -1, 0], 
              [1,  0, 0], 
              [0,  0, 1]], dtype=float)

YZ_ROTS = [I, Z, Z @ Z, Z @ Z @ Z, Y, Y @ Y @ Y]
X_ROTS = [I, X, X @ X, X @ X @ X]
ROTS = []
for yz in YZ_ROTS:
    for x in X_ROTS:
        ROTS.append(yz @ x)


@njit
def find_matches(target, origin, m):
    for fixed in origin[11:]:
        for f in target[11:]:
            offset = fixed - m @ f
            matches = 0
            for k, beacon in enumerate(origin):
                for b in target:
                    b = m @ b + offset
                    if np.array_equal(beacon, b):
                        matches += 1
                        break
                        
                if matches == 12:
                    for k, b in enumerate(target):
                        target[k] = m @ b + offset
                    return True
                #elif 12 - matches > len(origin) - k:
                #    break
                
    return False


scanners = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        
        if 'scanner' in line:
            scanner = []
        elif line == '':
            scanners.append(scanner)
        else:
            scanner.append(np.array(line.split(','), dtype=float))

beacons = set()
found = [36]
remaining = list(range(1, len(scanners)))
checked = []
while remaining:
    for j in found:
        for i in remaining:
            if (i, j) in checked:
                continue
            checked.append((i, j))
            for m in ROTS:
                if find_matches(scanners[i], scanners[j], m):
                    found.append(i)
                    remaining.remove(i)
                    print(found, remaining)
                    break

for s in scanners:
    for b in s:
        beacons.add(tuple(b))
    
print(len(beacons))
