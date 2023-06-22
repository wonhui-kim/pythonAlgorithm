import sys

n = int(sys.stdin.readline()) #주어진 배열 원소 수
arr_set = set(list(map(int, sys.stdin.readline().split()))) #set으로 만들어 검색 속도 O(1)

m = int(sys.stdin.readline()) #찾으려는 원소 수
numbers = list(map(int, sys.stdin.readline().split()))
for n in numbers:
    if n in arr_set:
        print(1)
    else:
        print(0)