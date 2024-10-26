import sys
input = sys.stdin.readline

b,a = list(map(int,input().split()))
lit = []
for i in range(b,a-1,-1):
    if i%2==1:
        lit.append(i)
print(*lit)