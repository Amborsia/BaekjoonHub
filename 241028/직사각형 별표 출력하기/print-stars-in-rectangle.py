import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))

for i in range(n):
    for j in range(m):
        print('*',end = ' ')
    print()