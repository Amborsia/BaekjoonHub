import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    queue = deque([(start,1)])

    while queue:
        num, count = queue.popleft()

        if num> maxs:
            print(-1)
            sys.exit()
        elif num == maxs:
            print(count)
            sys.exit()

        next_value = num*2
        if next_value <= maxs:
            queue.append((next_value,count+1))
        
        next_value = int(str(num)+"1")
        if next_value <= maxs:
            queue.append((next_value,count+1))
    print(-1)
    return

start, maxs = list(map(int, input().split()))
bfs(start)