def solution(phone_number):
    answer = ''
    temp = list(str(phone_number))
    for i in range(0,len(phone_number)-4):
        temp[i] = '*'
    return str(''.join(temp))