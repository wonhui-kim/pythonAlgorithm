import sys


def lower_bound(arr, left, right, value):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left


N = int(sys.stdin.readline())

temp_arr = []
for i in range(N):
    temp_arr.append(list(map(int, sys.stdin.readline().split())))

linked = dict()  # 어디에 연결된지 저장
temp_arr.sort()
arr = []
for t in temp_arr:
    arr.append(t[1])
    linked[t[1]] = t[0]

lis_info = []
dp = []
for a in arr:
    if (len(dp) == 0) or (dp[-1] < a):
        dp.append(a)
        lis_info.append([len(dp) - 1, linked[a], a])  # 인덱스, 연결노드, 본인 저장
    else:
        idx = lower_bound(dp, 0, len(dp) - 1, a)
        dp[idx] = a
        lis_info.append([idx, linked[a], a])

lis_result = [-1] * len(dp)
cur_idx = len(dp) - 1
for i in range(len(lis_info) - 1, -1, -1):
    if cur_idx < 0:
        break
    idx, link, value = lis_info[i]

    if cur_idx == idx:
        lis_result[idx] = value
        cur_idx -= 1

# lis에 속하지 않는 전깃줄 저장
removed = []
for l in lis_info:
    idx, link, value = l

    if lis_result[idx] != value:
        removed.append(link)

print(len(removed))
for r in removed:
    print(r)