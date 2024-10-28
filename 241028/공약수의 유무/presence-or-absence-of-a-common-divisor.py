import sys
input = sys.stdin.readline

IsFinish = False
a,b = list(map(int,input().split()))
for i in range(1,a):
    if a%i == 0 and b %i == 0:
        print(1)
        IsFinish = True
        break
if IsFinish == False:
    print(0)