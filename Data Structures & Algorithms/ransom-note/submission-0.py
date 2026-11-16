class Solution:
    def canConstruct(self, rn: str, mg: str) -> bool:
        if len(rn) > len(mg) : return False

        counts = [0]*26
        for c in mg:
            counts[ord(c) - ord('a')] += 1
        
        for c in rn:
            i = ord(c) - ord('a')
            counts[i] -= 1
            if counts[i] < 0:
                return False
            
        return True