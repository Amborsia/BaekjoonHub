import sys
input = sys.stdin.readline
avg = 0
count = 0
while True:
    temp = int(input().rstrip())
    if temp <30:
        count +=1
        avg += temp
    else:
        pit = round(avg/count,2)
        print(f"{pit:.2f}")
        break