import sys
import math
from decimal import Decimal

# 게임 횟수X, 이긴 횟수 Y
X, Y = map(int, sys.stdin.readline().split())


# 승률 구하는 함수 -> 소수점은 버리기에 trunc 사용
# 파이썬 float는 이진수 기반 연산으로, 오류 발생 가능성
# Decimal(문자열)을 통해 숫자를 10진수로 처리
def winning_rate(win, total):
    if win == 0:
        return 0
    return math.trunc(Decimal(str(win / total)) * 100)


# left는 1, right는 X의 범위인 1,000,000,000
# mid는 몇 판 더 해야하는지(승률이 변하는지)
def binary_search(left, right, value):
    answer = -1
    while left <= right:
        mid = (left + right) // 2

        rate = winning_rate(Y + mid, X + mid)

        # 구한 승률이 기존 승률보다 적거나 같으면 left 옮김
        if rate <= value:
            left = mid + 1
        else:  # 기존 승률보다 크면 right 옮김
            answer = mid
            right = mid - 1
    return answer


cur_rate = winning_rate(Y, X)
print(binary_search(1, 1000000000, cur_rate))