import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_min_heap = []
        self.k = k
        for num in nums:
            if len(self.k_min_heap) == k:
                if num > self.k_min_heap[0]:
                    heapq.heappop(self.k_min_heap)
                    heapq.heappush(self.k_min_heap, num)
            else:
                heapq.heappush(self.k_min_heap, num)
        

    def add(self, val: int) -> int:
        if len(self.k_min_heap) < self.k:
            heapq.heappush(self.k_min_heap, val)
        
        elif len(self.k_min_heap) == self.k:
            if val > self.k_min_heap[0]:
                heapq.heappop(self.k_min_heap)
                heapq.heappush(self.k_min_heap, val)
            
        return self.k_min_heap[0]   