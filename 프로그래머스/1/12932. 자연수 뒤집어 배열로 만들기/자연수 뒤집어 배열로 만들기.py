def solution(n):
    answer = []
    lit = list(str(n))
    for i in range(len(lit)-1,-1,-1):
        answer.append(int(lit[i]))
    return answer