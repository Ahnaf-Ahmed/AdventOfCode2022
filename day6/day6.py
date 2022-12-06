# Part 1

# with open('input.txt') as f:
#     line = f.readline()
#     start = 0
#     end = 0

#     while end < len(line):
#         if end-start < 4:
#             end += 1
        
#         pos = line[start:end].find(line[end])
#         if pos == -1 and end-start == 4:
#             break
#         else:
#             start += pos+1

#     print(end)


# Part 2

with open('input.txt') as f:
    line = f.readline()
    start = 0
    end = 0

    while end < len(line):
        if end-start < 14:
            end += 1
        
        pos = line[start:end].find(line[end])
        if pos == -1 and end-start == 13:
            break
        else:
            start += pos+1
        
    print(end+1)
    