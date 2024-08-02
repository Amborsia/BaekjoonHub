def solution(n):
    count = 0
    
    for start in range(1, n + 1):
        sum_value = 0
        current = start
        
        while sum_value < n:
            sum_value += current
            current += 1
        
        if sum_value == n:
            count += 1
    
    return count