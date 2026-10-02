class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagramGroups = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))

            anagramGroups[key].append(s)
        
        return list(anagramGroups.values())