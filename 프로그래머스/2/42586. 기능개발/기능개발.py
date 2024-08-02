import math
def solution(progresses, speeds):
    remaining_days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    # 결과 리스트
    result = []
    current = remaining_days[0]
    count = 0
    for days in remaining_days:
        if days <= current:
            count+=1
        else:
            result.append(count)
            current = days
            count = 1
    result.append(count)
    return result