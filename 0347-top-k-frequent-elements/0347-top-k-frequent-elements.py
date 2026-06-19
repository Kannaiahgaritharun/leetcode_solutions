class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequencies
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Convert to list of (number, frequency) pairs
        items = list(freq.items())

        # Sort by frequency descending
        items.sort(key=lambda x: x[1], reverse=True)

        # Take first k numbers
        result = []

        for num, count in items[:k]:
            result.append(num)

        return result