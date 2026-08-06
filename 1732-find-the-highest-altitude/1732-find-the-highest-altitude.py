class Solution(object):
    def largestAltitude(self, gain):
        current = 0
        maximum = 0

        for num in gain:
            current = current + num

            if current > maximum:
                maximum = current

        return maximum