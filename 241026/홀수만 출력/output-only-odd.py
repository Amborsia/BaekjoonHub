import sys
input = sys.stdin.readline

a,b = list(map(int, input().split()))
lit=[]
for i in range(a,b+1):
    if i%2 == 1:
        lit.append(i)

print(*lit)