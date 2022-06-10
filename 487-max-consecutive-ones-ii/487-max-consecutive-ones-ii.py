"""
there are 2 solutions for this problem on leetcode, this is the third way it can be solved
O(n) - time complexity
O(1) - space complexity
"""
import math
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mMax = 0
        cMax = 0
        lastSingleZeroIndex = math.inf
        for i in range(len(nums)):
            if nums[i] == 1:
                cMax += 1
            else:
                if (i + 1 < len(nums) and nums[i + 1] == 1) or (i == len(nums) - 1):
                    if lastSingleZeroIndex != math.inf:
                        cMax = i - lastSingleZeroIndex
                    else:
                        cMax += 1
                    lastSingleZeroIndex = i
                else:
                    cMax = 0
                    lastSingleZeroIndex = math.inf
                    
            mMax = max(mMax, cMax)
            
        return mMax