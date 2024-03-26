import sys

N = int(sys.stdin.readline())
answer = [-1 for i in range(N)]


def check(arr, length):
    check_list = arr[:length]
    for i in range(1, length // 2 + 1):
        if check_list[length - i:] == check_list[length - i * 2:length - i]:
            return False
    return True


def print_answer(arr):
    for a in arr:
        print(a, end='')


def backtracking(depth):
    if not check(answer, depth):
        return

    if depth == N:
        print_answer(answer)
        exit(0)

    for i in range(1, 4):  # 1~3
        if depth >= 1 and answer[depth - 1] == i:  # 이전 거랑 같으면 스킵
            continue
        answer[depth] = i
        backtracking(depth + 1)


backtracking(0)