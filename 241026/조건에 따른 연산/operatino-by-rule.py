import sys
input =sys.stdin.readline

a = int(input().rstrip())
count = 0
while a<=1000:
    if a %2 == 0:
        a = a*3+1
    else:
        a = a*2+2
    count+=1

print(count)