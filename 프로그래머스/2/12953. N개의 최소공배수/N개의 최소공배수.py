import math
def solution(arr):
    result = arr[0]
    for num in arr[1:]:
        result = abs(result * num)// math.gcd(result,num)
    return result