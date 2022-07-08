import math
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        def dfs(nCount, hIndex, lastColor):
            if hIndex >= len(houses):
                return 0 if target == nCount else math.inf
            
            if nCount > target:
                return math.inf
            
            if (nCount, hIndex, lastColor) in dp:
                return dp[(nCount, hIndex, lastColor)]
            
            minCost = math.inf
            if houses[hIndex] != 0:
                dp[(nCount, hIndex, lastColor)] = dfs(
                    nCount + 1 if houses[hIndex] != lastColor else nCount, 
                    hIndex + 1, 
                    houses[hIndex]
                )
                return dp[(nCount, hIndex, lastColor)]
            
            for color in range(1, n+1):
                minCost = min( 
                    minCost,
                    cost[hIndex][color-1] + dfs(
                        nCount + 1 if color != lastColor else nCount,
                        hIndex + 1,
                        color
                    )
                )
                dp[(nCount, hIndex, lastColor)] = minCost
                
            return dp[(nCount, hIndex, lastColor)]
        
        dp = {}
        
        minCost = dfs(0, 0, -1)
        
        return minCost if minCost != math.inf else -1