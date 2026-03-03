def solution(s, n):
    answer = ''
    for i in range(0,len(s)):
        temp = ord(s[i])
        if 65<=temp<=90:
            temp+=n
            if temp >90:
                temp -= 26
        elif 97<=temp<=122:
            temp+=n
            if temp >122:
                temp -= 26
        answer += chr(temp)
        # print(chr(ord(s[i])+1))
    return answer