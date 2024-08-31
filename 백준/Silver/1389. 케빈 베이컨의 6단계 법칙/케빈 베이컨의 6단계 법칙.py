import sys
input = sys.stdin.readline

def doid(n,dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]

def find_user(n,dist):
    min_bacon = float('inf')
    person = -1
    for i in range(n):
        bacon_sum = sum(dist[i])
        if bacon_sum < min_bacon:
            min_bacon = bacon_sum
            person = i
    return person+1


n,m = map(int,input().split())
dist = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    dist[a-1][b-1] = 1
    dist[b-1][a-1] = 1

for i in range(n):
    dist[i][i] = 0

doid(n,dist)



print(find_user(n,dist))




