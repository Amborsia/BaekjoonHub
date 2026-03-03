def solution(s):
    answer = ''
    idx = 0
    is_word = 0
    leng = len(s)
    while idx!=leng:
        if s[idx] == ' ':
            is_word = 0
            idx+=1
            answer+=' '
            continue
        elif is_word%2 == 0:
            answer += s[idx].upper()
        elif is_word%2 == 1:
            answer+= s[idx].lower()
        idx+=1
        is_word+=1
        
    return answer