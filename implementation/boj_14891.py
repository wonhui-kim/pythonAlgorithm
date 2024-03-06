import sys

wheel = []
for i in range(4):
    wheel.append(list(map(int, sys.stdin.readline().rstrip())))


def replace(arr, d):
    if d == -1:  # 반시계
        return turn_left(arr)
    else:
        return turn_right(arr)


# 반시계 방향 돌기
def turn_left(arr):
    turned = []
    for i in range(1, len(arr)):
        turned.append(arr[i])
    turned.append(arr[0])

    return turned


# 시계 방향 돌기
def turn_right(arr):
    turned = [arr[-1]]
    for i in range(len(arr) - 1):
        turned.append(arr[i])

    return turned


# 점수 계산
def score(wheel):
    result = 0
    for i in range(len(wheel)):
        result += (wheel[i][0] * (2 ** i))

    return result


k = int(sys.stdin.readline())
for i in range(k):
    idx, d = map(int, sys.stdin.readline().split())

    # 돌아야 할 톱니바퀴
    turn = []

    # 좌
    if idx - 1 > 0:
        for j in range(idx - 1, 0, -1):
            if wheel[j][6] != wheel[j - 1][2]:
                turn.append(j - 1)
            else:
                break

    # 우
    if idx - 1 < 4:
        for j in range(idx - 1, 3):
            if wheel[j][2] != wheel[j + 1][6]:
                turn.append(j + 1)
            else:
                break

    # 본인 돌기
    replaced = replace(wheel[idx - 1], d)
    wheel[idx - 1] = replaced

    for t in turn:
        direction = d
        if (idx - 1 - t) % 2 != 0:
            direction = (d * -1)
        replaced = replace(wheel[t], direction)
        wheel[t] = replaced

print(score(wheel))