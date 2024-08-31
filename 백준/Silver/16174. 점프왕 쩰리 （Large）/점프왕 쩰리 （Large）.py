import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())

matrix = [list(map(int,input().split())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
dx = [1,0]
dy = [0,1]

queue = deque([(0,0)])

while queue:
    x,y = queue.popleft()
    temp = matrix[x][y]
    if matrix[x][y] == -1:
        print("HaruHaru")
        sys.exit()
    for i in range(2):
        nx = (dx[i]*temp)+x
        ny = (dy[i]*temp)+y

        if 0<=nx <N and 0<=ny<N and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx,ny))
print("Hing")
        