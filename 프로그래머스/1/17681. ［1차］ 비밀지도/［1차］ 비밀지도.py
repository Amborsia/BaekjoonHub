def solution(n, arr1, arr2):
    answer = []
    # print(bin(2))
    result1 = []
    result2 = []
    result = []
    for i in range(0,n):
        val1 = int(format(arr1[i], f'0{n}b'))
        val2 = int(format(arr2[i], f'0{n}b'))
        result.append(val1 + val2)
    # print(result)
    for i in result:
        s = str(i).zfill(n)
        result1.append(s.replace('0',' ').replace('1','#').replace('2','#')
                      )
    
    return result1