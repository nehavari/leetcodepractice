from collections import deque
class Solution:
    DIRECTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[-1]*n for _ in range(m)]
        queue = deque() 
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                    queue.append((row, col))
                    
        while queue:
            row, col = queue.popleft()
            for direction in Solution.DIRECTIONS:
                r = row + direction[0]
                c = col + direction[1]
                if r < 0 or c < 0 or r >= m or c >= n or dist[r][c] != -1:
                    continue
                dist[r][c] = dist[row][col] + 1
                queue.append((r, c))
        return dist
        
        