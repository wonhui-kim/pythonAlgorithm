import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

operators = []
for i in range(4):
    temp_op = '+'

    if i == 1:
        temp_op = '-'
    elif i == 2:
        temp_op = '*'
    elif i == 3:
        temp_op = '//'

    for j in range(op[i]):
        operators.append(temp_op)

answer = [-1 for i in range(N - 1)]
visit = [False for i in range(len(operators))]


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        if a < 0:
            a = a * -1
            return (a // b) * -1
        return a // b


def find_result(arr, operator):
    result = arr[0]

    for i in range(1, len(arr)):
        result = calculate(result, arr[i], operator[i - 1])

    return result


min_result = int(10e9)
max_result = int(10e9) * -1


def dfs(depth):
    global min_result
    global max_result

    if depth == N - 1:
        # 계산 (max, min)
        temp_result = find_result(numbers, answer)

        if temp_result < min_result:
            min_result = temp_result

        if temp_result > max_result:
            max_result = temp_result

        return

    for i in range(len(operators)):
        if not visit[i]:
            visit[i] = True
            answer[depth] = operators[i]
            dfs(depth + 1)
            visit[i] = False


dfs(0)
print(max_result)
print(min_result)