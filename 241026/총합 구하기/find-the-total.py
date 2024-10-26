import sys
input = sys.stdin.readline

a,b = list(map(int,input().split()))
count = 0
for i in range(a,b+1):
    if i%6 ==0 and i%8!=0:
        count+=i

print(count)