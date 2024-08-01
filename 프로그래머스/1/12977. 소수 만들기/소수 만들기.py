from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solution(nums):
    answer = 0
    for triple in combinations(nums,3):
        triple_sum = sum(triple)
        if is_prime(triple_sum):
            answer+=1
        

    return answer