class Solution:
    dict_out = {}
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0

        if n == 0 or n == 1:
            return 1

        if n-1 in self.dict_out and n-2 not in self.dict_out:
            self.dict_out[n-2] = self.climbStairs(n-2)
            return self.dict_out[n-1] + self.dict_out[n-2]
        elif n-1 not in self.dict_out and n-2 in self.dict_out:
            self.dict_out[n-1] = self.climbStairs(n-1)
            return self.dict_out[n-2] + self.dict_out[n-1]
        elif n-1 in self.dict_out and n-2 in self.dict_out:
            return self.dict_out[n-1] + self.dict_out[n-2]
        else:
            self.dict_out[n-2] = self.climbStairs(n-2)
            self.dict_out[n-1] = self.climbStairs(n-1)
            return self.dict_out[n-1] + self.dict_out[n-2]
        