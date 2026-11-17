class Solution:
    def trap(self, height: List[int]) -> int:
        m = 0
        for i in range(1,len(height)):
            if height[i] > height[m]: m = i
        
        l, r = 0, 0
        temp = 0
        res  = 0

        while r <= m:
            hl, hr = height[l], height[r]
            if hr < hl:
                temp += hl - hr
            else:
                res += temp
                temp = 0
                l = r
            
            r += 1

        l, r = len(height) - 1, len(height) - 1
        temp = 0

        while l >= m:
            hl, hr = height[l], height[r]
            if hl < hr:
                temp += hr-hl
            else:
                res += temp
                temp = 0
                r = l
            
            l -= 1

        return res