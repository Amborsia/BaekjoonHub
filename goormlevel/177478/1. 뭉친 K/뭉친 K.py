import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end, graph, visited):
    queue = deque([(start, end)])
    visited[start][end] = True
    temp = graph[start][end]
    count = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == temp:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1
                
    return count

# 입력 처리
N = int(input().strip())
start, end = map(int, input().split())
lit = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

temp2 = lit[start-1][end-1] 
max_value = 0

for i in range(N):
    for j in range(N):
        if lit[i][j] == temp2 and not visited[i][j]:
            max_value = max(max_value, bfs(i, j, lit, visited))

print(max_value)
