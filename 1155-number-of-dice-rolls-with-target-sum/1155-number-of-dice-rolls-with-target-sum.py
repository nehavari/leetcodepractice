class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        
        def dp(index, curr_sum):
            if index == n:
                return curr_sum == target
            
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            ways = 0
            for num in range(1, min(k + 1, target - curr_sum + 1)):
                ways += dp(index + 1, curr_sum + num)
            
            memo[(index, curr_sum)] = ways % (10 ** 9 + 7)
            
            return memo[(index, curr_sum)]
        
        return dp(0, 0)
        