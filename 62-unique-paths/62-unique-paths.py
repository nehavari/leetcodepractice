from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dp(i, j):
            if i >= m or j >= n:
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            
            return dp(i + 1, j) + dp(i, j + 1)
        
        return dp(0, 0)