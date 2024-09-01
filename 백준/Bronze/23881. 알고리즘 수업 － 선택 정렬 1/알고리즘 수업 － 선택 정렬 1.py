import sys
input = sys.stdin.readline

N, K = list(map(int,input().split()))
lit = list(map(int,input().split()))
count = 0
temp_lit = []
for i in range(N-1,0,-1):
    max_value = max(lit[:(i+1)])
    index = lit.index(max_value)
    if index != i:
        count+=1
        if count == K:
            temp_lit.append(lit[i])
            temp_lit.append(lit[index])
            temp_lit.sort()
            print(" ".join(map(str, temp_lit)))
            sys.exit() 
        lit[i], lit[index] = lit[index], lit[i]
        
print(-1)
    
