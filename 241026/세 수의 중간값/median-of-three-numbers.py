import sys
input = sys.stdin.readline

a,b,c = list(map(int,input().split()))

if b>a and b<c:
    print(1)
else:
    print(0)