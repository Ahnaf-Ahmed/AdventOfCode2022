# Part 1

# with open('input.txt') as f:
#     line = f.readline().rstrip()
#     total = 0
#     while line:
#         line = list(line)
#         half = len(line)//2
#         one = line[:half]
#         two = line[half:]
#         common = list(set(one).intersection(two))[0]
#         num = ord(common)
#         total += num - (96 if num > 96 else 38)
#         line = f.readline().rstrip()
#     print(f"total is {total}")



# Part 2

with open('input.txt') as f:
    line1 = f.readline().rstrip()
    line2 = f.readline().rstrip()
    line3 = f.readline().rstrip()

    total = 0
    while line1:
        badge = list(set(line1).intersection(line2, line3))[0]
        num = ord(badge)
        total += num - (96 if num > 96 else 38)
        
        line1 = f.readline().rstrip()
        line2 = f.readline().rstrip()
        line3 = f.readline().rstrip()
        

    print(f"total is {total}")