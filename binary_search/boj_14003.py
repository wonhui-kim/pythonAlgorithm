import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def lower_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left

def print_result(arr):
    print(len(arr))

    for a in arr:
        print(a, end=' ')
    print()

dp = []
lis = []
for a in arr:
    if (len(dp) == 0) or dp[-1] < a:
        dp.append(a)
        lis.append([len(dp) - 1, a])  # 저장되는 인덱스와 값 저장
    else:
        idx = lower_bound(dp, 0, len(dp) - 1, a)
        dp[idx] = a
        lis.append([idx, a])

result = [-1] * len(dp)
cur_idx = len(dp) - 1
for i in range(len(lis) - 1, -1, -1):
    if cur_idx < 0:
        break

    idx, value = lis[i]

    if cur_idx == idx:
        result[idx] = value
        cur_idx -= 1

print(len(dp))
print(" ".join(map(str, result)))