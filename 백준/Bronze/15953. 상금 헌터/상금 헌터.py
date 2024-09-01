import sys
input = sys.stdin.readline

lit_a = [500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 
         30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]

# 2회 대회의 상금 리스트
lit_b = [512, 256, 256, 128, 128, 128, 128, 
         64, 64, 64, 64, 64, 64, 64, 64, 
         32, 32, 32, 32, 32, 32, 32, 32, 
         32, 32, 32, 32, 32, 32, 32, 32]

N = int(input().strip())

for i in range(N):
    num = 0
    a,b = list(map(int,input().split()))
    if a <=len(lit_a) and a >0:
        num += lit_a[a-1]*10000
    if b <= len(lit_b) and b>0:
        num += lit_b[b-1]*10000
    print(num)
