import sys

N, M = map(int, sys.stdin.readline().split())
daily_spend = []
for i in range(N):
    daily_spend.append(int(sys.stdin.readline()))


def cnt_withdraw(arr, money):
    cnt = 1
    left = money

    for a in arr:
        if a > left:
            cnt += 1
            left = money
        left -= a

    return cnt


def binary_search(l, r, target):
    answer = 0

    while l <= r:
        mid = (l + r) // 2

        cnt = cnt_withdraw(daily_spend, mid)

        if cnt <= target:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer


print(binary_search(max(daily_spend), sum(daily_spend), M))