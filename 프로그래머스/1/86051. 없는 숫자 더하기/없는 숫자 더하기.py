def solution(numbers):
    num = list(str(numbers))
    num_set = set(num)
    answer = 0
    for i in range(0,10):
        if str(i) not in num_set:
            answer += i
    return answer