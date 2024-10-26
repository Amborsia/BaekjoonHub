import sys
input = sys.stdin.readline

a,b,c = list(map(int,input().split()))
hap = a+b+c
avg = (a+b+c)/3
print(hap)
print(int(avg))
print(int(hap-avg))