from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        frequency = Counter(nums)
        unique = list(frequency.keys())
        
        def partition(left, right):
            pivotFreq = frequency[unique[right]]
            store_index = left
            for index in range(left, right):
                if frequency[unique[index]] > pivotFreq:
                    unique[index], unique[store_index] = unique[store_index], unique[index]
                    store_index += 1
            unique[store_index], unique[right] = unique[right], unique[store_index]
            
            return store_index
        
        def select(left, right):
            pivot = partition(left, right)
            if pivot == k - 1:
                return
            elif pivot < k - 1:
                select(pivot + 1, right)
            else:
                select(left, pivot - 1)
            
        select(0, len(unique) - 1)
        return unique[:k]