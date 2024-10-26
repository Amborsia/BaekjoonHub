import sys
input = sys.stdin.readline

a,b = list(map(str,input().split()))
if a == '0':
    print(0)
elif len(a)==1:
    print(a*int(b))
else:
    print(0)