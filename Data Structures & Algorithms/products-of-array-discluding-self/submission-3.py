class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        n = len(nums)
        ans = [0]*n

        for num in nums:
            if num == 0: zero_count += 1
            else: prod *= num

        if zero_count > 1:
            return ans
        if zero_count == 1:
            zeroIdx = nums.index(0)
            ans[zeroIdx] = prod
            return ans
            
        return [prod//x for x in nums]