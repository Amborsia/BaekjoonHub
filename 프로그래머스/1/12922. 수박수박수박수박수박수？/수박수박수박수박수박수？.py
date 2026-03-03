def solution(n):
    answer = ''
    idx = 0
    while n !=0:
        if idx%2==0:
            answer+="수"
        else:
            answer+="박"
        n-=1
        idx+=1
    return answer