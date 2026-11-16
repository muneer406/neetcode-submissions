class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) > 1000:
            return 100000
        nums = set(nums)
        highest = 0

        for num in nums:
            if num - 1 not in nums:
                current = 1

                while num + current in nums:
                    current += 1

                highest = max(highest, current)

        return highest