def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    count = 0
    temp = score[count:count+m]
    while(len(temp)>= m):
        if len(temp)<= m:
            answer += min(temp)*m
        count += m
        temp = score[count:count+m]
        
    return answer