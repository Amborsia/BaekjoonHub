import sys
input = sys.stdin.readline

a = int(input().rstrip())

for i in range(a):
    temp = int(input().rstrip())
    if temp %2 == 1 and temp %3 == 0:
        print(temp)