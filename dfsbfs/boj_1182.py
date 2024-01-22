import sys

def dfs(index, arr_sum):
    global answer

    if index >= N:  # 끝 원소이면
        return

    arr_sum += arr[index]

    if arr_sum == S:
        answer += 1

    # 포함하는 경우
    dfs(index + 1, arr_sum)

    # 포함하지 않는 경우
    dfs(index + 1, arr_sum - arr[index])


N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
dfs(0, 0)

print(answer)