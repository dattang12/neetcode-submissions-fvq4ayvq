class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtracking(path, remaining):
            if len(path) == len(nums):   
                res.append(path[:])
                return

            for i in range(len(remaining)):
                path.append(remaining[i])
                backtracking(path, remaining[:i] + remaining[i+1:])
                path.pop()

        backtracking([], nums)
        unique = set(map(tuple, res))
        return [list(x) for x in unique]