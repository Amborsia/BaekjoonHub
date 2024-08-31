import sys
input = sys.stdin.readline

def doid(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
def index(c):
    return ord(c) - ord('a')

n = int(input().rstrip())
reach = [[False] * 26 for _ in range(26)]

for _ in range(n):
    a, _, b = input().strip().split()
    reach[index(a)][index(b)] = True

doid(26,reach)

m = int(input().strip())
for _ in range(m):
    a, _, b = input().strip().split()
    if reach[index(a)][index(b)]:
        print("T")
    else:
        print("F")

    