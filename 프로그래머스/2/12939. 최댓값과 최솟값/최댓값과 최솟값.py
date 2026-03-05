def solution(s):
    answer = ''
    temp = s.split(' ')
    temp = list(map(int, temp))
    minv = min(temp)
    maxv = max(temp)
    answer = str(minv)+" "+str(maxv)
    return answer