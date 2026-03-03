def solution(arr):
    answer = []
    if len(arr) == 0:
        return []
    else:
        answer.append(arr[0])
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    
    return answer