def solution(k, score):
    answer = []
    ranking = []
    for i in score:
        if len(ranking) < k:
            ranking.append(i)
        else:
            minv = min(ranking)
            # 10,20,100 일때 150이 들ㅇ오면 10 삭제해야함
            if minv <= i:
                temp = ranking.index(minv)
                ranking[temp]= i
        # print(ranking)
        answer.append(min(ranking))
            
    return answer