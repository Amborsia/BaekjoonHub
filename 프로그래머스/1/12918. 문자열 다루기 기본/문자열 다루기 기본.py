def solution(s):
    try:
        if len(s) == 4 or len(s) == 6:
            temp = int(s)
        else:
            return False
    except:
        return False
    
    return True