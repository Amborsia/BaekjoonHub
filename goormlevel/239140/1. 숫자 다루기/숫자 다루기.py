import sys
input = sys.stdin.readline

# 숫자를 문자열로 입력받고, 그대로 정수로 변환
N = int(input().strip())

# 입력받은 숫자를 역순으로 출력
print(str(N)[::-1])

# 자릿수의 합을 구해서 출력
digit_sum = sum(map(int, str(N)))
print(digit_sum)

# 입력받은 숫자에 100을 더해서 출력
print(N + 100)
