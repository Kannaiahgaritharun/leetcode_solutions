class Solution(object):
    def findNumbers(self, arr):
        output = 0
        for num in arr:
            element = num
            element_output = 0
            while element > 0:
                element = element // 10
                element_output += 1
            if element_output % 2 == 0:
                output += 1
        return output

            