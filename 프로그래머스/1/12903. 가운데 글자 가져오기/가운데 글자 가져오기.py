def solution(s):
    answer = ''
    leng = len(s)
    if leng %2 == 1:
        leng = int((leng+1)/2)
        return s[leng-1:leng]
    else:
        leng = int(leng/2)
        return s[leng-1:leng+1]
    
    return leng