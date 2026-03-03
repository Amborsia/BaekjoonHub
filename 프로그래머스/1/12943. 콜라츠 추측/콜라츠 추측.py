def solution(num):
    answer = 0
    idx = 0
    while num != 1:
        idx+=1
        if idx >=500:
            return -1
        if num %2 == 0:
            num= num/2;
        elif num %2 == 1:
            num = num*3+1
        
    return idx