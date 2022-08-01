import math
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(self.nums)
        self.segTree = [0] * (2 * self.size)
        
        # assign leaf nodes
        for i, j in zip(range(self.size, 2 * self.size), range(0, self.size)):
            self.segTree[i] = self.nums[j]
            
        for i in range(self.size - 1, 0, -1):
            self.segTree[i] = self.segTree[2 * i] + self.segTree[2 * i + 1]
            
    def update(self, index: int, val: int) -> None:
        index = index + self.size
        self.segTree[index] = val
        parent = index // 2
        while parent != 0:
            left = 2 * parent
            right = 2 * parent + 1
            self.segTree[parent] = self.segTree[left] + self.segTree[right]
            parent = parent // 2
        
    def sumRange(self, left: int, right: int) -> int:
        left = left + self.size
        right = right + self.size
        ssum = 0 
        while left <= right:
            if left % 2 == 1:
                ssum += self.segTree[left]
                left += 1
            if right % 2 == 0:
                ssum += self.segTree[right]
                right -= 1
          
            left //= 2
            right //= 2
        
        return ssum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)