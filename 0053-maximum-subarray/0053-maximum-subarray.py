class Solution(object):
    def maxSubArray(self, nums):
        csum = 0
        msum = nums[0]
        for i in range(len(nums)):
            csum = csum + nums[i]
            if csum > msum:
                msum = csum
            if csum < 0:
                csum = 0
        return msum
        