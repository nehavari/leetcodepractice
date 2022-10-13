class Solution:
    def compress(self, chars: List[str]) -> int:
        pointer = first = 0
        second = 1
        
        def updateArr(chars, first, second, pointer):
            chars[pointer] = chars[first]
            pointer += 1
            count = second - first
            if count > 1:
                count = str(count)
                for char in count:
                    chars[pointer] = char
                    pointer += 1
            return pointer
                    
        while second != len(chars):
            if chars[first] != chars[second]:
                pointer = updateArr(chars, first, second, pointer) 
                first = second 
            second += 1
        
        pointer = updateArr(chars, first, second, pointer) 
            
        return pointer                           