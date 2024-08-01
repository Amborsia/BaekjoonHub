import math

def min_four_squares(n):
    # n이 0이면 0을 반환
    if n == 0:
        return 0

    # n이 완전 제곱수인지 체크
    if int(math.isqrt(n))**2 == n:
        return 1

    # 두 제곱수의 합으로 표현 가능한지 체크
    for i in range(1, int(math.isqrt(n)) + 1):
        if int(math.isqrt(n - i*i))**2 == n - i*i:
            return 2

    # 세 제곱수의 합으로 표현 가능한지 체크 (4는 남는 경우)
    for i in range(1, int(math.isqrt(n)) + 1):
        for j in range(1, int(math.isqrt(n - i*i)) + 1):
            if int(math.isqrt(n - i*i - j*j))**2 == n - i*i - j*j:
                return 3

    # 최대 4개의 제곱수로 표현
    return 4


n = int(input())
print(min_four_squares(n))
