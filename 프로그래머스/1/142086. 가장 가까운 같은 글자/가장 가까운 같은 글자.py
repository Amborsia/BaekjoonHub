def solution(s):
    answer = []
    temp_lit = list(str(s))
    temp = {}
    count = 0
    for i in temp_lit:
        if i not in temp:
            temp[i] = count
            answer.append(-1)
        else:
            answer.append(abs(temp[i]-count))
            temp[i] = count
        count +=1
    return answer