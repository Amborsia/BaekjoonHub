import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int,input().split()))

matrix = [list(map(int,input().split())) for _ in range(M)]

visited = [[False]*N for _ in range(M)]
visited[0][0] = True
queue = deque([(0,0)])
dx = [0,1]
dy = [1,0]
while queue:
    
    x,y = queue.popleft()
    if x == M-1 and y == N-1:
            print("Yes") 
            sys.exit()
    for i in range(2):
        nx = dx[i]+x
        ny = dy[i]+y

        if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and matrix[nx][ny] == 1:
            visited[nx][ny] = True
            queue.append((nx,ny))
print("No")
        




