import sys
input = sys.stdin.readline
a,b = list(map(int,input().split()))
temp = (a+b)/(a-b)
print(f"{temp:.2f}")