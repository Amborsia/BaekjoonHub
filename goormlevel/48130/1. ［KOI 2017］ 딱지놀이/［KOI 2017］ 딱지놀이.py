import sys
input = sys.stdin.readline

count = int(input().strip())

for i in range(count):
	person_a = [0,0,0,0]
	person_b = [0,0,0,0]
	flag = -1
	lit_a = list(map(int,input().split()))
	lit_b = list(map(int,input().split()))
	for j in range(1,len(lit_a)):
		person_a[lit_a[j]-1] +=1
	for j in range(1,len(lit_b)):
		person_b[lit_b[j]-1] +=1
	
	for j in range(3,-1,-1):
		if person_a[j] != person_b[j]:
			if person_a[j] > person_b[j]:
				flag = 1
				break
			else:
				flag = 0
				break
	if flag == 1:
		print("A")
	elif flag == 0:
		print("B")
	else:
		print("D")
				
print()
	
		