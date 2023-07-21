import sys

tc = int(sys.stdin.readline())
for i in range(tc):
    n = int(sys.stdin.readline())  # 전화번호 수

    phones = []
    for i in range(n):
        phones.append(sys.stdin.readline().rstrip())

    # 정렬 -> 포함되면 앞에 올 것이므로!
    phones.sort()

    consistency = True
    for i in range(n - 1):
        prev = phones[i]
        cur = phones[i + 1]

        # 같은 경우 없으므로 길이가 크거나 같으면 skip
        if len(prev) >= len(cur):
            continue

        # 다음 요소의 접두사인 경우
        if prev == cur[0:len(prev)]:
            consistency = False  # 일관성 없어짐
            break  # 반복문 탈출

    if consistency:
        print("YES")
    else:
        print("NO")