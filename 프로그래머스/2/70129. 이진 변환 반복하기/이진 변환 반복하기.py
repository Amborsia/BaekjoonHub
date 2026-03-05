def solution(s):
    count_v = 0
    remove = 0
    while s != "1":
        remove += s.count('0')
        new_len = len(s) - s.count('0')
        s = bin(new_len)[2:]
        count_v +=1
    return [count_v, remove]