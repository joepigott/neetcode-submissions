class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for s in strs:
            counts = [0 for _ in range(26)]
            for c in s:
                counts[ord(c) - ord('a')] += 1
            freqs[tuple(counts)] = freqs.get(tuple(counts), []) + [s]
        
        return list(freqs.values())