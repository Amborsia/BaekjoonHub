import sys
input = sys.stdin.readline

a = int(input().rstrip())
lit = []
for i in range(1,a+1):
    lit.append(i)
print(*lit)