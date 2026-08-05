class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        results = []
        for arr in nums:
            sums = sums + arr
            results.append(sums)
        return results