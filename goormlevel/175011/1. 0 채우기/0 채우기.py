# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
x,y = 0,0
for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if matrix[i][j] == 0:
			x = i
			y = j
			break
			
sums = 0
for i in range(len(matrix[x])):
	sums +=matrix[x][i]
for i in range(len(matrix)):
	sums+= matrix[i][y]
	
print(sums)
