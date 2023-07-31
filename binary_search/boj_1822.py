import sys

a, b = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

set_a = set(A)
set_b = set(B)

sorted_list = sorted(set_a - set_b)

print(len(sorted_list))

if len(sorted_list) != 0:
    for s in sorted_list:
        print(s, end=' ')