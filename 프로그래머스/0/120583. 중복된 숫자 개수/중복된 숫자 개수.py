def solution(array, n):
    count = 0
    for i in range(len(array)):
        if array[i] == n:
            print(array[i])
            count+=1
    return count