def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)):
        if len(temp) == k and score[i]>temp[0]:
            temp.pop(0)
            
        if len(temp) != k:
            temp.append(score[i])
            temp.sort()
        answer.append(temp[0])
        
    
    return answer