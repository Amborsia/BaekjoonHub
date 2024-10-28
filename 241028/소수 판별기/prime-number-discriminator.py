import sys
input = sys.stdin.readline

n= int(input().rstrip())
IsPrime = True
for i in range(2,n):
    if n%i == 0:
        IsPrime = False
        break
if IsPrime:
    print("P")
else:
    print("C")