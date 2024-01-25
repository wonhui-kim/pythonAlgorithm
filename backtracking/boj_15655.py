import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

answer = [-1 for i in range(M)]


def print_arr(arr):
    for a in arr:
        print(a, end=' ')
    print()


def dfs(depth, after):
    if depth == M:
        print_arr(answer)
        return

    for i in range(after, N):
        answer[depth] = array[i]
        dfs(depth + 1, i + 1)


dfs(0, 0)