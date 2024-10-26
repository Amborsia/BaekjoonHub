import sys
input = sys.stdin.readline

a = int(input().rstrip())
count = 0
for i in range(1, a+1):
    a //= i
    count += 1
    if a <= 1:
        break
print(count)