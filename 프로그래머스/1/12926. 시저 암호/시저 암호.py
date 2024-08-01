def solution(s, n):
    set_lit = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    set_big_lit = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer = ''
    temp_lit = list(str(s))
    for i in temp_lit:
        temp = 0
        if(i.isupper()):
            temp = set_big_lit.index(i)
            answer += set_big_lit[(temp+n)%26]
            
        elif(i.islower()):
            temp = set_lit.index(i)
            answer += set_lit[(temp+n)%26]
        else:
            answer += ' '
    return answer