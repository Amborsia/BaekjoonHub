def solution(numbers):
    temp = list(set(numbers))
    answer = 0
    for i in range(1,10):
        if i not in temp:
            answer+=i
    return answer