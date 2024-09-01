import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
lit = deque([])
erase = []
for i in range(1,N+1):
    lit.append(i)

for i in range(N):
    erase.append(lit.popleft())
    
    lit.rotate(-1)

print(" ".join(map(str, erase)))

