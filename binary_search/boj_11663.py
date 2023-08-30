import sys

N, M = map(int, sys.stdin.readline().split())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()


def lowerbound(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def upperbound(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return left


for i in range(M):
    length = len(graph) - 1

    a, b = map(int, sys.stdin.readline().split())
    start = lowerbound(graph, 0, length, a)
    end = upperbound(graph, 0, length, b)

    print(end - start)