from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        HOLDING = 1
        NO_HOLDING = 0
        COOL_DOWN = 2
        size = len(prices)
        
        @cache
        def dp(i, status):
            if i == size:
                return 0
            
            do_nothing = dp(i + 1, status)
                    
            if status == HOLDING:
                do_something = prices[i] + dp(i + 1, COOL_DOWN)
            elif status == COOL_DOWN:
                do_something = dp(i + 1, NO_HOLDING)
            else:
                do_something = -prices[i] + dp(i + 1, HOLDING)
            
            return max(do_nothing, do_something)
        
        return dp(0, NO_HOLDING)
