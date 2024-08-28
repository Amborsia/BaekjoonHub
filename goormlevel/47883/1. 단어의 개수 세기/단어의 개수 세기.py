# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 입력 받기
input_string = input().strip()  # 입력받은 문자열의 앞뒤 공백 제거

# 단어를 공백 기준으로 분리
words = input_string.split()

# 단어 개수 세기
word_count = len(words)

# 결과 출력
print(word_count)
