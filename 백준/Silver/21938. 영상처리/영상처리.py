import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, visited, binary_image):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < len(binary_image) and 0 <= ny < len(binary_image[0]):
                if not visited[nx][ny] and binary_image[nx][ny] == 255:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def solve(N, M, T, matrix):
    # 이진화된 이미지 만들기
    binary_image = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            r, g, b = matrix[i][j*3], matrix[i][j*3+1], matrix[i][j*3+2]
            avg_value = (r + g + b) // 3
            if avg_value >= T:
                binary_image[i][j] = 255
    
    visited = [[False] * M for _ in range(N)]
    count = 0
    
    for i in range(N):
        for j in range(M):
            if binary_image[i][j] == 255 and not visited[i][j]:
                bfs(i, j, visited, binary_image)
                count += 1
                
    print(count)

# 입력 처리
N, M = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for _ in range(N)]
T = int(input().rstrip())
solve(N, M, T, matrix)
