import math
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.buffer_len = math.ceil(math.sqrt(len(nums)))
        self.buffer = [0] * self.buffer_len
        for index in range(len(self.nums)):
            self.buffer[index // self.buffer_len] += self.nums[index]
        
        
    def update(self, index: int, val: int) -> None:
        buffer_ind = index // self.buffer_len
        self.buffer[buffer_ind] = self.buffer[buffer_ind] - self.nums[index] + val
        self.nums[index] = val
      
    def sumRange(self, left: int, right: int) -> int:
        sumR = 0
        startBlock = left // self.buffer_len
        endBlock = right // self.buffer_len
        if startBlock == endBlock:
            for i in range(left, right + 1):
                sumR += self.nums[i]
        else:
            for i in range(left, (startBlock + 1) * self.buffer_len):
                sumR += self.nums[i]
            for i in range(startBlock + 1, endBlock):
                sumR += self.buffer[i]
            for i in range(endBlock * self.buffer_len, right + 1):
                sumR += self.nums[i]
                
        return sumR


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)