def prod(xs):
    val = 1
    for x in xs:
        val *= x
    return val


def parse_packet(binary, start):
    version = int(binary[start:start+3], 2)
    type_id = int(binary[start+3:start+6], 2)
    print(f'version: {version}, type ID: {type_id}')
    
    values = []
    end = None
    if type_id == 4:
        value = ''
        i = start + 6
        while True:
            value += binary[i+1:i+5]
            if binary[i] == '0':
                end = i + 5
                break
            i+= 5
        values.append(int(value, 2))
    else:
        if type_id == 0:
            func = sum
        elif type_id == 1:
            func = prod
        elif type_id == 2:
            func = min
        elif type_id == 3:
            func = max
        elif type_id == 5:
            func = lambda x: int(x[0] > x[1])
        elif type_id == 6:
            func = lambda x: int(x[0] < x[1])
        elif type_id == 7:
            func = lambda x: int(x[0] == x[1])
            
        length_type_id = binary[start+6]
        print('length_type_id', length_type_id)
        if length_type_id == '0':
            i = start + 7
            length = int(binary[i:i+15], 2)
            print('length', length)
            i += 15
            end = i + length
            while i < end:
                vers, vals, i = parse_packet(binary, i)
                version += vers
                values += vals
            values = [func(values)]
        else:
            i = start + 7
            sub_packets = int(binary[i:i+11], 2)
            print('sub', sub_packets, binary[i:i+11])
            i += 11
            for _ in range(sub_packets):
                vers, vals, i = parse_packet(binary, i)
                version += vers
                values += vals
            values = [func(values)]
            end = i
            
    return version, values, end


with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        message = line.strip()
        binary = ''
        for c in message:
            binary += bin(int(c, 16))[2:].zfill(4)
        
        print(binary)
        
        start = 0
        version, values, start = parse_packet(binary, start)
        print(values)
