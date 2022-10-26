class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and char == stack[-1][0]:
                stack.append((char, stack[-1][1] + 1))
            else:
                stack.append((char, 1))
            
            if stack[-1][1] >= k:
                count = k
                while count:
                    stack.pop()
                    count -= 1
        
        return "".join([ele[0] for ele in stack])