import sys
input = sys.stdin.readline

N = int(input().strip())
for i in range(N):
    m,n = map(int,input().split())
    lit = [list(map(int, input().split())) for _ in range(m)]
    count = 0
    for j in range(m-2,-1,-1):
        for k in range(n):
            if lit[j][k] == 1:
                temp = j
                while temp <m-1:
                    temp +=1
                    if lit[temp][k] == 0:
                        count+=1
    print(count)


