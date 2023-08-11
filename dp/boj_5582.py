import sys

first = list(sys.stdin.readline().rstrip())
second = list(sys.stdin.readline().rstrip())

dp = [[0 for j in range(len(first))] for i in range(len(second))]

for i in range(len(second)):
    for j in range(len(first)):
        if first[j] != second[i]:
            continue
        else: #같으면
            if i > 0 and j > 0:
                dp[i][j] += dp[i-1][j-1] + 1
            else:
                dp[i][j] += 1

answer = -1
for i in range(len(second)):
    for j in range(len(first)):
        answer = max(answer, dp[i][j])

print(answer)