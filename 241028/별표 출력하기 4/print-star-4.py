import sys
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    for j in range(n-i,0,-1):
        print('*',end=' ')
    print()

for i in range(1,n):
    for j in range(i+1):
        print('*',end = ' ')
    print()