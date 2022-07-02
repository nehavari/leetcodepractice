from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        sList = deque()
        word = []
        for char in s:
            if char != ' ':
                word.append(char)
            else:
                if word:
                    word = ''.join(word)
                    sList.appendleft(word)
                word = []
        if word:
            word = ''.join(word)
            sList.appendleft(word)
        
        return ' '.join(sList)