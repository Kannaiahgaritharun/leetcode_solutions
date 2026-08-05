class Solution:
    def maximumWealth(self, arr: List[List[int]]) -> int:
        sums = []
        for num in arr:
            s = 0
            for nums in num:
                s = s+nums
            sums.append(s)
        maximum_sum = sums[0]
        for value in sums:
            if value > maximum_sum:
                maximum_sum = value
        return maximum_sum



        