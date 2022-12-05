import re

# Part 1

# firstEmpty = True
# with open('input.txt') as f:
#     line = f.readline().rstrip('\n')
#     numStacks = len(line) // 4 + 1
#     stacks = [[] for x in range(numStacks)]
#     while line or firstEmpty:
#         if "move" in line:
#             [amount, src, dest] = [int(x) for x in re.search("move (\d*) from (\d*) to (\d*)", line).groups()]
#             src = src-1
#             dest = dest-1

#             for i in range(amount):
#                 stacks[dest].append(stacks[src].pop())
        
#         elif '[' in line:

#             parts = [line[i:i+4].strip(" []") for i in range(0, len(line), 4)]
#             for i, part in enumerate(parts):
#                 if len(part) != 0:
#                     stacks[i].insert(0, part)
        
#         elif not line:
#             firstEmpty = False
#         line = f.readline().rstrip('\n')
#     for stack in stacks:
#         print(stack[-1],end="", sep="")


# Part 2

firstEmpty = True
with open('input.txt') as f:
    line = f.readline().rstrip('\n')
    numStacks = len(line) // 4 + 1
    stacks = [[] for x in range(numStacks)]
    while line or firstEmpty:
        if "move" in line:
            [amount, src, dest] = [int(x) for x in re.search("move (\d*) from (\d*) to (\d*)", line).groups()]
            src = src-1
            dest = dest-1
            position = len(stacks[dest])
            for i in range(amount):
                stacks[dest].insert(position,stacks[src].pop())
        
        elif '[' in line:

            parts = [line[i:i+4].strip(" []") for i in range(0, len(line), 4)]
            for i, part in enumerate(parts):
                if len(part) != 0:
                    stacks[i].insert(0, part)
        
        elif not line:
            firstEmpty = False
        line = f.readline().rstrip('\n')
    for stack in stacks:
        print(stack[-1],end="", sep="")