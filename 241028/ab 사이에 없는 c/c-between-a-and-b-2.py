import sys
input = sys.stdin.readline

a,b,c = list(map(int,input().split()))
IsFinish = False
for i in range(1,b+1):
    if i%c != 0:
        IsFinish = True
        break

if IsFinish:
    print("YES")
else:
    print("NO")