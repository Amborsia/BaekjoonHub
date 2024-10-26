import sys
input = sys.stdin.readline

a = int(input().rstrip())
lit = []
count = 0
while count<a:
    count+=1
    if count %2 == 0 and count %4 !=0:
        continue
    if (count //8)%2 ==0:
        continue
    if count%7 <4:
        continue

    lit.append(count)

print(*lit)