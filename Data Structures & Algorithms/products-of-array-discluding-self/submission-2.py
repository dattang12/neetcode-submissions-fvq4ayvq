from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        # left[i] = product of everything before index i
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        # right[i] = product of everything after index i
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # combine
        for i in range(n):
            result[i] = left[i] * right[i]

        return result