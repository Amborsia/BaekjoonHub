# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
target_chars = [0,0,0,0]

for i in range(len(user_input)):
	if user_input[i] == '1':
		target_chars[0] +=1
	elif user_input[i] == 'I':
		target_chars[1] +=1
	elif user_input[i] == 'l':
		target_chars[2] +=1
	elif user_input[i] == '|':
		target_chars[3] +=1
for i in range(len(target_chars)):
	print(target_chars[i])