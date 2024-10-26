import sys
input = sys.stdin.readline

a,b = list(map(int,input().split()))
count = 1
for i in range(1,b+1):
    if i%a == 0:
        count *=i
print(count)