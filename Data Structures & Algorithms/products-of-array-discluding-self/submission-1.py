class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        non_zero_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                non_zero_product *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        output = []
        for num in nums:
            if (zero_count == 1):
                output.append(non_zero_product if num == 0 else 0)
            else:
                output.append(non_zero_product // num)

        return output