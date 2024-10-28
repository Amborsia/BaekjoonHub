import sys
input = sys.stdin.readline

n = int(input().rstrip())

for k in range(2):
    for i in range(n):
        for j in range(n):
            print('*',end='')
        print()
    print()