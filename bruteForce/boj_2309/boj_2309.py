import itertools
import sys

dwarfs = []
for i in range(9):
    dwarfs.append(int(sys.stdin.readline()))

dwarfs.sort()

for i in itertools.combinations(dwarfs, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break
