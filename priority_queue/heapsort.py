import heapq

#힙 정렬
def heapsort(iterable):
    h = [] #힙
    result = []

    #매개변수로 받은 배열의 원소를 차례로 힙에 넣기
    for value in iterable:
        heapq.heappush(h, value)

    #힙 원소 개수만큼 돌면서
    for i in range(len(h)):
        result.append(heapq.heappop(h)) #h(힙)의 원소를 차례로 빼서 result qodufdp ekadkwna

    return result

after_heapsort = heapsort([3,4,64,5,43,221])
print(after_heapsort)