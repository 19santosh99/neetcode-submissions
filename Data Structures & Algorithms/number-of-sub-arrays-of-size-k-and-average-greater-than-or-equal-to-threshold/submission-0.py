class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        greaterThanThreshHold = 0
        window_sum = 0

        # initalize the window
        for i in range(k):
            window_sum += arr[i]

        if (window_sum / k) >= threshold:
            greaterThanThreshHold += 1

        for i in range(k, len(arr)):

            # add the new element
            window_sum += arr[i]
            # remove the leftmost element
            window_sum -= arr[i-k]

            if (window_sum / k) >= threshold:
                greaterThanThreshHold += 1



        return greaterThanThreshHold