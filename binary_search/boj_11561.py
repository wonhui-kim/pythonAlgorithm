import sys

T = int(sys.stdin.readline())

# 등차수열 합 공식
def sequence(a):
    return a * (a + 1) / 2

def parametric_search(left, right, num):
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if sequence(mid) == num:
            return mid

        if sequence(mid) < num:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


for i in range(T):
    N = int(sys.stdin.readline())

    print(parametric_search(1, N, N))