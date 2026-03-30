class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in dicto:
                dicto[sorted_word].append(word)
            else:
                dicto[sorted_word] = [word]
        return list(dicto.values())