import math
def solution(n):
    answer = 0
    temp = math.sqrt(n)
    if(temp.is_integer()):
        return (math.sqrt(n)+1)**2
    else:
        return -1
    