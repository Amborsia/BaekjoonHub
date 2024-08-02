from collections import deque
def solution(s):
    count= 0
    lit = deque(s)
    for i in range(len(s)):
        temp = lit.popleft()
        if(temp == '('):
            count +=1
        elif temp == ')':
            if count == 0:
                return False
            count -=1

    if count > 0:
        return False

    return True