class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtracking(index, path):
            res.append(path[:])  # every path is a valid subset

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue  # skip duplicates at same tree level
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        backtracking(0, [])
        return res