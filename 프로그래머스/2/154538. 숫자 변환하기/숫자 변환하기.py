from collections import deque
def solution(x, y, n):
    
    queue = deque([(x,0)])
    visited = set()
    visited.add(x)
    
    while queue :
        current, count = queue.popleft()
        
        if current == y:
            return count
        
        next_value = [current+n, current*2, current*3]
        for next_val in next_value:
            if next_val <= y and next_val not in visited:
                queue.append((next_val, count+1))
            visited.add(next_val)
    return -1