import sys
def cut_count(arr, unit):
    count = 0
    for i in arr:
        count += (i // unit)  # unit 기준으로 나올 수 있는 랜선 수

    return count

def binary_search(arr, start, end, target):
    answer = 0

    while (start <= end):
        mid = (start + end) // 2

        total = cut_count(arr, mid)

        if total >= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

K, N = map(int, sys.stdin.readline().split())

lan = []
for i in range(K):
    lan.append(int(sys.stdin.readline()))

lan.sort()
print(binary_search(lan, 1, lan[-1], N))