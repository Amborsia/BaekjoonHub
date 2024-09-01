import sys
input = sys.stdin.readline

timer_a = 300
timer_b = 60
timer_c = 10
N = int(input().rstrip())
lit = [0,0,0]
while True:
    if N>= timer_a:
        N-=timer_a
        lit[0]+=1
    elif N>= timer_b:
        N-=timer_b
        lit[1]+=1
    elif N>=timer_c:
        N-=timer_c
        lit[2]+=1
    elif N==0:
        print(" ".join(map(str,lit)))
        break
    else:
        print(-1)
        break


