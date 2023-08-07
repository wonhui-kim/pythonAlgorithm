import sys

N = int(sys.stdin.readline())

dic = {}
word = []
for i in range(N):
    word.append(list(sys.stdin.readline().rstrip()))

for w in word:
    temp = w[::-1]

    for i in range(len(temp)):
        if temp[i] not in dic:
            dic[temp[i]] = (10 ** (i))
        else:
            dic[temp[i]] += (10 ** (i))

sorted_dic = sorted(dic.items(), key=lambda x: -x[1])

# 알파벳을 적정 숫자로 변환
num_dic = {}
start = 9
for s in sorted_dic:
    alpha, weight = s

    num_dic[alpha] = str(start)
    start -= 1

for i in range(N):
    for j in range(len(word[i])):
        word[i][j] = num_dic[word[i][j]]

result = 0
for w in word:
    changed = ''.join(w)
    result += int(changed)

print(result)

