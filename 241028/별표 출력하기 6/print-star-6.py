import sys
input = sys.stdin.readline

n = int(input().rstrip())


for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end= ' ')
    for j in range(i*2-1):
        print('*',end=' ')
    print()

for i in range(1,n):
    for j in range(n-i-1):
            print(' ',end= ' ')
    for j in range(i*2+1):
        print('*',end=' ')
    print()