class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums.sort()
        maxL, l = 1, 1

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                l += 1
                maxL = max(maxL, l)
            elif nums[i] - nums[i-1] == 0: continue
            else: 
                l = 1
            
        return maxL