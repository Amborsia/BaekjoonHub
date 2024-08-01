def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line1 = bin(arr1[i])[2:].zfill(n)
        line2 = bin(arr2[i])[2:].zfill(n)
        line =''
        for j in range(n):
            if(line1[j] == '1' or line2[j] == '1'):
                line+='#'
            else:
                line+=' '
        answer.append(line)
    return answer