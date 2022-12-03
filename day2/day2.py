def wrap(x:int):
    return ((x-1) + 3) % 3 + 1

convert = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

table = [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]

total = 0
#Part 1

# with open('input.txt') as f:
#     line = f.readline()
#     while line:
#         line = line.strip("\n")
#         [A, B] = line.split()
#         A = convert[A]
#         B = convert[B]
#         total += table[B][A] + B + 1
#         line = f.readline()
# print(f"total is {total}")

#Part 2
with open('input.txt') as f:
    line = f.readline()
    while line:
        line = line.strip("\n")
        [A, B] = line.split()
        A = convert[A]
        B = convert[B]
        resultMod = B-1
        choice = wrap(A+resultMod+1)
        total += 3*B + choice
        line = f.readline()
print(f"total is {total}")


convert = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}
