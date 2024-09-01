import sys
input = sys.stdin.readline

N = int(input())
count = 1
total = 0

while total + count <= N:
    total += count
    count += 1


if N-total >=0:
    if count %2 == 0:
        print(0)
    else:
        print((count)-(N-total))

