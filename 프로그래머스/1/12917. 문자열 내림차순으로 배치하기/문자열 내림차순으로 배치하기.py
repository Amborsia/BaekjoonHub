def solution(s):
    temp = sorted(s, reverse = True)
    return ''.join(temp)