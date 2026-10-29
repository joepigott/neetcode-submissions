class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_counts, t_counts = {}, {}
        for c in s:
            s_counts[c] = s_counts.get(c, 0) + 1
        
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1

        return s_counts == t_counts