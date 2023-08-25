import sys
import itertools

while True:
    line = list(map(int, sys.stdin.readline().split()))

    if line == [0]:
        break

    k = line[0]
    S = line[1:len(line)]

    for i in itertools.combinations(S, 6):
        for j in i:
            print(j, end=' ')
        print()

    print()