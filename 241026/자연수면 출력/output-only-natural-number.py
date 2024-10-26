import sys
input = sys.stdin.readline

a,b = list(map(str,input().split()))
if len(a)==1:
    print(a*int(b))
else:
    print(0)