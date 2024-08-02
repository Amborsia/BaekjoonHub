def solution(n):
    answer = 0
    temp = bin(int(n))[2:]
    temp = temp.count("1")
    count = 0
    temp2 = 0
    while temp!=temp2:
        count +=1
        temp2 = bin(int(n)+count)[2:]
        temp2 = temp2.count("1")

    answer = int(n)+count
    return answer