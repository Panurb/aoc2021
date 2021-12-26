with open('input.txt') as f:
    count = 0
    for line in f.readlines():
        signals, output = line.split('|')
        signals = signals.split()
        output = output.split()
        
        connections = {c: 'abcdefg' for c in 'abcdefg'}
        
        for signal in output:
            n = len(signal)
            if n in [2, 3, 4, 7]:
                count += 1
                            
    print(count)
