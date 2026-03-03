import heapq
def solution(k, score):
    answer = []
    temp = []
    for i in score:
        heapq.heappush(temp,i)
        
        if len(temp) >k:
            heapq.heappop(temp)
        answer.append(temp[0])
        
    return answer