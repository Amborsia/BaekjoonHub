# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
count = 0
for i in range(1,user_input+1):
	count = count+ 3**i
print ( count)