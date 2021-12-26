with open('input.txt') as f:
    avgs = 12 * [0]
    for line in f.readlines():
        for i, b in enumerate(line):
            if b != '\n':
                avgs[i] += int(b) / 1000
        
    gamma = ''
    epsilon = ''
    for avg in avgs:
        gamma += str(round(avg))
        epsilon += str(round(1 - avg))
            
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon)
    
    
import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)
    
    
with open('input.txt') as f:
    data = ['00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010']
    data = f.readlines()

    lines = list(data)
    b = 0
    while len(lines) > 1:
        ones = 0
        zeros = 0
        for line in lines:
            n = int(line[b])
            if n == 1:
                ones += 1
            else:
                zeros += 1
                
        most_common = 1
        if zeros > ones:
            most_common = 0
        
        lines = [l for l in lines if int(l[b]) == most_common]
        b += 1
        
    oxy = int(lines[0], 2)
    
    lines = list(data)
    b = 0
    while len(lines) > 1:
        ones = 0
        zeros = 0
        for line in lines:
            n = int(line[b])
            if n == 1:
                ones += 1
            else:
                zeros += 1
                
        least_common = 0
        if zeros > ones:
            least_common = 1
        
        lines = [l for l in lines if int(l[b]) == least_common]
        b += 1
        
    co2 = int(lines[0], 2)
    
    print(oxy, co2)
    print(oxy * co2)
    # 432567, 428460
