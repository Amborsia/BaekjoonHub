import sys, math
input = sys.stdin.readline

def check(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			return i
	return n

a,b = map(int,input().split())
if a == b:
	print(check(a))
else:
	print(2)
		