import sys
input = sys.stdin.readline

count = 0
for i in range(5):
    temp = int(input().rstrip())
    if temp%2 == 0:
        count+=1

print(count)