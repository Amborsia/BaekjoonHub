def solution(s):
    open = 0
    for i in range(0,len(s)):
        if s[i] == "(":
            open+=1
        elif s[i] == ")":
            if open >=1:
                open-=1
            else:
                return False
    if open >=1:
        return False
    return True