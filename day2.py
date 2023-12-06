import re

file1 = open('input2.txt', 'r')
input = file1.readlines()

colorMaxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0
totalPower = 0
for line in input:
    data = re.split("[;:,]", line)
    index = 0
    possible = True
    # this will be fiiiiine
    colorMins = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for d in data:
        tokens = d.split()
        if tokens[0] == "Game":
            index = int(tokens[1])
        if tokens[0].isnumeric():
            val = int(tokens[0])
            if val > colorMaxes[tokens[1]]:
                possible = False
            if val > colorMins[tokens[1]]:
                colorMins[tokens[1]] = val
    if possible:
        total += index
    totalPower += colorMins["red"]*colorMins["blue"]*colorMins["green"]

print("sum of ids of possible games " + str(total))
print("sum of powers " + str(totalPower))