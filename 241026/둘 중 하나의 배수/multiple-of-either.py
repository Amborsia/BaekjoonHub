import sys
input = sys.stdin.readline

a = int(input().rstrip())

if a %3 == 0 or a %5 == 0:
    print(1)
else:
    print(0)