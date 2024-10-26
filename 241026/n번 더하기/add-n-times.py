import sys
input = sys.stdin.readline

a,b = list(map(int,input().split()))

for i in range(b):
    a +=b
    print(a)