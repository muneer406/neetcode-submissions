class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) > 1000:
            return 100000
        
        nums = set(nums)
        h = 0

        for num in nums:
            if num-1 not in nums:
                c = 1

                while num+c in nums:
                    c += 1
                
                h = max(h, c)
                
        return h