import random


func = 'def f(inp):\n    w = 0\n    x = 0\n    y = 0\n    z = 0\n'

with open('input.txt') as f:
    i = 0
    for line in f.readlines():
        func += '    '
        match line.strip().split():
            case 'inp', a:
                func += f'{a} = inp[{i}]'
                i += 1
            case 'add', a, b:
                func += f'{a} += {b}'
            case 'mul', a, b:
                func += f'{a} *= {b}'
            case 'div', a, b:
                if b != 1:
                    func += f'{a} //= {b}'
            case 'mod', a, b:
                func += f'{a} %= {b}'
            case 'eql', a, b:
                func += f'{a} = int({a} == {b})'
        func += '\n'
                
func += '    return w, x, y, z'

#print(func)
exec(func)

def iterative_search():
    inp = list(map(int, '51147191111111'))
    digits = [7, 8, 9, 10, 11, 12, 13]
         
    while True:
        i = len(digits) - 1
        while True:
            inp[digits[i]] = (inp[digits[i]] + 1) % 9 or 9
            if inp[digits[i]] == 1:
                i -= 1
            else:
                break
                
        z = f(inp)[-1]
        print(inp, z)
        if z == 0:
            print(int(''.join(map(str, inp))))
            break
            
            
def random_search():
    while True:
        inp = [int(8 * random.random() + 1) for _ in range(14)]
        inp[0] = 5
        inp[1] = 1
        inp[2] = 1
        inp[3] = 4
        inp[4] = 7
             
        for _ in range(100):
            z = f(inp)[-1]
            for i in range(5, 14):
                inp[i] = (inp[i] - 1) % 9 or 9
                if f(inp)[-1] <= z:
                    continue
                else:
                    inp[i] = (inp[i] + 1) % 9 or 9
                    
            if z == 0:
                print(int(''.join(map(str, inp))))
                break
                
                
iterative_search()
#random_search()
# 51149394861991, too high
# 51148291161261
