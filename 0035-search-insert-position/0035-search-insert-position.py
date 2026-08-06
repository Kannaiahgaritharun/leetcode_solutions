class Solution(object):
    def searchInsert(self, arr, target):

        for i in range(len(arr)):

            if arr[i] == target:
                return i

            if arr[i] > target:
                return i

        return len(arr)
        