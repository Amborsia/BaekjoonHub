def solution(nums):
    answer = 0
    leng = len(nums)//2
    num_lit = list(set(nums))
    if leng >= len(num_lit):
        return len(num_lit)
    else:
        return leng