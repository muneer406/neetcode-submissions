class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sk = "".join(sorted(s))
            if sk not in groups:
                groups[sk] = []
            
            groups[sk].append(s)
        
        return list(groups.values())