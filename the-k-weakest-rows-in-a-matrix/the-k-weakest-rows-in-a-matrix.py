import heapq
from collections import defaultdict
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_count_per_row = defaultdict(list)
        for row in range(len(mat)):
            count = 0
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    break
                count += 1
            soldier_count_per_row[count].append(row)
                    
        soldiers_count = list(soldier_count_per_row.keys())
        k_smallest = heapq.nsmallest(k, soldiers_count)
        
        answer = []
        for key in k_smallest:
            answer.extend(soldier_count_per_row[key])
            
        return answer[:k]