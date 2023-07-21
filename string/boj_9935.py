import sys

before = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())

stack = []
for b in before:
    stack.append(b)

    remove_count = len(stack) - len(bomb)  # 0

    if remove_count >= 0:  # 최소한 시작 인덱스가 0이상

        if stack[remove_count:len(stack)] == bomb:
            for i in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")