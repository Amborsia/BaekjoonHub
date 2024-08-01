def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        if budget - i >=0:
            count+=1
            budget -=i
        else:
            break
            
    return count