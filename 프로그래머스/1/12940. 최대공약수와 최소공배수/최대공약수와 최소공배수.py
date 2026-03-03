import math
def solution(n, m):
    answer = []
    a,b = n,m
    while b>0:
        a,b = b, a%b
    val = a
    
    lcm = (n*m)//val
    return [val, lcm]