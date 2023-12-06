import bisect
import sys

def resolveSeed(seed, maps):
    val = seed
    for m in maps:
        # binary search to find the range we're checking
        pos = bisect.bisect_right(m, (val, sys.maxsize, sys.maxsize))
        if pos > 0:
            pos = pos - 1
        reference = m[pos]
        if val >= reference[0] and val < reference[0] + reference[2]:
            val = reference[1] + val - reference[0]
    return val

file1 = open('input5.txt', 'r')
input = file1.readlines()

shortestDistance = sys.maxsize

mapIndex = -1
seeds = []
maps = []
for line in input:
    if line.startswith("seeds"):
        tokens = line.split()
        for s in tokens:
            if s.isnumeric():
                seeds.append(int(s))
    elif "map:" in line:
        maps.append([])
        mapIndex += 1
    else:
        tokens = line.split()
        if len(tokens) == 3:
            # we want the source index to come first
            maps[mapIndex].append((int(tokens[1]),int(tokens[0]),int(tokens[2])))
# sort so we can use binary search
# yes I know these list are tiny shut up
for m in maps:
    m.sort()

for s in seeds:
    distance = resolveSeed(s, maps)
    if distance < shortestDistance:
        shortestDistance = distance

print("shortest distance", shortestDistance)