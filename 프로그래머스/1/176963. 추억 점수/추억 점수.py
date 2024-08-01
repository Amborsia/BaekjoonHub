def solution(name, yearning, photo):
    answer = [0]*len(photo)
    temp_dict = {}
    for i in range(len(name)):
        temp_dict[name[i]] = yearning[i]
        
    for i in range(len(photo)):
        for j in photo[i]:
            if(j in temp_dict):
                answer[i]+= temp_dict[j]
    return answer