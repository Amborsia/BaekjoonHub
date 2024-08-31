import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
start,end,goal_x, goal_y = list(map(int,input().split()))

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
visited = [[0]*N for _ in range(N)]
def dfs(start,end,goal_x, goal_y):
    queue = deque([(start,end,0)])
    visited[start][end] = True

    while queue:
        x,y,order = queue.popleft()
        if x == goal_x and y == goal_y:
            print(order)
            sys.exit()
        for i in range(6):
            nx = dx[i]+x
            ny = dy[i]+y

            if 0<=nx<N and 0<= ny<N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,order+1))
    print(-1)

dfs(start,end,goal_x,goal_y)

        
