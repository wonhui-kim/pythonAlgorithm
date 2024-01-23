import sys

N, M = map(int, sys.stdin.readline().split())
answer = [-1 for i in range(M)]


def print_arr(arr):
    for a in arr:
        print(a, end=' ')


def dfs(depth, after):
    if depth == M:
        print_arr(answer)
        print()
        return

    for i in range(after, N + 1):
        answer[depth] = i
        dfs(depth + 1, i + 1)


dfs(0, 1)