def solution(a, b):
    answer = 0
    maxv, minv = max(a,b),min(a,b)
    
    for i in range(minv,maxv+1):
        answer+=i
    return answer