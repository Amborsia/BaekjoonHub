import sys
input= sys.stdin.readline

a = int(input().rstrip())

if a %3 == 0:
    print("YES")
else:
    print("NO")

if a %5 == 0:
    print("YES")
else:
    print("NO")