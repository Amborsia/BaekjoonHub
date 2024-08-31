import sys
input = sys.stdin.readline

def doid(N, graph):
    dist = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                dist[i][j] = 1
            elif i == j:
                dist[i][j] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] == 0 and dist[i][k] ==1 and dist[k][j] == 1:
                    dist[i][j] =1

    return dist


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = doid(N,graph)

for i in result:
    print(" ".join(map(str, i)))

