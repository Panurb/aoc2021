from itertools import permutations


DIGITS = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 
          'abdefg', 'acf', 'abcdefg', 'abcdfg']


with open('input.txt') as f:
    count = 0
    for line in f.readlines():
        signals, output = line.split('|')
        signals = signals.split()
        output = output.split()
        
        for p in permutations('abcdefg'):
            def m(c):
                return p[ord(c) - 97]
                
            for s in signals + output:
                s = ''.join(sorted(map(m, s)))
                if s not in DIGITS:
                    break
            else:
                n = ''
                for o in output:
                    o = ''.join(sorted(map(m, o)))
                    n += str(DIGITS.index(o))
                count += int(n)

    print(count)
