"""
There are easier solution than however this one guaranteed to be run in O(n) time complexity even in worst case.
Space complexity is O(n) to keep medianSet array.
"""
class Solution:
    
    def partition(self, nums, pivot):
        index, left, right = 0, 0, len(nums) - 1
        while index <= right:
            if nums[index] == pivot:
                index += 1
            elif nums[index] < pivot:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            else:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
        return left
    
    def medianOfMedian(self, nums, medianIndex):
        sublists = [nums[i: i+5] for i in range(0, len(nums), 5)]
        
        medianSet = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
        
        if len(medianSet) <= 5:
            pivot = sorted(medianSet)[len(medianSet)//2]
        else:
            pivot = self.medianOfMedian(medianSet, len(medianSet)//2)
        
        pivotIndex = self.partition(nums, pivot)
        
        if pivotIndex == medianIndex:
            return pivot
        
        if medianIndex < pivotIndex:
            return self.medianOfMedian(nums[0:pivotIndex], medianIndex)
        else:
            return self.medianOfMedian(nums[pivotIndex+1:len(nums)], medianIndex-pivotIndex-1)
        
    def minMoves2(self, nums: List[int]) -> int:
        length = len(nums)
        medianIndex = (length - 1) // 2
        median = self.medianOfMedian(nums, medianIndex) # O(n) 
        distance = 0
        for num in nums: # O(n)
            distance += abs(median - num)
            
        return distance
