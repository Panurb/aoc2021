with open('input.txt') as f:
    n = 0
    lines = f.readlines()
    prev = int(lines[0])
    for line in lines[1:]:
        cur = int(line)
        if cur > prev:
            n += 1
        prev = cur
    print(n)
    

with open('input.txt') as f:
    n = 0
    nums = [int(x) for x in f.readlines()]
    for i in range(1, len(nums) - 2):
        if sum(nums[i:i+3]) > sum(nums[i-1:i+2]):
            n += 1
    print(n)
    