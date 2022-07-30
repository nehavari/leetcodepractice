from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        HOLDING = 1
        NO_HOLDING = 0
        COOL_DOWN = 2
        size = len(prices)
        
        dp = [[0] * 3 for _ in range(size + 1)]
        
        for i in range(size - 1, -1, -1):
            for status in (HOLDING, NO_HOLDING, COOL_DOWN):
                do_nothing = dp[i + 1][status]
                if status == HOLDING:
                    do_something = prices[i] + dp[i+1][COOL_DOWN]
                elif status == COOL_DOWN:
                    do_something = dp[i+1][NO_HOLDING]
                else:
                    do_something = -prices[i] + dp[i + 1][HOLDING]
                    
                dp[i][status] = max(do_nothing, do_something)
                
        return dp[0][NO_HOLDING]