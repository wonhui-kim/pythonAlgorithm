import sys
from itertools import permutations


def possible_result(guess_num, guess_answer):
    possible = []
    for i in permutations('123456789', 3):
        # 스트라이크 개수
        s = 0
        for j in range(3):
            if i[j] == guess_num[j]:
                s += 1

        # 볼 개수
        b = 0
        for j in range(3):
            if i[j] in guess_num:
                b += 1
        b -= s

        if guess_answer == [s, b]:
            possible.append(i)

    return possible


N = int(sys.stdin.readline())

result = set()
for i in range(N):
    num, strike, ball = map(int, sys.stdin.readline().split())
    temp_result = set(possible_result(str(num), [strike, ball]))

    if len(result) == 0:
        result = temp_result
    else:
        result = result.intersection(temp_result)

print(len(result))
