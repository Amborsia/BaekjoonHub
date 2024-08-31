from collections import deque
def solution(maps):
    visited = [[False] *len(maps[0]) for _ in range(len(maps))]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    while queue:
        x,y,dist = queue.popleft()
        
        if x == len(maps)-1 and y == len(maps[0]) -1:
            return dist
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0 <= nx < len(maps) and 0<= ny <len(maps[0]) and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny,dist+1))
    return -1