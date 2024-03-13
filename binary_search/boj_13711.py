import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


def lower_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left


def lis(arr):
    dp = []

    for a in arr:
        if (len(dp) == 0) or (dp[-1] < a):
            dp.append(a)
        else:
            dp[lower_bound(dp, 0, len(dp) - 1, a)] = a

    return len(dp)


# 인덱스 배열 구하기 - a 배열의 b 위치
# A 인덱스 저장
a_dic = dict()
for i in range(len(A)):
    a_dic[A[i]] = i

idx_arr = []
for b in B:
    idx_arr.append(a_dic[b])

print(lis(idx_arr))