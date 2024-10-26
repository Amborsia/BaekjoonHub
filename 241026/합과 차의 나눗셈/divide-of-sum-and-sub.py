import sys
input = sys.stdin.readline
a,b = list(map(int,input().split()))
print(round((a+b)/(a-b),2))