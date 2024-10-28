import sys
input = sys.stdin.readline

a = int(input().rstrip())
IsFinish =False
for i in range(2,a):
    if a%i == 0:
        IsFinish = True
        break
if IsFinish:
    print("C")
else:
    print("N")