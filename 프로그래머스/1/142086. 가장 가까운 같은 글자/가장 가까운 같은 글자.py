def solution(s):
    answer = []
    dict = {}
    for i in range(0,len(s)):
        if s[i] not in dict:
            answer.append(-1)
        else:
            answer.append(i-dict[s[i]])
        dict[s[i]] = i
    return answer