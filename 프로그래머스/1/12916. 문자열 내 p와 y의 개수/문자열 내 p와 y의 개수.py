def solution(s):
    temp = s.replace('P','p').replace('Y','y')
    print(temp.count('p'))
    if temp.count('p') == temp.count('y'):
        return True

    return False