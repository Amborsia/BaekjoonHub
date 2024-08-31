import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_x, start_y, visited, graph):
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = 0  # 시작점은 거리가 0
    
    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))

def solve(matrix):
    visited = [[-1] * M for _ in range(N)]

    # 목표지점(2) 찾기
    start_x, start_y = -1, -1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                start_x, start_y = i, j
                break
        if start_x != -1:
            break

    bfs(start_x, start_y, visited, matrix)

    # 출력
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                print(0, end=' ')
            else:
                print(visited[i][j], end=' ')
        print()

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
solve(matrix)
