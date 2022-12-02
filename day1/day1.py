elves = []
count = 0
with open('input.txt') as f:
    line = f.readline()
    if line:
        elves.append(0)
    while line:
        if line == '\n':
            count += 1
            line = 0
            elves.append(line)
        elves[count] += int(line)
        line = f.readline()

print(max(elves))


sort = sorted(elves, reverse=True)
print(sort[0] + sort[1] + sort[2])
