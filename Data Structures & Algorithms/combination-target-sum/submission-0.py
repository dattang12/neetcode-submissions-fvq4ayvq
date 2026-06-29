class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(index, path, total):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i, path, total + nums[i])
                path.pop()

        backtracking(0,[],0)
        return res