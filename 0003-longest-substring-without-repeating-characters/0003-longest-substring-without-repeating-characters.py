class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        longest = 0
        
        while right < len(s):
            while s[right] in s[left: right]:
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest
            
        
        