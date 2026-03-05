def solution(s):
    lit=list()
    
    for i in s:
        if i == "(":
            lit.append(i)
        elif i == ")":
            try:
                lit.pop()
            except:
                return False
    if lit:
        return False
    return True