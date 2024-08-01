def solution(nums):
    answer = 0
    temp = set(nums)
    count = len(nums)//2
    if(len(temp) < count):
        return len(temp)
    else:
        return count