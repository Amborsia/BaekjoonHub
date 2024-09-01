import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))


lit = [input().strip() for _ in range(N)]
result = [input().strip() for _ in range(N)]
flag = True
for i in range(len(lit)):
    temp = ''.join([char*2 for char in lit[i]])
    if temp != result[i]:
        flag = False
        break

if flag:
    print("Eyfa")
else:
    print("Not Eyfa")



