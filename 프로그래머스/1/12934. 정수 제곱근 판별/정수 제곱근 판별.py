def solution(n):
    answer = -1
    value = n**0.5
    if value % 1 == 0:
        return (value+1)**2
    return answer