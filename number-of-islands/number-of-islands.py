"""
a very simple solution to number of Islands using BFS
time complexity = O(m*n)
space complexity = O(min(m, n))
"""

from collections import deque

class Solution:
    
    DIRECTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]
    
    def markIsland(self, grid, row, col):
        queue = deque()
        queue.append((row, col))
        m = len(grid)
        n = len(grid[0])
        
        while queue:
            row, col = queue.popleft()
            for direction in Solution.DIRECTIONS:
                r = row + direction[0]
                c = col + direction[1]
                
                if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != '1':
                    continue
                
                grid[r][c] = '2'
                queue.append((r, c))
                
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        m = len(grid)
        n = len(grid[0])
        
        for row in range(m):
            for col in range(n):
                
                if grid[row][col] == '1':
                    num += 1
                    grid[row][col] = '2'
                    self.markIsland(grid, row, col)
    
        return num