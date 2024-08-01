def solution(arr):
    answer = []
    temp = arr.pop(0);
    answer.append(temp)
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    return answer