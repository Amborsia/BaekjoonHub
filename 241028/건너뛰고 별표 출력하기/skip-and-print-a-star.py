import sys
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
    print()

for i in range(1,n):
    for j in range(n-i):
        print('*',end = '')
    print()
    print()