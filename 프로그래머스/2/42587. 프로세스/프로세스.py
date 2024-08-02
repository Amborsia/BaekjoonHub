from collections import deque

def solution(priorities, location):
    queue = deque ([(priority, index) for index,priority in enumerate(priorities)])
    order = 0

    while queue:
        current = queue.popleft()
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            order+=1
            if current[1] == location:
                return order
