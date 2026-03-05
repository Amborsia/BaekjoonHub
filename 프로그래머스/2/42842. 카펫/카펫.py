def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for i in range(3, int(total**0.5)+1):
        if total % i == 0:
            w = total//i
            if (w-2) * (i-2) == yellow:
                return [w, i]

