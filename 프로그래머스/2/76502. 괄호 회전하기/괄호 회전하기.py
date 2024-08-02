def solution(s):
    
    pair = {')':'(', ']':'[','}':'{'}
    extend_s = s*2
    len_s = len(s)
    answer = 0
    for leng in range(len_s):
        stack = []
        rotated = extend_s[leng:leng+len_s]
        
        for char in rotated:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if stack and stack[-1]== pair[char]:
                    stack.pop()
                else:
                    stack.append(char)
                    break
        if not stack:
            answer+=1


    return answer