import sys
from collections import deque


def bfs(a, b, start, end):
    deq = deque()
    deq.append([start, 0])
    visited = set()

    while deq:
        cur, cur_depth = deq.popleft()

        if cur == end:
            return cur_depth

        candidate = [cur - 1, cur + 1, cur - a, cur + a, cur - b, cur + b, cur * a, cur * b]

        for c in candidate:
            if c >= 0 and c <= 100000 and (c not in visited):
                visited.add(c)
                deq.append([c, cur_depth + 1])


A, B, N, M = map(int, sys.stdin.readline().split())
print(bfs(A, B, N, M))