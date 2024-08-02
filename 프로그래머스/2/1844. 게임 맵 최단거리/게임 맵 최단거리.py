from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS를 위한 큐 초기화
    queue = deque([(0, 0, 1)])  # (x, y, 거리)
    
    # 방문 배열 초기화
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True  # 시작점 방문 처리
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 목적지 도달 시 최단 경로 반환
        if x == n - 1 and y == m - 1:
            return dist
        
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 맵 경계 내에 있고, 방문하지 않았으며, 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    # 목적지에 도달할 수 없는 경우
    return -1
