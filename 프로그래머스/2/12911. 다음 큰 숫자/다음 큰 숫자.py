def solution(n):
    comp = n+1
    while True:
        if format(n,'b').count('1') == format(comp,'b').count('1'):
                return comp
        else:
            comp+=1    