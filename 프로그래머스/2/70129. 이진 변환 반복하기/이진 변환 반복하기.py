def solution(s):
    convert_count = 0
    zero_count = 0
    while s!= "1":
        num_zeros = s.count('0')
        zero_count += num_zeros
        
        s = s.replace('0','')
        s=bin(len(s))[2:]
        convert_count +=1
    return [convert_count, zero_count]
