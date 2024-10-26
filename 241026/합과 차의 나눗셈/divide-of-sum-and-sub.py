import sys
input = sys.stdin.readline
a,b = list(map(float,input().split()))
print(round((a+b)/(a-b),2))