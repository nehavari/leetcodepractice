class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n == 0:
                return 1.0

            ans = fastPow(x, n//2)

            if n % 2 == 0:
                ans = ans * ans
            else:
                ans = x * ans * ans
            return ans
        
        if n < 0:
            n, x = -n, 1/x
            
        return fastPow(x, n)
    
        