import sys

# 전깃줄 개수
N = int(sys.stdin.readline())

line = []
for i in range(N):
    line.append(list(map(int, sys.stdin.readline().split())))

line.sort()  # lower_bound 적용한 LCS 위해 정렬


def lower_bound(left, right, arr, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


dp = [line[0][1]]  # 첫번째 라인 삽입
for i in range(1, N):
    index = lower_bound(0, len(dp) - 1, dp, line[i][1])

    if index < len(dp):
        dp[index] = line[i][1]
    else:
        dp.append(line[i][1])

print(N - len(dp))