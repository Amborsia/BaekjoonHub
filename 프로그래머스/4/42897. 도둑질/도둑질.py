def solution(money):
    n = len(money)
    
    # Edge case: if there are only 3 houses, return the max of them because we can't rob adjacent houses
    if n == 3:
        return max(money)
    
    # Function to calculate the max money that can be robbed in a linear arrangement of houses
    def rob_linear(houses):
        n = len(houses)
        if n == 0:
            return 0
        elif n == 1:
            return houses[0]
        
        # Dynamic programming arrays
        dp = [0] * n
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + houses[i])
        
        return dp[-1]
    
    # Scenario 1: Include the first house, exclude the last house
    max_money1 = rob_linear(money[:-1])
    
    # Scenario 2: Exclude the first house, include the last house
    max_money2 = rob_linear(money[1:])
    
    # Return the maximum of both scenarios
    return max(max_money1, max_money2)