class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ">"
            res += s
            
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        while s:
            i = 0
            n = ""
            while s[i] != ">":
                n += s[i]
                i += 1
            
            n = int(n)
            res.append(s[i+1:n+i+1])
            s = s[n+i+1:]
        
        return res