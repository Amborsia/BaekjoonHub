def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer+=str(i)*int(food[i]//2)

    temp = list(answer)
    temp.reverse()
    answer+='0'
    for i in temp:
        answer+=str(i)
    
        
    return answer