class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtracking(index, total):
            if index == len(nums):
                return total

            # include nums[i] + not include nums[i]
            return backtracking(index + 1, total ^ nums[index]) + backtracking(index + 1, total)
        return backtracking(0,0)
            

        