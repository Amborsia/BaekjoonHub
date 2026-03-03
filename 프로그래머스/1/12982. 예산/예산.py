def solution(d, budget):
    answer = 0
    temp = sorted(d)
    print(temp)
    for i in range(0,len(temp)):
        if budget-temp[i] >=0:
            answer+=1
            budget-=temp[i]
        else:
            break;
    return answer