class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        n = len(nums)

        for num in nums:
            if num == 0: zero_count += 1
            else: prod *= num

        if zero_count > 1:
            return [0]*n
        if zero_count == 1:
            return [0 if x != 0 else prod for x in nums]
        if zero_count == 0:
            return [prod//x for x in nums]