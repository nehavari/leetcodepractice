class Solution:
    
    def __init__(self):
        self.factCache = {}
        
    def factorial(self, num):
        
        if self.factCache.get(num):
            return self.factCache[num]
        
        if num == 0 or num == 1:
            result = 1
        else:
            result = num * self.factorial(num - 1)
            
        self.factCache[num] = result
        
        return result
    
    def combinations(self, num, twos):
        return self.factorial(num) / (self.factorial(twos) * self.factorial(num - twos))
    
    def climbStairs(self, n: int) -> int:
        ways = 1        
        twos = n // 2
        
        for i in range(1, twos + 1):
            ways += self.combinations(n - i, i)          
            
        return int(ways)
       
        