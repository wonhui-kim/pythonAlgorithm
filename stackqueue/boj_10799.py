import sys

stick = list(sys.stdin.readline().rstrip())

stack = []
stick_cnt = 0
idx = 0

while idx < len(stick):
    if stick[idx] == "(" and stick[idx + 1] == ")":  # 레이저인 경우
        stick_cnt += len(stack)
        idx += 2
        continue

    if stick[idx] == "(":  # 스틱 시작
        stack.append(stick[idx])
    else:  # 스틱 끝
        stick_cnt += 1
        stack.pop()

    idx += 1

print(stick_cnt)