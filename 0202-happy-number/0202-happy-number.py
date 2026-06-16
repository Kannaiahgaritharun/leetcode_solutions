class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sum = 0
            while n > 0:
                d = n % 10
                sum = sum + d * d
                n = n // 10
            n = sum
        return True
     
        

   
        