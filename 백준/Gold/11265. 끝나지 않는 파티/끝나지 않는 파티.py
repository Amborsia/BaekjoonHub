import sys
input = sys.stdin.readline

def doid(N,dist):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
        

N, M = map(int, input().split())

dist = []
for i in range(N):
    row = list(map(int, input().split()))
    dist.append(row)

doid(N,dist)

for _ in range(M):
    a,b,c = list(map(int,input().split()))
    a = a-1
    b = b-1

    if dist[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")