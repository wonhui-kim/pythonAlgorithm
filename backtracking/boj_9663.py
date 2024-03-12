import sys

N = int(sys.stdin.readline())

visited = [False] * N
answer = [-1] * N

result = 0


def backtracking(depth, upper, lower):
    global result

    if depth == N:
        result += 1
        return

    for i in range(N):
        if (not visited[i]) and (depth + i not in upper) and (depth - i not in lower):
            visited[i] = True
            upper.add(depth + i)
            lower.add(depth - i)
            answer[depth] = i
            backtracking(depth + 1, upper, lower)
            visited[i] = False
            upper.remove(depth + i)
            lower.remove(depth - i)


upper = set()
lower = set()
backtracking(0, upper, lower)
print(result)