class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sk = ''.join(sorted(s))
            groups[sk].append(s)
        
        return list(groups.values())