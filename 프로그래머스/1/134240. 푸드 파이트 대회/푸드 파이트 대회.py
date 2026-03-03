def solution(food):
    answer = 0
    temp = 0
    for i in range(1,len(food)):
        if food[i]%2 == 1:
            temp += food[i]-1
        else:
            temp+=food[i]
    answer = ["0" for _ in range(temp+1)]
    temp = temp//2
    start,end = 0,len(answer)-1
    for i in range(1,len(food)):
        while food[i] >=2:
            answer[start] = str(i)
            answer[end] = str(i)
            start +=1
            end-=1
            food[i] -=2
            
    return "".join(answer)