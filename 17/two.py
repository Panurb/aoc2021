from numba import njit


@njit
def run():
    count = 0
    for i in range(10000):
        for j in range(-10000, 10000):
            vx = i
            vy = j
            x = 0
            y = 0
            while True:
                x += vx
                y += vy
                if vx != 0:
                    vx -= vx // abs(vx)
                vy -= 1
                
                if left <= x <= right and bottom <= y <= top:
                    count += 1
                    break
                    
                if x > right or y < bottom:
                    break
                    
    return count


with open('input.txt') as f:
    line = f.read()
    x, y = line.split(':')[1].split(',')
    left, right = list(map(int, x.split('=')[1].split('..')))
    bottom, top = list(map(int, y.split('=')[1].split('..')))
                    
    print(run())
