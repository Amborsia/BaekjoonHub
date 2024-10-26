import sys
input = sys.stdin.readline

a = int(input().rstrip())
count = 0
while True:
    count+=1
    a //=count
    if a <=0:
        break
print(count)