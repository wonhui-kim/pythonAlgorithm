import sys

N = int(sys.stdin.readline())
temp_std = list(map(int, sys.stdin.readline().split()))

std = []  # b,s,g,p 까지의 기준 저장
dia = -1  # 다이아는 따로 저장 min은 dia값이고, max가 없기 때문.
for i in range(len(temp_std)):
    std.append(temp_std[i] - 1)  # s값-1이 b의 최대값

    if i == len(temp_std) - 1:  # 다이아는 따로 저장
        dia = temp_std[i]

# B,S,G,P,D 기준은 std 배열에 인덱스 0,1,2,3으로 저장되어 있음
dic = {"B": 0, "S": 1, "G": 2, "P": 3}

# 상민이가 N개월까지 받은 등급
grades = list(sys.stdin.readline().rstrip())

# 최대 소비 저장
consume = [0 for i in range(N + 1)]
for i in range(N):  # N == len(grades)
    grade = grades[i]

    # 다이아등급기준액이 최대이기 때문에
    if grade == "D":
        consume[i + 1] = dia
    else:  # 해당 달의 최대 소비액은 해당 달 등급 기준 최대액수 - 이전달 소비량임
        consume[i + 1] = std[dic[grade]] - consume[i]

# 최대 과금액 출력이므로 consume 배열 모두 더한 값
print(sum(consume))