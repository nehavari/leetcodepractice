class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def dp(row, col):
            if row >= m or col >= n:
                return float('inf')
            
            if row == m - 1 and col == n - 1:
                return grid[row][col]
            
            min_sum = grid[row][col] + min(
                dp(row + 1, col),
                dp(row, col + 1)
            )
            
            return min_sum
        
        return dp(0, 0)
