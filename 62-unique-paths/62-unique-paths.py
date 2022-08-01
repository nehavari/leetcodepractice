class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
#         @cache
#         def dp(i, j):
#             if i >= m or j >= n:
#                 return 0
            
#             if i == m - 1 and j == n - 1:
#                 return 1
            
#             return dp(i + 1, j) + dp(i, j + 1)
        
#         return dp(0, 0)

        dp = [[1] * (n) for _ in range(m)]
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
                
        return dp[0][0]
