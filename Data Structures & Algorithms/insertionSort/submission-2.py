# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if pairs == []:
            return []
        result = []
        result.append(pairs[:])
        for i in range(1, len(pairs)):
            j = i - 1

            while pairs[j].key > pairs[i].key and j >=0:
                #swap the elements
                temp = pairs[i]
                pairs[j + 1] = pairs[j]
                pairs[j] = temp
                j = j - 1
                i = i - 1

            result.append(pairs[:])
        return result
        