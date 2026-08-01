class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        current_sum = 0
        max_sum = arr[0]
        for num in arr:
            current_sum = current_sum + num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
                
        