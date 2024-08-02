def convert(num, base):
    digits = "0123456789ABCDEF"
    if num == 0:
        return "0"
    result = ""
    while num >0:
        result = digits[num%base]+result
        num//=base
        
    return result

def solution(n, t, m, p):
    sequence = ""
    number = 0
    
    while len(sequence)< t*m:
        sequence += convert(number, n)
        number+=1
        
    result = ""
    for i in range(t):
        result += sequence[(i*m)+(p-1)]
    
    return result