class Solution:
    def climbStairs(self, n: int) -> int:

        def memoize(n, cache):

            if n in cache:
                return cache[n]

            if n < 0:
                return 0

            if n <= 1:
                return 1

            cache[n] = memoize(n-1, cache) + memoize(n-2, cache)
            return cache[n]
        return memoize(n, {})