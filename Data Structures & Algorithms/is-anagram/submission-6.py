from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        output_dict = {}
        output_dict2 = {}
        for c in s:
            if c in output_dict:
                output_dict[c] += 1
            else:
                output_dict[c] = 1

        for c in t:
            if c in output_dict2:
                output_dict2[c] += 1
            else:
                output_dict2[c] = 1
        
        return output_dict == output_dict2
        