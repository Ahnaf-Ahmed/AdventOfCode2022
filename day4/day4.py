def overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

overlap = 0
with open('input.txt') as f:
    line = f.readline()
    while line:
        [one,two] = line.split(',')
        
        one = [int(x) for x in one.split('-')]
        two = [int(x) for x in two.split('-')]
        
        if (one[0] <= two[0] and one[1] >= two[0]) or (two[0] <= one[0] and two[1] >= one[0]):
            overlap += 1
        line = f.readline()
print(f"overlap is {overlap}")