import sys

while True:
    temp_n, temp_m = sys.stdin.readline().split()

    if temp_n == "0" and temp_m == "0.00":
        break

    n = int(temp_n)
    m = int(float(temp_m) * 100 + 0.5)

    c = [0]  # 칼로리
    p = [0]  # 가격

    for i in range(n):
        temp_c, temp_p = sys.stdin.readline().split()

        c.append(int(temp_c))
        p.append(int(float(temp_p) * 100 + 0.5))

    dp = [0 for i in range(m + 1)]

    for k in range(n + 1):
        for w in range(m + 1):
            if w >= p[k]:
                dp[w] = max(dp[w], dp[w - p[k]] + c[k])

    print(dp[m])