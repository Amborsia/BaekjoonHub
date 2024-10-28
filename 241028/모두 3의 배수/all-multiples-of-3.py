import sys
input = sys.stdin.readline

IsThree = True
for i in range(5):
    temp = int(input().rstrip())
    if temp % 3 != 0:
        IsThree = False
        break
if IsThree:
    print(1)
else:
    print(0)