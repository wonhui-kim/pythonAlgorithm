import sys

N = int(sys.stdin.readline())
fluid = list(map(int, sys.stdin.readline().split()))

fluid.sort()


def two_pointer(arr, n):
    min_value = int(10e9)

    result = [arr[0], arr[1]]

    left = 0
    right = n - 1

    while left < right:
        two_sum = arr[left] + arr[right]

        if abs(two_sum) < min_value:
            min_value = abs(two_sum)
            result = [arr[left], arr[right]]

            if min_value == 0:
                return result

        if two_sum < 0: #합이 음수이면 left를 오른쪽으로 이동
            left += 1
        else: #합이 양수이면 right를 왼쪽으로 이동하여 0에 가깝게 함
            right -= 1

    return result


answer = two_pointer(fluid, N)
for a in answer:
    print(a, end=' ')