def solution(number, limit, power):
    divisors_count = [0] * (number + 1)
    answer = 0
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors_count[j] += 1

    for i in divisors_count:
        if i<=limit:
            answer+= i
        else:
            answer+=power
    return answer