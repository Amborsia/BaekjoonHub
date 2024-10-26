import sys
input = sys.stdin.readline

a,b = list(map(int,input().split()))
lit = []
while a>=b:
    if a%2 ==0:
        lit.append(a)
    a-=1
print(*lit)