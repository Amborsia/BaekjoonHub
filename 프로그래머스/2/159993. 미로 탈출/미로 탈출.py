from collections import deque

def bfs(start,end,maps):
    n,m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque([(start[0],start[1],0)])
    visited[start[0]][start[1]] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x,y,dist = queue.popleft()
        if (x, y) == end:
            return dist
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx,ny,dist+1))
    return -1
            


def solution(maps):
    start = end = lever = None
    n = len(maps)
    m = len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i,j)
            elif maps[i][j] == 'E':
                end = (i,j)
            elif maps[i][j] == 'L':
                lever= (i,j)
    
    dist_lever = bfs(start, lever, maps)
    if dist_lever == -1:
        return -1
    
    dist_goal = bfs(lever, end, maps)
    if dist_goal == -1:
        return -1
    
    
    return dist_lever + dist_goal