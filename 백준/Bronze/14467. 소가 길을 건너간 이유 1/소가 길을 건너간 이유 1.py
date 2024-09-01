import sys
input = sys.stdin.readline

N = int(input().strip())

dict = {}
count = 0
for i in range(N):
    key,value = list(map(int, input().split()))
    if key in dict and dict[key] != value:
        dict[key] = value
        count+=1
    elif key not in dict:
        dict[key] = value
print(count)
        