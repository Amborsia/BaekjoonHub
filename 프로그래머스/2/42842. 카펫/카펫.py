def solution(brown, yellow):
    answer = brown + yellow
    for height in range(3, int(answer **0.5)+1):
        if answer % height == 0:
            width = answer // height
            if (width-2) * (height-2) == yellow:
                return [width, height]
    return answer