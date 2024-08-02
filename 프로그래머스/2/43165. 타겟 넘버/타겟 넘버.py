def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        count_plus = dfs(index+1, current_sum+numbers[index])
        count_minus = dfs(index+1,current_sum-numbers[index])
        return count_plus+count_minus
    
    return dfs(0,0)
    