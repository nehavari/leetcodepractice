from functools import cache
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        
        @cache
        def dp(index, aCity, bCity):
            if index == len(costs):
                if aCity == n and bCity == n:
                    return 0
                return float('inf')
            
            a_cost = costs[index][0] + dp(index + 1, aCity + 1, bCity)
            b_cost = costs[index][1] + dp(index + 1, aCity, bCity + 1)
                    
            return min(a_cost, b_cost)
        
        return dp(0, 0, 0)