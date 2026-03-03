def solution(name, yearning, photo):
    answer = []
    for i in photo:
        temp = 0
        for j in name:
            # print(j in i, j, name.index(j), yearning[name.index(j)])
            if j in i:
                temp += yearning[name.index(j)]
        answer.append(temp)
    return answer