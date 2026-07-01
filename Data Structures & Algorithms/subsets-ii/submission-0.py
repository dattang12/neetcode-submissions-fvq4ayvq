class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(index, path):
            res.append(path[:])
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0,[])
        
        unique = set(map(tuple, res))
        return [list(x) for x in unique]



        