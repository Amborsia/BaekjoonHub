import sys
input = sys.stdin.readline

a = int(input().rstrip())

for i in range(a):
    for j in range(a):
        print('*',end='')
    print()