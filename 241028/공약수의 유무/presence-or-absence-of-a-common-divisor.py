import sys
input = sys.stdin.readline
a,b = list(map(int,input().split()))
IsFinish = False
for i in range(a,b+1):
    if 1920%i == 0 and 2880%i == 0:
        IsFinish= True
        break

if IsFinish:
    print(1)
else:
    print(0)