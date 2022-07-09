class Solution:
    def search(self, nums: List[int], target: int) -> int:
        firstIndex = 0
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                firstIndex = index
                break
            
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            realMid = (firstIndex + mid) % length
            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
