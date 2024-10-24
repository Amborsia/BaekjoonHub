import sys
input = sys.stdin.readline

a = list(map(str,input().split('-')))
temp = a[1]
a[1] = a[2]
a[2] = temp
print('-'.join(a))