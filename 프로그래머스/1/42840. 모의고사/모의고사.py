def solution(answers):
    temp1 = [1,2,3,4,5]
    temp2 = [2,1,2,3,2,4,2,5]
    temp3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    
    # 정답을 하나씩 체크
    for i, answer in enumerate(answers):
        if answer == temp1[i % len(temp1)]:
            scores[0] += 1
        if answer == temp2[i % len(temp2)]:
            scores[1] += 1
        if answer == temp3[i % len(temp3)]:
            scores[2] += 1
    max_score = max(scores)
    result = []
    for i, score in enumerate(scores):
        if(score == max_score):
            result.append(i+1)
    return result