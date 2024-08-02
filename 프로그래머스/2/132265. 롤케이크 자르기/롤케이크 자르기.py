from collections import Counter
def solution(topping):
    right_counter = Counter(topping)   
    left_counter = Counter()
    
    left_unique = 0
    right_unique = len(right_counter)
    
    count = 0
    
    for t in topping:
        right_counter[t] -=1
        if right_counter[t] == 0:
            right_unique -=1
        if left_counter[t] == 0:
            left_unique +=1
        left_counter[t] +=1
        
        if left_unique == right_unique:
            count+=1
            
    return count