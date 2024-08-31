import sys
from collections import deque
input = sys.stdin.readline


answer = []

    



def bfs(x,y,graph,visited):
    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [-1,-1,-1,0,0,1,1,1]
    queue = deque([(x,y)])
   
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<len(graph) and 0<=ny<len(graph[0]) and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))

def solve(x,y,graph):
    visited = [[False]*len(graph[0]) for _ in range(len(graph))]
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs(i,j,graph,visited)
                count +=1
    return count

while True:
    N,M = list(map(int,input().split()))
    
    if N == 0 and M == 0:
        for i in range(len(answer)):
            print(answer[i])
        break
    # if N <=1 and M <=1:
    #     print(input())
    #     continue
    matrix = [list(map(int,input().split())) for _ in range(M)]

    answer.append(solve(0,0,matrix))
