import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_x,start_y,visited, graph, N):
	queue = deque([(start_x, start_y)])	
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	visited[start_x][start_y] = True
	while queue:
		x,y = queue.popleft()
		for i in range(4):
			nx = dx[i]+x
			ny = dy[i]+y
			if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] == 1:
				visited[nx][ny] = True
				queue.append((nx,ny))

N = int(input().strip())

lit = [list(map(int,input().split())) for _ in range(N)]


visited = [[False]*N for _ in range(N)]
count = 0
for i in range(N):
	for j in range(N):
		if not visited[i][j] and lit[i][j] == 1:
			bfs(i,j,visited,lit, N)
			count+=1
			
print(count)
