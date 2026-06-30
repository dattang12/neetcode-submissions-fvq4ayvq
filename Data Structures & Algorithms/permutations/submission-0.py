class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(path, remaining):
            if len(path) == len(nums):   
                res.append(path[:])
                return
            
            for num in remaining:
                path.append(num)
                backtracking(path, remaining - {num})
                path.pop()
            
        backtracking([], set(nums))
        return res
        