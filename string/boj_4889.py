import sys

order = 1

while True:
    s = list(sys.stdin.readline().rstrip())

    if '-' in s:
        break

    stack = []
    change = 0
    for i in range(len(s)):
        if s[i] == '}':
            if not stack:  # 스택에 들어있는 게 없으면
                change += 1
                stack.append('{')  # 바꿔서 넣어줌
            else:
                stack.pop()
        else:  # s[i] == '{' 이면
            stack.append(s[i])

    change += (len(stack) // 2)

    print(str(order) + ". " + str(change))
    order += 1