def solution(n):
    answer = ''
    if n == 0:
        return ""
    elif n == 1:
        return "수"
    else:
        if(n %2 == 0):
            return "수박"*(n//2)
        else:
            return "수박"*(n//2)+"수"
    