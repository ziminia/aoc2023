file1 = open('input1.txt', 'r')
input = file1.readlines()

#this is what happens when you code at 1:30 AM
numberMap = {
    "one" : "o1ne",
    "two" : "t2wo",
    "three" : "t3hree",
    "four" : "f4our",
    "five" : "f5ive",
    "six" : "s6ix",
    "seven" : "s7even",
    "eight" : "e8ight",
    "nine": "n9ine"
}

total = 0
for line in input:
    for key in numberMap:
        line = line.replace(key, numberMap[key])
    print(line)
    first = 0
    firstSet = False
    last = 0
    for i in range(len(line)):
        char = line[i]
        if char.isnumeric():
            if not firstSet:
                firstSet = True
                first = int(char)*10
            last = int(char)
    total += first + last

print(total)