import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_to_soldiers = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                row_to_soldiers[row] = row_to_soldiers.get(row, 0) + mat[row][col]
                
        soldiers_count = list(row_to_soldiers.values())
        k_smallest = heapq.nsmallest(k, soldiers_count)
        
        answer = []
        for key, value in row_to_soldiers.items():
            if value in k_smallest:
                answer.append((key, value))
        answer.sort(key=lambda num: (num[1], num[0]))
        
        return [num[0] for num in answer[:k]]