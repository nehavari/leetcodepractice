"""
O(m*n) solution for Walls and Gates in Python using BFS, leetcode has solution but only in Java
"""


from collections import deque
class Solution:
    EMPTY = 2147483647
    DIRECTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]
    GATE = 0
    WALL = -1
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        queue = deque()
        # append all the gates in queue
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == Solution.GATE:
                    queue.append((row, col))
                    
        while queue:
            # queue already has all gates in it
            # first each 1 unit away coordinates will be processed 
            # after that 2 unit away and so one 
            # this way each empty room will have distance to its nearest gate
            row, col = queue.popleft()
            
            # process all 1 unit away coordinates from (row, col) in each of the 4 direction
            for direction in Solution.DIRECTIONS:
                r = row + direction[0]
                c = col + direction[1]
                
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != Solution.EMPTY or rooms[r][c] == Solution.WALL:
                    continue

                rooms[r][c] = rooms[row][col] + 1

                queue.append((r,c))
