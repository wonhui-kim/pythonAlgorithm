import sys

S = list(map(int, sys.stdin.readline().rstrip()))

count = [0 for i in range(2)] #0과 1 chunk 개수 세기
for i in range(len(S)):
    if (i == (len(S)-1)) or (S[i] != S[i+1]): #마지막 요소일 경우
        count[S[i]] += 1

#0섹션과 1섹션 중 작은 값이 답
print(min(count))