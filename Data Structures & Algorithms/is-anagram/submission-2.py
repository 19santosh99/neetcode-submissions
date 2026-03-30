from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = defaultdict(int)
        s2 = defaultdict(int)

        for c in s:
            s1[c] += 1

        for c in t:
            s2[c] += 1

        return s1 == s2
        