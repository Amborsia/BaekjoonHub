import sys
input = sys.stdin.readline

a = int(input().rstrip())
count = 0

while a > 0:
    count += 1  
    a //= count 
    

print(count)