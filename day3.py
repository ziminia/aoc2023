import re

file1 = open('input3.txt', 'r')
input = file1.readlines()

total = 0
totalGearRatio = 0
grid = []

potentialGears = {}

for line in input:
    grid.append(line)
for i in range(len(grid)):
    numberValid = False
    number = ""
    symbol = ""
    markGears = set()
    for j in range(len(grid[i])):
        c = grid[i][j]
        if c.isnumeric():
            number += c
            for m in range(max(i - 1, 0), min(i + 2, len(grid))):
                for n in range(max(j - 1, 0), min(j + 2, len(grid[i]))):
                    if grid[m][n] != '.' and not grid[m][n].isnumeric() and not grid[m][n] == "\n":
                        numberValid = True
                        symbol = grid[m][n]
                        if symbol == '*':
                            markGears.add((m,n))
        elif len(number) > 0 and numberValid:
            total += int(number)
            if len(markGears) > 0:
                for g in markGears:
                    if g in potentialGears:
                        potentialGears[g].append(int(number))
                    else:
                        potentialGears[g] = [int(number)]
            number = ""
            numberValid = False
            markGears.clear()
        else:
            number = ""
            numberValid = False
    if len(number) > 0 and numberValid:
        total += int(number)
        if len(markGears) > 0:
            for g in markGears:
                if g in potentialGears:
                    potentialGears[g].append(int(number))
                else:
                    potentialGears[g] = [int(number)]
for p in potentialGears:
    val = potentialGears[p]
    if len(val) == 2:
        totalGearRatio += val[0]*val[1]

print("sum of part numbers " + str(total))
print("total gear ratio " + str(totalGearRatio))