class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        
        for i in range(n):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining], i]
            seen[nums[i]] = i