def solution(nums):
    pos = len(nums)//2 #가져갈 수 있는 폰켓몬 수

    dict = {}  # 빈 딕셔너리 생성
    #[3,1,2,3] -> {3:2, 1:1, 2:1}
    for i in nums:
        if i not in dict: #딕셔너리에 키가 없으면
            dict[i] = 1
        else:
            dict[i] += 1 #키가 있으면 더해주기

    if len(dict) < pos:
        return len(dict)
    else:
        return pos

print(solution([3,1,2,3])) #2
print(solution([3,3,3,2,2,4])) #2
print(solution([3,3,3,2,2,2])) #2