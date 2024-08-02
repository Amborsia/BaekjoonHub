from itertools import permutations
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True
def solution(numbers):
    unique = set()
    
    for length in range(1, len(numbers)+1):
        for perm in permutations(numbers, length):
            num = int(''.join(perm))
            if is_prime(num):
                unique.add(num)
    return len(unique)