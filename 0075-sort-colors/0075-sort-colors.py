class Solution:
    def sortColors(self, nums: List[int]) -> None:
     noZero = 0
     noOnes = 0
     noTwos = 0
     for num in nums:
        if num == 0:
            noZero += 1
        elif num == 1:
            noOnes += 1
        else:
            noTwos += 1
     i = 0
     while noZero != 0:
        nums[i] = 0
        i = i+1
        noZero -= 1
     while noOnes != 0:
        nums[i] = 1
        i = i+1
        noOnes -= 1
     while noTwos != 0:
        nums[i] = 2
        i = i + 1
        noTwos -= 1

        