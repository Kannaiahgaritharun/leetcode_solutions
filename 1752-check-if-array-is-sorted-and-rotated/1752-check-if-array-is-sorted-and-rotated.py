class Solution(object):
    def check(self, nums):
        num = sorted(nums)
        for i in range(len(nums)):
            rotated = num[i:] + num[:i]
            if rotated == nums:
                return True
        return False


            
    
        
