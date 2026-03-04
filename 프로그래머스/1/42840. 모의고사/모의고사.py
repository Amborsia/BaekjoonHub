def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    num1_limit = len(num1)
    num1_current = 0
    num1_correct = 0
    num2_limit = len(num2)
    num2_current = 0
    num2_correct = 0
    num3_limit = len(num3)
    num3_current = 0
    num3_correct = 0
    for i in range(len(answers)):
        if answers[i] == num1[i%num1_limit]:
            score[0] +=1
        if answers[i] == num2[i%num2_limit]:
            score[1] +=1
        if answers[i] == num3[i%num3_limit]:
            score[2] +=1
    maxs = max(score)
    for i in range(3):
        if score[i] == maxs:
            answer.append(i+1)
    return answer
  
        
    