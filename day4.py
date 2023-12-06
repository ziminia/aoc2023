file1 = open('input4.txt', 'r')
input = file1.readlines()

total = 0
totalCards = 0

table = [1]

for i, line in enumerate(input):
    tokens = line.split()
    winningSet = set()
    numbersPresent = set()
    separator = False
    for t in tokens:
        if t == "|":
            separator = True
        if t.isnumeric():
            if separator:
                numbersPresent.add(t)
            else:
                winningSet.add(t)
    scoringSet = winningSet & numbersPresent
    if len(scoringSet) > 0:
        total += 2**(len(scoringSet) - 1)
    if len(table) < i + 1:
        table.append(1)
    print("applying", table[i],"from card", i, "to the next", len(scoringSet), "cards")
    for n in range(1, len(scoringSet)+1):
        if (len(table) <= i + n):
            table.append(1 + table[i])
        else:
            table[i+n] += table[i]
    totalCards += table[i]

print("sum of points " + str(total))
print("total scratchcards " + str(totalCards))