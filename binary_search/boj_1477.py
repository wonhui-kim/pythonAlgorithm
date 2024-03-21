import sys

N, M, L = map(int, sys.stdin.readline().split())
places = list(map(int, sys.stdin.readline().split()))
places.append(0)
places.append(L)
places.sort()


def binary_search(arr, left, right, target):
    answer = -1

    while left <= right:
        mid = (left + right) // 2  # 간격

        cnt = 0
        for i in range(len(arr) - 1):
            if ((arr[i + 1] - arr[i]) > mid) and mid > 0:
                cnt += (arr[i + 1] - arr[i] - 1) // mid

        if cnt > target:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid

    return answer


print(binary_search(places, 1, L - 1, M))