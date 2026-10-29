from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = defaultdict(list)
        for s in strs:
            counts = [0 for _ in range(26)]
            for c in s:
                counts[ord(c) - ord('a')] += 1
            freqs[tuple(counts)].append(s)
        
        return list(freqs.values())